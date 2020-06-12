import unittest
from Expression.keywords import Keywords
import z_test_data

class testKeywords(unittest.TestCase):

    def setUp(self):
        self.PDF_Info = z_test_data.PDF_Info
        self.supporting_data = []
        self.attributes = []
        self.x = Keywords(self.PDF_Info, self.supporting_data, self.attributes)

    def test_get(self):
        keyWord = 'February 20, 2020'
        out_put = self.x.get(keyWord)
        for o in out_put:
            print(o)
        print('------------------out_put-----------------')
        keyWord = 'February 29'
        out_put = self.x.get(keyWord)
        # out_put =self.x.strip_details(out_put)
        print(out_put)
        print('------------------out_put-----------------')

    def test_synonyms_keyword(self):
        pass

    def test_search_keyword_pdf_info(self):
        keyWord = 'February 20, 2020'
        out_put = self.x.search_keyword_pdf_info(keyWord)
        for o in out_put:
            print(o)

        keyWord = 'February 20, 2022'
        out_put = self.x.search_keyword_pdf_info(keyWord)
        

    def test_qualify(self):
        l_key = ('February 20, 2020', ('february', '20', ',', '2020'))
        l_pdf_keyword = [(5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0), [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 22)], [[5, 1, 4, 1, 2, 5, 1487, 1056, 93, 62, 94, ',', 1], ('down', 21)], [[5, 1, 4, 1, 2, 6, 1609, 1056, 156, 53, 95, '2020', 0], ('right', 29)]]
        out_put = self.x.qualify(l_key, l_pdf_keyword)
        print(out_put)

    def test_strip_details(self):
        keywords = [[(5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0), [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 22)], [[5, 1, 4, 1, 2, 5, 1487, 1056, 93, 62, 94, ',', 1], ('down', 21)], [[5, 1, 4, 1, 2, 6, 1609, 1056, 156, 53, 95, '2020', 0], ('right', 29)]], [(5, 1, 4, 1, 2, 4, 1179, 1056, 285, 67, 95, 'February', 0), [[5, 1, 4, 1, 2, 5, 1487, 1056, 93, 62, 94, '20', 0], ('right', 23)], [[5, 1, 4, 1, 2, 5, 1487, 1056, 93, 62, 94, ',', 1], ('right', 23)], [[5, 1, 4, 1, 2, 6, 1609, 1056, 156, 53, 95, '2020', 0], ('right', 29)]]]
        out_put = self.x.strip_details(keywords)
        print(out_put)


if __name__ == "__main__":
    # unittest.main()
    TK = testKeywords()
    TK.setUp()
    TK.test_search_keyword_pdf_info()