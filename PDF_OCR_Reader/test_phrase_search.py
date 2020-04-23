import unittest
from phrase_search import Phrase_Search
import z_test_data
from token_network import Token_Network
from String_compare import String_Compare
 

class TestPhraseSearch(unittest.TestCase):
    
    def setUp(self):
        self.x = Phrase_Search()

    def get_top1(self,e):
        return e[7]

    def get_left1(self,e):
        return e[6]

    def get_height1(self,e):
        return e[9]

    def get_width1(self,e):
        return e[8]
    
    def get_term1(self, e):
        return e[11]

    def get_direction1(self, e):
        return e[1][0]

    def get_order_key(self, e):
        return e[12]

    def get_order_value(self, e):
        return e[0][12]

    def get_distance(self, e):
        return e[1][1]

    def test_search_phrase_in_document_network(self):
        search_str = ['purchase', 'order', ':', 'ae10071871']
        p_distance = 50
        p_data = {(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('down', 198)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('down', 198)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1): [[[5, 1,
        1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('left', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('left', 32)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 335)]], (5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0): [[[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('right', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0): [[[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('left', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]]}

        key = (5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0)

        match = self.x.search_phrase_in_document_network(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance, 0) 
        
        # print(match)
        
        self.assertEqual(match, [(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0), [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)]])
        
        self.assertEqual(len(match), len(search_str))

        key = (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0)
        match = self.x.search_phrase_in_document_network(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, 0, p_distance) 
        self.assertEqual(match, [])

        self.assertNotEqual(len(match), len(search_str))

        # two terms
        search_str = ['order', ':']
        key = (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0)

        match = self.x.search_phrase_in_document_network(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance, 0) 
        self.assertEqual(match, [(5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0), [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)]])
        self.assertEqual(len(match), len(search_str))
        
        
    def test_search(self):
        search_str = ['purchase', 'order', ':', 'ae10071871']
        p_distance = 50
        p_data = {(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('down', 198)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('down', 198)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1): [[[5, 1,
        1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('left', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('left', 32)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 335)]], (5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0): [[[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('right', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0): [[[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('left', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]]}

        key = (5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0)
        match = self.x.search(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance, 0) 
        # print(match)
        self.assertEqual(match, [(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0), [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]])
        self.assertEqual(len(match), len(search_str))

        key = (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0)
        match = self.x.search(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance, 0) 
        self.assertEqual(match, [])

        self.assertNotEqual(len(match), len(search_str))

        # two terms
        search_str = ['order', ':']
        key = (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0)
        match = self.x.search(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance, 0) 
        self.assertEqual(match, [(5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0), [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)]])
        self.assertEqual(len(match), len(search_str))


        # single term
        search_str = ['order']
        key = (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0)
        match = self.x.search(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance, 0) 
        self.assertEqual(match, [(5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0)])
        self.assertEqual(len(match), len(search_str))


        


if __name__ == "__main__":
    unittest.main()
    # ps = TestPhraseSearch()
    # ps.setUp()
    # ps.test_search_phrase_in_document_network()
