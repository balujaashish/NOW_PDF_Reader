import unittest
from String_compare import String_Compare

class testStringComapare(unittest.TestCase):

    def setUp(self):
        self.x = String_Compare()

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

       

    

if __name__ == "__main__":
    unittest.main()