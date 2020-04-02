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

    

if __name__ == "__main__":
    unittest.main()