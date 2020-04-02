import unittest
from Sort_list import sort_List

class testSortList(unittest.TestCase):

    def setUp(self):
        self.x = sort_List()
    
    def test_sort_2D_list(self):
        l_list = [[1,1,'a'], [1,1,'d'], [1,1,'c']]
        l_position = 3
        self.assertEqual(self.x.sort_2D_list(l_list,l_position),[[1,1,'a'], [1,1,'c'], [1,1,'d']])
        
        l_list = [[1,1,'a'], [1,1,'2'], [1,1,'c']]
        l_position = 3
        y = self.x.sort_2D_list(l_list,l_position)
        self.assertEqual(y,[[1,1,'2'], [1,1,'a'], [1,1,'c']])
        self.assertGreaterEqual(y[2][l_position-1],y[1][l_position-1])

        l_list = [[1,3,'fwf'], [2,3,'hd'], [3,3,'iosd'], [2,83,'kFf'], [93,3,'sndsfkmsS'], [4,3,'YSDVG'],[5,3,'kFf'], [6,3,'dffv'],[2,3,'8834']]
        l_position = 3
        y = self.x.sort_2D_list(l_list,l_position)
        i = 0
        len_y = len(y)
        while i < len_y-1:
            self.assertGreaterEqual(y[i+1][l_position-1].lower(),y[i][l_position-1].lower())
            i = i+1
        


        
if __name__ == "__main__":
    unittest.main()