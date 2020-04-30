import unittest
from prepare_data_keywords import Prepare_Data_Keywords

class testPrepareDataKeyword(unittest.TestCase):

    def setUp(self):
        self.x = Prepare_Data_Keywords()

    def get_term(self, e):
        return e[3]

    def get_key_term(self, e):
        return e[3]

    def test_tokenize_keyword(self):
        phrase = "hey, how's it going?"
        out_put = self.x.tokenize_keyword(phrase)
        self.assertEqual(out_put, ['hey', ',', 'how', "'s", 'it', 'going', '?'])
        # no split
        phrase = "hey"
        out_put = self.x.tokenize_keyword(phrase)
        self.assertEqual(out_put, ['hey'])
        # only spaces
        phrase = "hey you"
        out_put = self.x.tokenize_keyword(phrase)
        self.assertEqual(out_put, ['hey', 'you'])
        # split using comma
        phrase = "tom,harry,sally"
        out_put = self.x.tokenize_keyword(phrase)
        self.assertEqual(out_put, ['tom',',','harry',',','sally'])
        # blank
        phrase = ''
        out_put = self.x.tokenize_keyword(phrase)
        self.assertEqual(out_put, [])
        # capital
        phrase = "Tom,Harry,Sally"
        out_put = self.x.tokenize_keyword(phrase)
        self.assertEqual(out_put, ['tom',',','harry',',','sally'])


    def test_get_vocab(self):
        d = {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871'],[9829,939,921,'fhc']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'Qty (Unit)']]}
        out_put = self.x.get_vocab(d, self.get_term, self.get_key_term)
        self.assertEqual(out_put,{'Amount', 'AE10071871', 'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel', 'fhc', 'Qty (Unit)', 'keywords', 'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States', 'Purchase Order Number', 'Addresses'})
        # single entry dictionary
        d = {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871'],[9829,939,921,'fhc']]}
        out_put = self.x.get_vocab(d, self.get_term, self.get_key_term)
        self.assertEqual(out_put,{'AE10071871', 'fhc', 'Purchase Order Number'})
        # single term in dict value
        d = {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'Qty (Unit)']]}
        out_put = self.x.get_vocab(d, self.get_term, self.get_key_term)
        self.assertEqual(out_put,{'Amount', 'AE10071871', 'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel', 'Qty (Unit)', 'keywords', 'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States', 'Purchase Order Number', 'Addresses'})

        d = {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871']]}
        out_put = self.x.get_vocab(d, self.get_term, self.get_key_term)
        self.assertEqual(out_put,{'AE10071871', 'Purchase Order Number'})
        # empty dict
        d = {}
        out_put = self.x.get_vocab(d, self.get_term, self.get_key_term)
        self.assertEqual(out_put,{})
        # empty value for dict
        d = {(2000010, 838, 8389,'Purchase Order Number'): []}
        out_put = self.x.get_vocab(d, self.get_term, self.get_key_term)
        self.assertEqual(out_put,{'Purchase Order Number'})
        
    def test_tokenize_keywords_dictionary(self):
        d = {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871'],[9829,939,921,'fhc']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'Qty (Unit)']]}
        out_put = self.x.tokenize_keywords_dictionary(d)
        self.assertEqual(out_put, {'fhc': ['fhc'], 'Purchase Order Number': ['purchase', 'order', 'number'], 'Amount': ['amount'], 'keywords': ['keywords'], 'Qty (Unit)': ['qty', '(', 'unit', ')'], 'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States': ['boardwalktech', ',', 'inc', '10050', 'n', '.', 'wolfe', 'rd', '.', '#', '276', 'cupertino', ',', 'ca', '95014', 'united', 'states'], 'AE10071871': ['ae10071871'], 'Addresses': ['addresses'], 'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel': ['teva', 'bazel', '5', '5', 'bazel', 'st', '.', '4951033', 'petah', 'tikva', 'israel']})

        # single entry dictionary
        d = {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871'],[9829,939,921,'fhc']]}
        out_put = self.x.tokenize_keywords_dictionary(d)
        self.assertEqual(out_put,{'fhc': ['fhc'], 'AE10071871': ['ae10071871'], 'Purchase Order Number': ['purchase', 'order', 'number']})

        # single term in dict value
        d = {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'Qty (Unit)']]}
        out_put = self.x.tokenize_keywords_dictionary(d)
        self.assertEqual(out_put,{'Addresses': ['addresses'], 'keywords': ['keywords'], 'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel': ['teva', 'bazel', '5', '5', 'bazel', 'st', '.', '4951033', 'petah', 'tikva', 'israel'], 'Amount': ['amount'], 'Qty (Unit)': ['qty', '(', 'unit', ')'], 'Purchase Order Number': ['purchase', 'order', 'number'], 'AE10071871': ['ae10071871'], 'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States': ['boardwalktech', ',', 'inc', '10050', 'n', '.', 'wolfe', 'rd', '.', '#', '276', 'cupertino', ',', 'ca', '95014', 'united', 'states']})
        # -----
        d = {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871']]}
        out_put = self.x.tokenize_keywords_dictionary(d)
        self.assertEqual(out_put,{'Purchase Order Number': ['purchase', 'order', 'number'], 'AE10071871': ['ae10071871']})

        # empty dict
        d = {}
        out_put = self.x.tokenize_keywords_dictionary(d)
        self.assertEqual(out_put,{})

        # empty value for dict
        d = {(2000010, 838, 8389,'Purchase Order Number'): []}
        out_put = self.x.tokenize_keywords_dictionary(d)
        self.assertEqual(out_put,{'Purchase Order Number': ['purchase', 'order', 'number']})




if __name__ == "__main__":
    unittest.main()