import unittest
from Data_cleaner import Data_Cleaner

class testDataCleaner(unittest.TestCase):

    def setUp(self):
        self.x = Data_Cleaner()
        self.y = [[1,2,'tfd'], [1,2,'df'], [1,2,'rf'], [1,2,''], [1,2,'rf']]
        self.t = ((1,2,'tfd'), (1,2,'df'), (1,2,'rf'), (1,2,''), (1,2,'rf'))

    def test_remove_blanks(self):    
        y = self.x.remove_blanks(self.y,3)
        self.assertEqual(len(y),4)
        [self.assertNotEqual(r[2],'') for r in y]
        self.assertEqual(self.x.remove_blanks([],3),[])
        self.assertRaises(TypeError, self.x.remove_blanks, True, 3)
        y = self.x.remove_blanks(self.t,3)
        self.assertEqual(len(y),4)
        [self.assertNotEqual(r[2],'') for r in y]

if __name__ == "__main__":
    unittest.main()