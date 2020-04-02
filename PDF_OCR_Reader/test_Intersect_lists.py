import unittest
from Intersect_lists import Intersect_Lists
from operator import itemgetter
from multiprocessing import Queue
from Sort_list import sort_List


class testINtersectLists(unittest.TestCase):

    def setUp(self):
        self.x = Intersect_Lists()
        self.sl = sort_List()
        self.l = [[1,3,'fwf'], [2,3,'hd'], [3,3,'iosd'], [4,3,'kFf'], [5,3,'sndsfkmsS'], [6,3,'YSDVG'],[7,3,'kFf'], [8,3,'dffv'],[9,3,'8834'], [10,3,'iosd'], [11,3,'kFf'],[12,3,'8834']]
        self.p = 3
        self.l = self.sl.sort_2D_list(self.l,self.p)
        self.y =  {(1,4,'a'): [[1,1,'kFf'],[2,1,'8834']],(2,4,'b'):[[1,2,'nkrnr'], [2,2,'sndsfkmsS']],(3,4,'c'):[[1,3,'kFf'], [2,3,'sndsfkmsS']]}
        self.key_position = 3



    def test_Intersect_list_item(self):
        return_obj = self.x.Intersect_list_item(self.l, self.p, (1,4,'a'), [[100,1,'kFf'],[200,1,'8834']], self.key_position)
        self.assertEqual(return_obj, {(1, 4, 'a'): [[[100, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[200, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]]})

        # no match
        return_obj = self.x.Intersect_list_item(self.l, self.p, (1,4,'a'), [[1,1,'ksdk'],[2,1,'kldskmcklmd']], self.key_position)
        self.assertEqual(return_obj,{})

        # single item in list 1
        l_l = [[1,3,'fwf']]
        return_obj = self.x.Intersect_list_item(l_l, self.p, (1,4,'a'), [[1,1,'fwf'],[2,1,'kldskmcklmd']], self.key_position)
        self.assertEqual(return_obj,{(1, 4, 'a'): [[[1, 1, 'fwf'], [1, 3, 'fwf']]]})

        # single item in list 2
        return_obj = self.x.Intersect_list_item(self.l, self.p, (1,4,'a'), [[1,1,'kFf']], self.key_position)
        self.assertEqual(return_obj,{(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']]]})

        # empty list1
        l_l = []
        return_obj = self.x.Intersect_list_item(l_l, self.p, (1,4,'a'), [[1,1,'fwf'],[2,1,'kldskmcklmd']], self.key_position)
        self.assertEqual(return_obj,{})

        # empty list2
        return_obj = self.x.Intersect_list_item(self.l, self.p, (1,4,'a'), [], self.key_position)
        self.assertEqual(return_obj,{})

        # empty list2 and no key
        return_obj = self.x.Intersect_list_item(self.l, self.p, (), [], self.key_position)
        self.assertEqual(return_obj,{})

        #no key
        return_obj = self.x.Intersect_list_item(self.l, self.p, (), [[1,1,'kFf'],[2,1,'8834']], self.key_position)
        self.assertEqual(return_obj, {})


        
    def test_Intersect_multi_lists(self):
        return_obj = self.x.Intersect_multi_lists(self.l, self.p, self.y, self.key_position)
        self.assertEqual(return_obj, {(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]], (2, 4, 'b'): [[[2, 2, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]], (3, 4, 'c'): [[[1, 3, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 3, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]]})
        
        # one entry dictionary
        l_dict = {(1,4,'a'): [[1,1,'kFf'],[2,1,'8834']]}
        return_obj = self.x.Intersect_multi_lists(self.l, self.p, l_dict, self.key_position)
        self.assertEqual(return_obj, {(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]]})

        # empty dictionary
        l_dict = {}
        return_obj = self.x.Intersect_multi_lists(self.l, self.p, l_dict, self.key_position)
        self.assertEqual(return_obj, {})

        # no match in one of the items
        l_dict = {(1,4,'a'): [[1,1,'kFf'],[2,1,'8834']],(2,4,'b'):[[1,2,'csdnk'], [2,2,'clkm']],(3,4,'c'):[[1,3,'kFf'], [2,3,'sndsfkmsS']]}
        return_obj = self.x.Intersect_multi_lists(self.l, self.p, l_dict, self.key_position)
        self.assertEqual(return_obj, {(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]], (3, 4, 'c'): [[[1, 3, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 3, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]]})

        # no match at all
        l_dict = {(1,4,'a'): [[1,1,'jknj'],[2,1,'4km4']],(2,4,'b'):[[1,2,'csdnk'], [2,2,'clkm']],(3,4,'c'):[[1,3,'fk54'], [2,3,'dkd8d3']]}
        return_obj = self.x.Intersect_multi_lists(self.l, self.p, l_dict, self.key_position)
        self.assertEqual(return_obj, {})



    def test_Intersect_multi_lists_using_queue(self):
        l_List = Queue()
        l_result = Queue()
        for key in self.y:
            l_List.put({key:self.y[key]})
        self.x.Intersect_multi_lists_using_queue(self.l, self.p, l_List, self.key_position, l_result)
        out_put = {}

        while not l_result.empty():
            l_jk = l_result.get()
            out_put.update(l_jk)  
        print(out_put)
        self.assertEqual(out_put,{(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]], (2, 4, 'b'): [[[2, 2, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]], (3, 4, 'c'): [[[1, 3, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 3, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]]})
        self.assertEqual(out_put[(1,4,'a')],[[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]])
        self.assertEqual(out_put[(2,4,'b')],[[[2, 2, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]])
        self.assertEqual(out_put[(3,4,'c')],[[[1, 3, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 3, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]])

        # single entry dictionary
        l_List1 = Queue()
        l_result1 = Queue()
        l_y =  {(2,4,'b'):[[1,2,'nkrnr'], [2,2,'sndsfkmsS']]}
        for key in l_y:
            l_List1.put({key:l_y[key]})
        self.x.Intersect_multi_lists_using_queue(self.l, self.p, l_List1, self.key_position, l_result1)
        out_put = {}
        while not l_result1.empty():
            out_put.update(l_result1.get())
        self.assertEqual(out_put,{(2, 4, 'b'): [[[2, 2, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]]})

        # empty dictionary
        l_List2 = Queue()
        l_result2 = Queue()
        l_y =  {}
        for key in l_y:
            l_List2.put({key:l_y[key]})
        self.x.Intersect_multi_lists_using_queue(self.l, self.p, l_List2, self.key_position, l_result2)
        out_put = {}  
        while not l_result2.empty():
            print('c')
            out_put.update(l_result2.get_nowait())
        self.assertEqual(out_put,{})

        # empty target document
        l_List3 = Queue()
        l_result3 = Queue()
        l_l = []
        for key in self.y:
            l_List.put({key:self.y[key]})
        self.x.Intersect_multi_lists_using_queue(l_l, self.p, l_List3, self.key_position, l_result3)
        out_put = {}
        while not l_result3.empty():
            out_put.update(l_result3.get_nowait())   
        self.assertEqual(out_put,{})

        # no match in one of the items
        l_List1 = Queue()
        l_result1 = Queue()
        l_l = []
        l_y = {(1,4,'a'): [[1,1,'kFf'],[2,1,'8834']],(2,4,'b'):[[1,2,'csdnk'], [2,2,'clkm']],(3,4,'c'):[[1,3,'kFf'], [2,3,'sndsfkmsS']]}
        for key in l_y:
            l_List1.put({key:l_y[key]})
        self.x.Intersect_multi_lists_using_queue(self.l, self.p, l_List1, self.key_position, l_result1)
        out_put = {}
        while not l_result1.empty():
            out_put.update(l_result1.get())
        self.assertEqual(out_put, {(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]], (3, 4, 'c'): [[[1, 3, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 3, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]]})

        # no match at all
        l_List1 = Queue()
        l_result1 = Queue()
        l_l = []
        l_y = {(1,4,'a'): [[1,1,'jknj'],[2,1,'4km4']],(2,4,'b'):[[1,2,'csdnk'], [2,2,'clkm']],(3,4,'c'):[[1,3,'fk54'], [2,3,'dkd8d3']]}
        for key in l_y:
            l_List1.put({key:l_y[key]})
        self.x.Intersect_multi_lists_using_queue(self.l, self.p, l_List1, self.key_position, l_result1)
        out_put = {}
        while not l_result1.empty():
            out_put.update(l_result1.get())
        self.assertEqual(out_put, {})




    def test_Intersect_multi_lists_using_MultiProcessing(self):
        out_put = self.x.Intersect_multi_lists_using_MultiProcessing(self.l, self.p, self.y, self.key_position) 
        self.assertEqual(out_put,{(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]], (2, 4, 'b'): [[[2, 2, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]], (3, 4, 'c'): [[[1, 3, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 3, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]]})
        self.assertEqual(out_put[(1,4,'a')],[[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]])
        self.assertEqual(out_put[(2,4,'b')],[[[2, 2, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]])
        self.assertEqual(out_put[(3,4,'c')],[[[1, 3, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 3, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]])

        # single entry dictionary
        l_y =  {(2,4,'b'):[[1,2,'nkrnr'], [2,2,'sndsfkmsS']]}
        out_put =self.x.Intersect_multi_lists_using_MultiProcessing(self.l, self.p, l_y, self.key_position)
        self.assertEqual(out_put,{(2, 4, 'b'): [[[2, 2, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]]})

        # empty dictionary
        l_y =  {}
        out_put =self.x.Intersect_multi_lists_using_MultiProcessing(self.l, self.p, l_y, self.key_position)
        self.assertEqual(out_put,{})

        # empty target document
        l_l = []
        out_put = self.x.Intersect_multi_lists_using_MultiProcessing(l_l, self.p, self.y, self.key_position)
        self.assertEqual(out_put,{})

        # no match in one of the items
        l_y = {(1,4,'a'): [[1,1,'kFf'],[2,1,'8834']],(2,4,'b'):[[1,2,'csdnk'], [2,2,'clkm']],(3,4,'c'):[[1,3,'kFf'], [2,3,'sndsfkmsS']]}
        out_put = self.x.Intersect_multi_lists_using_MultiProcessing(self.l, self.p, l_y, self.key_position)
        self.assertEqual(out_put, {(1, 4, 'a'): [[[1, 1, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 1, '8834'], [9, 3, '8834'], [12, 3, '8834']]], (3, 4, 'c'): [[[1, 3, 'kFf'], [4, 3, 'kFf'], [7, 3, 'kFf'], [11, 3, 'kFf']], [[2, 3, 'sndsfkmsS'], [5, 3, 'sndsfkmsS']]]})

        # no match at all
        l_y = {(1,4,'a'): [[1,1,'jknj'],[2,1,'4km4']],(2,4,'b'):[[1,2,'csdnk'], [2,2,'clkm']],(3,4,'c'):[[1,3,'fk54'], [2,3,'dkd8d3']]}
        out_put = self.x.Intersect_multi_lists_using_MultiProcessing(self.l, self.p, l_y, self.key_position)
        self.assertEqual(out_put, {})


if __name__ == '__main__':
    # xjd = testINtersectLists()
    # xjd.test_Intersect_multi_lists_using_queue()
    unittest.main()