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
    
    def get_term2(self, e):
        return e[1]

    def test_search_phrase_in_document_network(self):
        search_str = ['purchase', 'order', ':', 'ae10071871']
        p_distance = 50
        p_data = {(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('down', 198)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('down', 198)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1): [[[5, 1,
        1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('left', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('left', 32)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 335)]], (5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0): [[[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('right', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0): [[[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('left', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]]}

        key = (5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0)

        match = self.x.search_phrase_in_document_network(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance) 
        
        # print(match)
        
        self.assertEqual(match, [(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0), [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]])
        
        self.assertEqual(len(match), len(search_str))

        key = (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0)
        match = self.x.search_phrase_in_document_network(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance) 
        self.assertEqual(match, [])

        self.assertNotEqual(len(match), len(search_str))

        # two terms
        search_str = ['order', ':']
        key = (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0)

        match = self.x.search_phrase_in_document_network(p_data, key, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance) 
        self.assertEqual(match, [(5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0), [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)]])
        self.assertEqual(len(match), len(search_str))
        
        
    def test_search(self):
        search_str = ['purchase', 'order', ':', 'ae10071871']
        p_distance = 50
        p_data = {(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('down', 198)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('down', 198)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1): [[[5, 1,
        1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('left', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('left', 32)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 335)]], (5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0): [[[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('right', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0): [[[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('left', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]]}

        match = self.x.search(p_data, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance) 

        # print(match)
        self.assertEqual(match, [[(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0), [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]]])
        self.assertEqual(len(match[0]), len(search_str))

        search_str = ['purchamse', 'order', ':', 'ae10071871']
        match = self.x.search(p_data, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance) 
        self.assertEqual(match, [])

        self.assertNotEqual(len(match), len(search_str))

        # two terms
        search_str = ['order', ':']
        match = self.x.search(p_data, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance) 
        self.assertEqual(match, [[(5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0), [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)]]])
        self.assertEqual(len(match[0]), len(search_str))


        # single term
        search_str = ['order']
        match = self.x.search(p_data, search_str, self.get_term1, self.get_direction1, self.get_distance, self.get_order_key, self.get_order_value, p_distance) 
        self.assertEqual(match, [[(5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0)]])
        self.assertEqual(len(match), len(search_str))

    def test_search_first_term_phrase(self):
        p_data = {(1,'x'):[1,1], (2,'y'):[1,2], (3,'u'):[1,3], (4,'z'):[1,4]}
        phrase_tokens = ['x','a']
        out_put = self.x.search_first_term_phrase(p_data, phrase_tokens, self.get_term2)
        self.assertEqual(out_put, {(1, 'x'): [1, 1]})

    def test_reverse_list_from_index(self):
        l = [1,2,3,4,5]
        out_put = self.x.reverse_list_from_index(l,2)
        self.assertEqual(out_put, [1, 2, 5, 4, 3])

        # single item list
        l = [1]
        out_put = self.x.reverse_list_from_index(l,0)
        self.assertEqual(out_put, [1])

        # index out of range
        l = [1,2,3,4,5]
        out_put = self.x.reverse_list_from_index(l,10)
        self.assertEqual(out_put, [1,2,3,4,5])

        # reverse from first 
        l = [1,2,3,4,5]
        out_put = self.x.reverse_list_from_index(l,0)
        self.assertEqual(out_put, [5,4,3,2,1])

        # reverse from last
        l = [1,2,3,4,5]
        out_put = self.x.reverse_list_from_index(l,4)
        self.assertEqual(out_put, [1, 2, 3, 4, 5])

    def test_add_to_match(self):
        p = [[[1,2,3,4],('a','b')],[[1,2,3,5],('a','c')],[[1,2,3,6],('a','d')],[[1,2,3,7],('a','e')]]
        p_term = [[[1,2,3,5],('right','c')],[[1,2,3,7],('down','e')]]
        out_put = self.x.add_to_match(p, p_term)
        self.assertEqual(out_put, [[[1, 2, 3, 5], ('right', 'c')], [[1, 2, 3, 7], ('down', 'e')], [[1, 2, 3, 4], ('a', 'b')], [[1, 2, 3, 6], ('a', 'd')]])
        # no match found in p
        p = [[[1,2,3,4],('a','b')],[[1,2,3,5],('a','c')],[[1,2,3,6],('a','d')],[[1,2,3,7],('a','e')]]
        p_term = [[[1,2,3,15],('right','c')],[[1,2,3,27],('down','e')]]
        out_put = self.x.add_to_match(p, p_term)
        self.assertEqual(out_put, [[[1,2,3,15],('right','c')],[[1,2,3,27],('down','e')],[[1,2,3,4],('a','b')],[[1,2,3,5],('a','c')],[[1,2,3,6],('a','d')],[[1,2,3,7],('a','e')]])
        # empty p
        p = []
        p_term = [[[1,2,3,15],('right','c')],[[1,2,3,27],('down','e')]]
        out_put = self.x.add_to_match(p, p_term)
        self.assertEqual(out_put, [[[1,2,3,15],('right','c')],[[1,2,3,27],('down','e')]])
        # single term in p match
        p = [[[1,2,3,4],('a','b')]]
        p_term = [[[1,2,3,15],('right','c')],[[1,2,3,4],('down','e')]]
        out_put = self.x.add_to_match(p, p_term)
        self.assertEqual(out_put, [[[1,2,3,15],('right','c')],[[1,2,3,4],('down','e')]])
        # single term in p no match
        p = [[[1,2,3,4],('a','b')]]
        p_term = [[[1,2,3,15],('right','c')],[[1,2,3,344],('down','e')]]
        out_put = self.x.add_to_match(p, p_term)
        self.assertEqual(out_put, [[[1,2,3,15],('right','c')],[[1,2,3,344],('down','e')], [[1,2,3,4],('a','b')]])


        
        


if __name__ == "__main__":
    unittest.main()
    # ps = TestPhraseSearch()
    # ps.setUp()
    # ps.test_search_phrase_in_document_network()
