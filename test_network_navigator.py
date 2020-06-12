import unittest
from Expression.network_navigator import Network_Navigtor
from PDF_OCR_Reader.PDF_information import PDF_Information
import z_test_data
import copy


class testNetworkNavigator(unittest.TestCase):
    def setUp(self):
        self.PDF_Info = PDF_Information()
        self.PDF_Info = z_test_data.PDF_Info
        self.x = Network_Navigtor()

    

    def test_is_same(self):
        PDF_Info= PDF_Information()

        term1 = [5, 1, 13, 1, 3, 8, 2864, 104712, 282, 53, 96, '$60,000.00']
        term2 = [5, 1, 13, 1, 3, 8, 2864, 104712, 282, 53, 96, '$60,000.00']
        out_put =  self.x.is_same(term1, term2, PDF_Info.get_indexes_with_pixel_info)
        self.assertTrue(out_put)
        # same pixel different text
        term1 = [5, 1, 13, 1, 3, 8, 2864, 104712, 282, 53, 96, '$60,000.00']
        term2 = [5, 1, 13, 1, 3, 8, 2864, 104712, 282, 53, 96, '$.00']
        out_put =  self.x.is_same(term1, term2, PDF_Info.get_indexes_with_pixel_info)
        self.assertTrue(out_put)
        # not equal
        term1 = [5, 1, 13, 1, 3, 8, 93, 104712, 282, 53, 96, '$60,000.00']
        term2 = [5, 1, 13, 1, 3, 8, 2864, 104712, 282, 53, 96, '$60,000.00']
        out_put =  self.x.is_same(term1, term2, PDF_Info.get_indexes_with_pixel_info)
        self.assertFalse(out_put)
        # term1 blank
        term1 = []
        term2 = [5, 1, 13, 1, 3, 8, 2864, 104712, 282, 53, 96, '$60,000.00']
        out_put =  self.x.is_same(term1, term2, PDF_Info.get_indexes_with_pixel_info)
        self.assertFalse(out_put)
        # term2 blank
        term1 = [5, 1, 13, 1, 3, 8, 93, 104712, 282, 53, 96, '$60,000.00']
        term2 = []
        out_put =  self.x.is_same(term1, term2, PDF_Info.get_indexes_with_pixel_info)
        self.assertFalse(out_put)
        # both term blank
        term1 = []
        term2 = []
        out_put =  self.x.is_same(term1, term2, PDF_Info.get_indexes_with_pixel_info)
        self.assertTrue(out_put)

    def test_get_alignment_term(self):
       

        l_term = [5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0]
        l_list = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1]]
        out_put = self.x.get_alignment_term(self.PDF_Info, l_term, l_list)
        # print(out_put)
        self.assertEqual(out_put, [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)], [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 785)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)], [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)]]]])

        # single term in list
        l_term = [5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0]
        l_list = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0]]
        out_put = self.x.get_alignment_term(self.PDF_Info, l_term, l_list)
        self.assertEqual(out_put, [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]]])

        # empty list
        l_term = [5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0]
        l_list = []
        out_put = self.x.get_alignment_term(self.PDF_Info, l_term, l_list)
        self.assertEqual(out_put, [])

        # one term align
        l_term = [5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0]
        l_list = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 14838842, 973, 94, 62, 95, '20', 0], [5, 1, 4, 1, 1, 5, 1442, 97473, 94, 62, 95, ',', 1]]
        out_put = self.x.get_alignment_term(self.PDF_Info, l_term, l_list)
        self.assertEqual(out_put, [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]]])
        # no align
        l_term = [5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0]
        l_list = [[5, 1, 4, 1, 1, 4, 1134, 837830, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 14838842, 762, 94, 62, 95, '20', 0], [5, 1, 4, 1, 1, 5, 1442, 97473, 94, 62, 95, ',', 1]]
        out_put = self.x.get_alignment_term(self.PDF_Info, l_term, l_list)
        self.assertEqual(out_put, [])
        

    def test_get_alignment_list(self):
        l_list1 = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0]]
        l_list2 = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1]]
        out_put = self.x.get_alignment_list(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(out_put,[[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 785)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]]]], [[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 375)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 27)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 27)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 683)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 27)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 27)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 683)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 27)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 27)]]]]]])
        # single entry in list1
        l_list1 = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0]]
        l_list2 = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1]]
        out_put = self.x.get_alignment_list(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(out_put, [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 785)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]]]]])
        # empty list1
        l_list1 = []
        l_list2 = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1]]
        out_put = self.x.get_alignment_list(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(out_put,[])
        # no match
        l_list1 = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0]]
        l_list2 = [[5, 1, 16, 1, 5, 4, 1957, 4628, 243, 62, 91, 'February', 0], [5, 1, 16, 1, 5, 5, 2219, 4629, 79, 57, 86, '29', 0]]
        out_put = self.x.get_alignment_list(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(out_put,[])
        # single match
        l_list1 = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0]]
        l_list2 = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 74, 973, 94, 62, 95, '20', 0], [5, 1, 4, 1, 1, 5, 73, 973, 94, 62, 95, ',', 1]]
        out_put = self.x.get_alignment_list(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(out_put, [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]]]], [[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 375)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 27)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 27)]]]]]])
        

    def test_get_direction(self):
        l_alignment_list = [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 785)], [[5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, '2020', 0], ('right', 907)]]], [[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 375)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 683)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 683)], [[5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, '2020', 0], ('right', 805)]]]]
        out_put = self.x.get_direction(l_alignment_list, self.PDF_Info.get_direction)
        self.assertEqual(out_put, {'right': 8, 'down': 0, 'equal': 0})
        # single entry
        l_alignment_list = [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('up', 477)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 785)], [[5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, '2020', 0], ('right', 907)]]]]
        out_put = self.x.get_direction(l_alignment_list, self.PDF_Info.get_direction)
        self.assertEqual(out_put, {'right': 3, 'down': 0, 'equal': 0})
        # no match
        l_alignment_list = [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('up', 477)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('up', 785)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('left', 785)], [[5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, '2020', 0], ('up', 907)]]]]
        out_put = self.x.get_direction(l_alignment_list, self.PDF_Info.get_direction)
        self.assertEqual(out_put, {'right': 0, 'down': 0, 'equal': 0})
        # single entry no match
        l_alignment_list = [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('up', 477)]]]]
        out_put = self.x.get_direction(l_alignment_list, self.PDF_Info.get_direction)
        self.assertEqual(out_put, {'right': 0, 'down': 0, 'equal': 0})

        l_alignment_list = [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)]]]]
        out_put = self.x.get_direction(l_alignment_list, self.PDF_Info.get_direction)
        self.assertEqual(out_put, {'right': 1, 'down': 0, 'equal': 0})
        # empty
        l_alignment_list = [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], []]]
        out_put = self.x.get_direction(l_alignment_list, self.PDF_Info.get_direction)
        self.assertEqual(out_put, {'right': 0, 'down': 0, 'equal': 0})
        out_put = self.x.get_direction(l_alignment_list, self.PDF_Info.get_direction)

    def test_get_distance(self):
        PDF_Info = PDF_Information()
        l_alignment_list = [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 785)], [[5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, '2020', 0], ('right', 907)]]], [[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 375)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 683)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 683)], [[5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, '2020', 0], ('right', 805)]]]]
        out_put = self.x.get_distance(l_alignment_list, PDF_Info.get_distance)
        self.assertEqual(out_put,{'min': 375, 'max': 907})

        # empty
        l_alignment_list = []
        out_put = self.x.get_distance(l_alignment_list, PDF_Info.get_distance)
        self.assertEqual(out_put,{'min': -1, 'max': -1})

        # two max at same distance
        l_alignment_list = [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 785)], [[5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, '2020', 0], ('right', 907)]]], [[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], [[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 375)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 683)], [[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], ('right', 907)], [[5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, '2020', 0], ('right', 805)]]]]
        out_put = self.x.get_distance(l_alignment_list, PDF_Info.get_distance)
        self.assertEqual(out_put,{'min': 375, 'max': 907})
        

    def test_align(self):
        l_list1 = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0]]
        l_list2 = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0]]
        self.x.align(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(self.x.alignment_list, [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]]]], [[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 375)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 27)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 27)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 683)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 27)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 27)]]]]]])

        # no align
        l_list1 = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0]]
        l_list2 = [[5, 1, 4, 1, 1, 4, 1134, 9173, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 21, 94, 62, 95, '20', 0]]
        self.x.align(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(self.x.alignment_list, [])
        
        # one term align
        l_list1 = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 6, 1, 1, 3, 714, 101233, 149, 49, 95, 'supply', 0]]
        l_list2 = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 9743, 94, 62, 95, '20', 0]]
        self.x.align(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(self.x.alignment_list, [[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]]]]])
        
        # empty list1
        l_list1 = []
        l_list2 = [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0]]
        self.x.align(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(self.x.alignment_list, [])

        # empty list2
        l_list1 = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0]]
        l_list2 = []
        self.x.align(self.PDF_Info, l_list1, l_list2)
        self.assertEqual(self.x.alignment_list, [])
       

    
    def test_remove_aligning_terms(self):
        p_list = [[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]], [[[5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], ('right', 785)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)], [[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)]]]]

        p_aligning_term = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], [5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, '20', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], [5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, '2020', 0]]
        out_put = self.x.remove_aligning_terms(copy.deepcopy(p_list), p_aligning_term)       
        self.assertEqual(out_put[0],[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]])
        
        # no match
        p_aligning_term = [[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'k', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'mk', 0], [5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'kk', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, 'kl', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], [5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, 'lkm', 0]]
        out_put = self.x.remove_aligning_terms(copy.deepcopy(p_list), p_aligning_term)
        self.assertEqual(out_put[0],[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('right', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)]]])

        # all match
        p_aligning_term = [[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], [5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], [5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, 'kl', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], [5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, 'lkm', 0]]
        out_put = self.x.remove_aligning_terms(copy.deepcopy(p_list), p_aligning_term)
        self.assertEqual(out_put[0],[[[5, 1, 4, 1, 1, 4, 1134, 973, 286, 67, 95, 'February', 0], ('right', 477)], []])

        # empty list
        p_aligning_term = [[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], [5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], [5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, 'kl', 0], [5, 1, 4, 1, 1, 5, 1442, 973, 94, 62, 95, ',', 1], [5, 1, 4, 1, 1, 6, 1564, 973, 157, 53, 95, 'lkm', 0]]
        out_put = self.x.remove_aligning_terms([], p_aligning_term)
        self.assertEqual(out_put,[])


    def test_clean_data(self):
        p_data = [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('down', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('down', 129)]]
        out_put = self.x.clean_data(p_data, self.PDF_Info.get_direction, 'right')
        self.assertEqual(out_put, [[[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)]])
       
        # empty
        p_data = []
        out_put = self.x.clean_data(p_data, self.PDF_Info.get_direction, 'right')
        self.assertEqual(out_put, [])
        
        # no direction match
        p_data = [[[5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0], ('down', 28)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, 'thursday', 0], ('right', 129)], [[5, 1, 4, 1, 1, 3, 786, 973, 316, 67, 95, ',', 1], ('down', 129)]]
        out_put = self.x.clean_data(p_data, self.PDF_Info.get_direction, 'up')
        self.assertEqual(out_put, [])
        



if __name__ == "__main__":
    # TNN = testNetworkNavigator()
    # TNN.setUp()
    # TNN.test_remove_aligning_terms()
    unittest.main()


