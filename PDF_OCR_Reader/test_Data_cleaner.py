import unittest
from Data_cleaner import Data_Cleaner

class testDataCleaner(unittest.TestCase):

    def setUp(self):
        self.x = Data_Cleaner()
        self.y = [[1,2,'tfd'], [1,2,'df'], [1,2,'rf'], [1,2,''], [1,5,' '], [1,2,'rf']]
        self.t = ((1,2,'tfd'), (1,2,'df'), (1,2,'rf'), (1,2,''), (1,2,'rf'))

    def get_key(self,e):
        return e[2]

    def test_remove_blanks(self):    
        y = self.x.remove_blanks(self.y,self.get_key)
        # print(y)
        self.assertEqual(len(y),4)
        [self.assertNotEqual(r[2],'') for r in y]
        self.assertEqual(self.x.remove_blanks([],3),[])
        self.assertRaises(TypeError, self.x.remove_blanks, True, 3)
        y = self.x.remove_blanks(self.t,self.get_key)
        # print(y)
        self.assertEqual(len(y),4)
        [self.assertNotEqual(r[2],'') for r in y]

    def test_convert_string_to_int_at_indexes(self):
        l_test_data = [['5', '1', '1', 'Purchase'],
        ['5', '77', '91', 'Order:'],
        ['558', '76', '88', 'AE10071871']]   
        indexes = [0]
        output = self.x.convert_string_to_int_at_indexes(l_test_data, indexes)
        for o in output:
            self.assertEqual(type(o[0]),int)

        # blank index array
        l_test_data = [['5', '1', '1', 'Purchase'],
        ['5', '77', '91', 'Order:'],
        ['558', '76', '88', 'AE10071871']]  
        indexes = []
        output = self.x.convert_string_to_int_at_indexes(l_test_data, indexes)
        for o in output:
            self.assertEqual(type(o[0]),str)
        
        # blank pdf
        l_test_data = []  
        indexes = [0]
        output = self.x.convert_string_to_int_at_indexes(l_test_data, indexes)
        for o in output:
            self.assertEqual(output,[])

        # last index
        l_test_data = [['5', '1', '1', '83'],
        ['5', '77', '91', '93'],
        ['558', '76', '88', '73']]  
        indexes = [3]
        output = self.x.convert_string_to_int_at_indexes(l_test_data, indexes)
        for o in output:
            self.assertEqual(type(o[3]),int)

        # middle index
        l_test_data = [['5', '1', '1', '83'],
        ['5', '77', '91', '93'],
        ['558', '76', '88', '73']]  
        indexes = [2]
        output = self.x.convert_string_to_int_at_indexes(l_test_data, indexes)
        for o in output:
            self.assertEqual(type(o[2]),int)

        # index out of range
        l_test_data = [['5', '1', '1', '83'],
        ['5', '77', '91', '93'],
        ['558', '76', '88', '73']]  
        indexes = [4]
        output = self.x.convert_string_to_int_at_indexes(l_test_data, indexes)
        self.assertEqual(output,[['5', '1', '1', '83'], ['5', '77', '91', '93'], ['558', '76', '88', '73']])

        # multiple index
        l_test_data = [['5', '1', '1', 'Purchase'],
        ['5', '77', '91', 'Order:'],
        ['558', '76', '88', 'AE10071871']]   
        indexes = [0,2,1]
        output = self.x.convert_string_to_int_at_indexes(l_test_data, indexes)
        for o in output:
            for i in indexes:
                self.assertEqual(type(o[i]),int)

        # convert string, blank, date.
        l_test_data = [['5', '1', '1', 'Purchase'],
        ['5', '77', '91', ''],
        ['558', '76', '88', '12/1/2010']]   
        indexes = [3]
        output = self.x.convert_string_to_int_at_indexes(l_test_data, indexes)
        for o in output:
            self.assertEqual(type(o[3]),str)

    
    def test_clean_pdf_data(self):
        l_test_data = [['5', '1', 'sksk', '83'],
        ['5', '77', 'kkd', '93'],
        ['558', '76', '  ', '73'],
        ['558', '76', ' dkdkd ', '73']] 
        indexes = [0,1,3]
        output  = self.x.clean_pdf_data(l_test_data, self.get_key, indexes)
        for o in output:
            for i in indexes:
                self.assertEqual(type(o[i]),int)
        self.assertEqual(len(output),3)


    def test_is_punctuation(self):
        self.assertTrue(self.x.is_punctuation(','))
        self.assertTrue(self.x.is_punctuation(''))
        self.assertFalse(self.x.is_punctuation('kdk'))
        self.assertFalse(self.x.is_punctuation(',jdk'))
        self.assertFalse(self.x.is_punctuation('.023'))

    def test_is_ignore_term(self):
        self.assertTrue(self.x.is_ignore_term(','))
        self.assertTrue(self.x.is_ignore_term(''))
        self.assertTrue(self.x.is_ignore_term(' , '))
        self.assertFalse(self.x.is_ignore_term(',kdl'))
        self.assertFalse(self.x.is_ignore_term('  kd ;s s,'))



if __name__ == "__main__":
    unittest.main()