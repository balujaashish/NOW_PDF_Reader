import unittest
from token_network import Token_Network

class testTokenNetwork(unittest.TestCase):

    def setUp(self):
        self.x = Token_Network()
        self.l = [[1, 256, 284, 410, 76, 95, 'Purchase'],
        [2, 698, 283, 271, 77, 91, 'Order:'],
        [3, 1001, 284, 558, 76, 88, 'AE10071871'],
        [2, 376, 558, 234, 53, 95, 'purchase']]


    def get_key1(self,e):
        return e[2]

    def get_key2(self,e):
        return e[4]

    def get_top(self,e):
        return e[2]

    def get_left(self,e):
        return e[1]

    def get_height(self,e):
        return e[4]

    def get_width(self,e):
        return e[3]
    
    def get_term(self, e):
        return e[11]

    def get_distance_key(self, e):
        return e[1][1]

    # ----------

    def get_top1(self,e):
        return e[7]

    def get_left1(self,e):
        return e[6]

    def get_height1(self,e):
        return e[9]

    def get_width1(self,e):
        return e[8]
    
    def get_term1(self, e):
        return e[11]
    
    def get_term2(self, e):
        return e[1]

    # ----------

    def test_is_align_coordinates(self):
        self.assertTrue(self.x.is_align_coordinates(4,5,8,5))
        self.assertFalse(self.x.is_align_coordinates(4,5,10,5))
        self.assertFalse(self.x.is_align_coordinates(4,5,-1,-1))

    def test_is_align_1D(self):
        t1 = [1,2,4,6,5,7]
        t2 = [53,321,8,919,5,8943]
        self.assertTrue(self.x.is_align_1D(t1, t2, self.get_key1, self.get_key2))
        t1 = [1,2,4,6,5,7]
        t2 = [53,321,10,919,5,8943]
        self.assertFalse(self.x.is_align_1D(t1, t2, self.get_key1, self.get_key2))

    def test_get_vertical_align_direction(self):
        l = [[1, 256, 284, 410, 76, 95, 'Purchase'],
        [2, 698, 283, 271, 77, 91, 'Order:'],
        [3, 1001, 284, 558, 76, 88, 'AE10071871'],
        [2, 376, 558, 234, 53, 95, 'purchase']]

        left_i, top_i, width_i, height_i = 2, 3, 4, 5

        out_put = self.x.get_vertical_align_direction(l[0], l[3], self.get_top, self.get_height)
        self.assertEqual(out_put, ('down', 198))

        out_put = self.x.get_vertical_align_direction(l[3], l[0], self.get_top, self.get_height)
        self.assertEqual(out_put, ('up', 198))

        out_put = self.x.get_vertical_align_direction(l[0], l[0], self.get_top, self.get_height)
        self.assertEqual(out_put, ('equal', 0))

    def test_get_horizontal_align_direction(self):
        l = [[1, 256, 284, 410, 76, 95, 'Purchase'],
        [2, 698, 283, 271, 77, 91, 'Order:'],
        [3, 1001, 284, 558, 76, 88, 'AE10071871'],
        [2, 376, 558, 234, 53, 95, 'purchase']]

        # left_i, top_i, width_i, height_i = 2, 3, 4, 5

        out_put = self.x.get_horizontal_align_direction(l[0], l[1], self.get_left, self.get_width)
        self.assertEqual(out_put, ('right', 32))

        out_put = self.x.get_horizontal_align_direction(l[1], l[0], self.get_left, self.get_width)
        self.assertEqual(out_put, ('left', 32))

        out_put = self.x.get_horizontal_align_direction(l[0], l[0], self.get_left, self.get_width)
        self.assertEqual(out_put, ('equal', 0))

    def test_is_aligned_2d(self):

        # horizontally align right
        out_put = self.x.is_aligned_2d(self.l[0], self.l[1], self.get_left, self.get_top, self.get_width, self.get_height)
        self.assertEqual(out_put, ('right', 32))

        # vertically align down
        out_put = self.x.is_aligned_2d(self.l[0], self.l[3], self.get_left, self.get_top, self.get_width, self.get_height)
        self.assertEqual(out_put, ('down', 198))

        # horizontally align left
        out_put = self.x.is_aligned_2d(self.l[1], self.l[0], self.get_left, self.get_top, self.get_width, self.get_height)
        self.assertEqual(out_put, ('left', 32))

        # vertically align up
        out_put = self.x.is_aligned_2d(self.l[3], self.l[0], self.get_left, self.get_top, self.get_width, self.get_height)
        self.assertEqual(out_put, ('up', 198))
        # not aligned
        out_put = self.x.is_aligned_2d(self.l[3], self.l[2], self.get_left, self.get_top, self.get_width, self.get_height)
        self.assertEqual(out_put, None)
        out_put = self.x.is_aligned_2d(self.l[2], self.l[3], self.get_left, self.get_top, self.get_width, self.get_height)
        self.assertEqual(out_put, None)

    

    def test_sort_by_distance(self):
        l2 = {'x': [[[1, 256, 284, 410, 76, 95, 'Purchase'],('right', 10)],
        [[2, 698, 283, 271, 77, 91, 'Order:'], ('down', 34)],
        [[3, 1001, 284, 558, 76, 88, 'AE10071871'], ('right', 4)],
        [[2, 376, 558, 234, 53, 95, 'purchase'], ('down',13)]], 
        'y': [[[1, 256, 284, 410, 76, 95, 'Purchase'],('right', 10)],
        [[2, 698, 283, 271, 77, 91, 'Order:'], ('down', 34)],
        [[3, 1001, 284, 558, 76, 88, 'AE10071871'], ('right', 4)],
        [[2, 376, 558, 234, 53, 95, 'purchase'], ('down',13)]]}

        x = self.x.sort_by_distance(l2, self.get_distance_key)
        self.assertEqual(x['x'],[[[3, 1001, 284, 558, 76, 88, 'AE10071871'], ('right', 4)], [[1, 256, 284, 410, 76, 95, 'Purchase'], ('right', 10)], [[2, 376, 558, 234, 53, 95, 'purchase'], ('down', 13)], [[2, 698, 283, 271, 77, 91, 'Order:'], ('down', 34)]])

        l = {'x':[[1, 256, 284, 410, 76, 95, 'Purchase'],
        [2, 698, 283, 271, 77, 91, 'Order:'],
        [3, 1001, 284, 558, 76, 88, 'AE10071871'],
        [2, 376, 558, 234, 53, 95, 'purchase']]}
        x = self.x.sort_by_distance(l, self.get_left)
        self.assertEqual(x['x'], [[1, 256, 284, 410, 76, 95, 'Purchase'], [2, 376, 558, 234, 53, 95, 'purchase'], [2, 698, 283, 271, 77, 91, 'Order:'], [3, 1001, 284, 558, 76, 88, 'AE10071871']])
        

    def test_get_aligned_terms(self):
        out_put = self.x.get_aligned_terms(self.l,self.get_top, self.get_left, self.get_width, self.get_height)
        self.assertEqual(out_put[(1, 256, 284, 410, 76, 95, 'Purchase')],[[[2, 698, 283, 271, 77, 91, 'Order:'], ('right', 32)], [[3, 1001, 284, 558, 76, 88, 'AE10071871'], ('right', 335)], [[2, 376,
        558, 234, 53, 95, 'purchase'], ('down', 198)]])
        l = []
        out_put = self.x.get_aligned_terms(l,self.get_top, self.get_left, self.get_width, self.get_height)
        self.assertEqual(out_put,{})


    def test_get_neighbor_map(self):
        l = [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase'],
        [5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'Order:'],
        [5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871'],
        [5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This'],
        [5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase']]
        indexes = [0,1,2,3,4,5,6,7,8,9,10]
        out_put = self.x.get_neighbor_map( l, indexes, self.get_top1, self.get_left1, self.get_width1, self.get_height1, self.get_term1)
        print(out_put)
        # print(out_put[(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase')])
        self.assertEqual(out_put[(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase')],[[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'Order:'], ('right', 32)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This'], ('down', 198)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase'], ('down', 198)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871'], ('right', 335)]])
        l = []
        out_put = self.x.get_neighbor_map( l, indexes, self.get_top1, self.get_left1, self.get_width1, self.get_height1, self.get_term1)
        self.assertEqual(out_put,{})

    def test_search_nh_map(self):
        p_data = {(1,'x'):[1,1], (2,'y'):[1,2], (3,'u'):[1,3], (4,'z'):[1,4]}
        out_put = self.x.search_neighbor_map(p_data, 'y', self.get_term2)
        self.assertEqual(out_put, {(2, 'y'): [1, 2]})
        # empty dictionary
        p_data = {}
        out_put = self.x.search_neighbor_map(p_data, 'y', self.get_term2)
        self.assertEqual(out_put, {})
        # first term
        p_data = {(1,'x'):[1,1], (2,'y'):[1,2], (3,'u'):[1,3], (4,'z'):[1,4]}
        out_put = self.x.search_neighbor_map(p_data, 'x', self.get_term2)
        self.assertEqual(out_put, {(1,'x'):[1,1]})
        # last term
        out_put = self.x.search_neighbor_map(p_data, 'z', self.get_term2)
        self.assertEqual(out_put, {(4,'z'):[1,4]})
        # no match
        out_put = self.x.search_neighbor_map(p_data, 'g', self.get_term2)
        self.assertEqual(out_put, {})



if __name__ == "__main__":
    unittest.main()


