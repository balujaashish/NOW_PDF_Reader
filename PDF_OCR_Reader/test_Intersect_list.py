import unittest
from Intersect_list import Intersect_List
from operator import itemgetter

class testIntersectList(unittest.TestCase):
    
    def setUp(self):
        self.x = Intersect_List()
        self.l1 = [[1,3,'fwf'], [2,3,'hd'], [3,3,'iosd'], [4,3,'kFf'], [5,3,'sndsfkmsS'], [6,3,'YSDVG'],[7,3,'kFf'], [8,3,'dffv'],[9,3,'8834'], [10,3,'iosd'], [11,3,'kFf'],[12,3,'8834']]
        self.p1 = 3
        self.l1 = sorted(self.l1, key=itemgetter(self.p1-1))
        self.l2 = [[100,1,'kFf'],[200,1,'8834']]
        self.p2 = 3



    def test_Intersect_2_lists (self):
        self.assertEqual(self.x.Intersect_2_lists(self.l1, self.p1, self.l2, self.p2),[[[100, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[200, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]])

        l1 = [[1,3,'kFf']]
        self.assertEqual(self.x.Intersect_2_lists(l1, self.p1, self.l2, self.p2),[[[100, 1, 'kFf'], [1, 3, 'kFf']]])

        l2 = [[193,1,'kFf']]   
        self.assertEqual(self.x.Intersect_2_lists(self.l1, self.p1, l2, self.p2),[[[193,1,'kFf'],[4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']]])

        self.assertEqual(self.x.Intersect_2_lists(self.l1, self.p1, [], self.p2),[])

        self.assertEqual(self.x.Intersect_2_lists([], self.p1, self.l2, self.p2),[])

if __name__ == '__main__':
    unittest.main()