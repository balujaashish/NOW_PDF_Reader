import unittest

from term_proximity import Term_Proximity

class testTermProximity(unittest.TestCase):

    def setUp(self):
        self.x = Term_Proximity()
        self.p_aligned_term = [[[1,1,1],('r',4)],
        [[1,1,2],('d',13)],
        [[1,1,3],('r',13)],
        [[1,1,4],('r',65)]]

        self.p_aligned_term1 = [[[1,1,1],('right',4)],
        [[1,1,2],('down',13)],
        [[1,1,3],('right',13)],
        [[1,1,4],('right',65)]]

        self.p_aligned_term2 = [[[1,1,1],('equal',0)],
        [[10,10,2],('equal',0)],
        [[10,10,4],('equal',0)],
        [[1,1,2],('down',13)],
        [[1,1,3],('right',13)],
        [[1,1,4],('right',65)]]

    def p_get_direction(self, e):
        return e[1][0]

    def get_distance(self, e):
        return e[1][1]

    def p_get_order_term(self, e):
        return e[2]

    def p_get_order_value(self, e):
        return e[0][2]



    def test_get_first_term_in_direction(self):
        p_term = ()
        p_distance = 50
        self.assertEqual(self.x.get_first_term_in_direction(self.p_aligned_term, self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, 'd', p_distance),[[[1, 1, 2], ('d', 13)]])
        self.assertEqual(self.x.get_first_term_in_direction(self.p_aligned_term, self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, 'r', p_distance), [[[1, 1, 1], ('r', 4)]] )
        self.assertEqual(self.x.get_first_term_in_direction(self.p_aligned_term, self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, 'j', p_distance), [] )
        self.assertEqual(self.x.get_first_term_in_direction([], self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, 'r', p_distance), [] )

        p_term = (3,4,0)
        self.assertEqual(self.x.get_first_term_in_direction(self.p_aligned_term2, self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, 'equal', p_distance), [[1, 1, 1], ('equal', 0)])

        p_term = (3,4,3)
        self.assertEqual(self.x.get_first_term_in_direction(self.p_aligned_term2, self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, 'equal', p_distance), [[10,10,4],('equal',0)])


    def test_get_next_term_in_direction(self):
        out_put = self.x.get_next_term_in_direction(self.p_aligned_term, [[1,1,1],('r',4)], self.p_get_direction)
        self.assertEqual(out_put, [[1, 1, 3], ('r', 13)])
        out_put = self.x.get_next_term_in_direction(self.p_aligned_term, [[1,1,2],('d',13)], self.p_get_direction)
        self.assertEqual(out_put, [])
        out_put = self.x.get_next_term_in_direction([], [[1,1,2],('d',13)], self.p_get_direction)
        self.assertEqual(out_put, [])
        out_put = self.x.get_next_term_in_direction(self.p_aligned_term, [[1,1,3],('r',13)], self.p_get_direction)
        self.assertEqual(out_put, [[1, 1, 4], ('r', 65)])
        out_put = self.x.get_next_term_in_direction(self.p_aligned_term, [[1,1,4],('r',65)], self.p_get_direction)
        self.assertEqual(out_put, [])

    def test_get_all_terms_in_proximity(self):
        p_term = (3,4,0) 
        p_distance = 50
        out_put = self.x.get_all_terms_in_proximity(self.p_aligned_term1, self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, p_distance)
        self.assertEqual(out_put, [[[1, 1, 1], ('right', 4)], [[1, 1, 2], ('down', 13)]])

        p_aligned_term2 = []
        out_put = self.x.get_all_terms_in_proximity(p_aligned_term2, self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, p_distance)
        self.assertEqual(out_put, [])

        p_aligned_term3 = [[[1,1,1],('right',4)],
        [[1,1,3],('right',13)],
        [[1,1,4],('right',65)]]
        out_put = self.x.get_all_terms_in_proximity(p_aligned_term3, self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, p_distance)
        self.assertEqual(out_put, [[[1,1,1],('right',4)]])

        p_term = (3,4,0) 
        out_put = self.x.get_all_terms_in_proximity(self.p_aligned_term2, self.p_get_direction, self.get_distance, self.p_get_order_term, self.p_get_order_value, p_term, p_distance)
        # print(out_put)
        self.assertEqual(out_put, [[[1, 1, 1], ('equal', 0)], [[1, 1, 3], ('right', 13)], [[1, 1, 2], ('down', 13)]])

    def test_get_first_term_equal(self):
        p_term = (1,2,0)
        out_put = self.x.get_first_term_equal(self.p_aligned_term2, self.p_get_order_term, self.p_get_order_value, self.p_get_direction, p_term)
        self.assertEqual(out_put, [[1, 1, 1], ('equal', 0)])

        p_term = (1,1,3)
        out_put = self.x.get_first_term_equal(self.p_aligned_term2, self.p_get_order_term, self.p_get_order_value, self.p_get_direction, p_term)
        self.assertEqual(out_put, [[10, 10, 4], ('equal', 0)])

        p_term = (1,2,0)
        out_put = self.x.get_first_term_equal(self.p_aligned_term1, self.p_get_order_term, self.p_get_order_value, self.p_get_direction, p_term)
        self.assertEqual(out_put, [])

        # print(out_put)


if __name__ == "__main__":
    unittest.main()