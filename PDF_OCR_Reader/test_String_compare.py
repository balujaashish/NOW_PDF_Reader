import unittest
from String_compare import String_Compare

class testStringComapare(unittest.TestCase):

    def setUp(self):
        self.x = String_Compare()

    def get_term(self, e):
        return e[2]

    def test_str_compare(self):
        str1 = 'ffwe'
        str2 = 'ffwe'
        self.assertEqual(self.x.str_compare(str1,str2),1)
        str1 = 'ffwe'
        str2 = 'kfwe'
        self.assertEqual(self.x.str_compare(str1,str2),3)
        str1 = 'kfwe'
        str2 = 'ffwe'
        self.assertEqual(self.x.str_compare(str1,str2),2)
        str1 = '992'
        str2 = 'ffwe'
        self.assertEqual(self.x.str_compare(str1,str2),3)
        str1 = []
        str2 = 'ffwe'
        self.assertEqual(self.x.str_compare(str1,str2),0)
        str1 = 'ffwe'
        str2 = 'Ffwe'
        self.assertEqual(self.x.str_compare(str1,str2),1)
        str1 = 'KH87HG6'
        str2 = 'kh87hg6'
        self.assertEqual(self.x.str_compare(str1,str2),1)
        str1 = 'KH8-7HG6'
        str2 = 'kh8-7hg6'
        self.assertEqual(self.x.str_compare(str1,str2),1)

    def test_str_compare_basic(self):
        str1 = 'ffwe'
        str2 = 'ffwe'
        self.assertEqual(self.x.str_compare_basic(str1,str2),1)
        str1 = 'ffwe'
        str2 = 'kfwe'
        self.assertEqual(self.x.str_compare_basic(str1,str2),0)
        str1 = 'kfwe'
        str2 = 'ffwe'
        self.assertEqual(self.x.str_compare_basic(str1,str2),0)
        str1 = '992'
        str2 = 'ffwe'
        self.assertEqual(self.x.str_compare_basic(str1,str2),0)
        str1 = []
        str2 = 'ffwe'
        self.assertEqual(self.x.str_compare_basic(str1,str2),0)
        str1 = 'ffwe'
        str2 = 'Ffwe'
        self.assertEqual(self.x.str_compare_basic(str1,str2),1)
        str1 = 'KH87HG6'
        str2 = 'kh87hg6'
        self.assertEqual(self.x.str_compare_basic(str1,str2),1)
        str1 = 'KH8-7HG6'
        str2 = 'kh8-7hg6'
        self.assertEqual(self.x.str_compare_basic(str1,str2),1)

    def test_str_prepare(self):
        self.assertEqual(self.x.str_prepare('SJS'),'sjs')
        self.assertEqual(self.x.str_prepare('12345'),'12345')
        self.assertEqual(self.x.str_prepare('GsjhnDjHGD'),'gsjhndjhgd')
        self.assertEqual(self.x.str_prepare(' GsjhnDjHGD'),'gsjhndjhgd')
        self.assertEqual(self.x.str_prepare('GsjhnDjHGD '),'gsjhndjhgd')
        self.assertEqual(self.x.str_prepare('   GsjhnDjHGD  '),'gsjhndjhgd')
        self.assertEqual(self.x.str_prepare('GsjhnDjHGD,'),'gsjhndjhgd')
        self.assertEqual(self.x.str_prepare('(GsjhnDjHGD'),'gsjhndjhgd')
        self.assertEqual(self.x.str_prepare('Gsjhn-DjHGD'),'gsjhndjhgd')
        self.assertEqual(self.x.str_prepare(' @Gsj$hn-DjHGD & '),'gsjhndjhgd')

    def test_prepare_phrase(self):
        phrase = 'go for it!'
        out_put = self.x.prepare_phrase(phrase,0)
        self.assertEqual(out_put,['go', 'for', 'it', '!'])
        # empty string
        phrase = ''
        out_put = self.x.prepare_phrase(phrase,0)
        self.assertEqual(out_put,[])
        # space at both ends
        phrase = '  go for it!  '
        out_put = self.x.prepare_phrase(phrase,0)
        self.assertEqual(out_put,['go', 'for', 'it', '!'])
        # punctuations 
        phrase = ',  go. for it!  '
        out_put = self.x.prepare_phrase(phrase, 0)
        self.assertEqual(out_put,[',','go', '.', 'for', 'it', '!'])

    def test_pdf_data_tokenize(self):
        p = [['1','2','game'], ['1','2','reserved'], ['1','2','john.doe@boardwalktech.com'], ['1','2','game']]
        out_put = self.x.pdf_data_tokenize(p, 2, self.get_term, 0)
        self.assertEqual(out_put,[['1', '2', 'game', 0], ['1', '2', 'reserved', 0], ['1', '2', 'john.doe', 0], ['1', '2', '@', 1], ['1', '2', 'boardwalktech.com', 2], ['1', '2', 'game', 0]])

        p = []
        out_put = self.x.pdf_data_tokenize(p, 2, self.get_term, 0)
        self.assertEqual(out_put,[])

        p = [['1','2','game']]
        out_put = self.x.pdf_data_tokenize(p, 2, self.get_term, 0)
        self.assertEqual(out_put,[['1','2','game', 0]])

        p = [['1','2','game, time @ india']]
        out_put = self.x.pdf_data_tokenize(p, 2, self.get_term, 0)
        self.assertEqual(out_put,[['1','2','game', 0],['1','2',',', 1],['1','2','time', 2], ['1','2','@', 3], ['1','2','india', 4]])




if __name__ == "__main__":
    unittest.main()