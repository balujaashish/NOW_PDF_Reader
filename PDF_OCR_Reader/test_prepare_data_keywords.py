import unittest
from prepare_data_keywords import Prepare_Data_Keywords

class testPrepareDataKeyword(unittest.TestCase):

    def setUp(self):
        self.x = Prepare_Data_Keywords()


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



if __name__ == "__main__":
    unittest.main()