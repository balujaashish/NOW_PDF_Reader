import unittest
from PDF_OCR_Reader.extract_currency_frm_pdf import Extract_Currency_Frm_PDF
from PDF_OCR_Reader.PDF_information import PDF_Information
from PDF_OCR_Reader.prepare_data_pdf import Prepare_Data_PDF

class TestExtractCurrencyFrmPDF(unittest.TestCase):

    def setUp(self):
        self.x = Extract_Currency_Frm_PDF()

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


    def test_is_ammount(self):
        out_put = self.x.is_ammount('100')
        self.assertTrue(out_put)
        # not digit
        out_put = self.x.is_ammount('1kdkd00')
        self.assertFalse(out_put)
        # decimal
        out_put = self.x.is_ammount('10.0')
        self.assertTrue(out_put)
        # comma
        out_put = self.x.is_ammount('10,000')
        self.assertTrue(out_put)
        # blank
        out_put = self.x.is_ammount('')
        self.assertFalse(out_put)
        # only decimal
        out_put = self.x.is_ammount('.')
        self.assertFalse(out_put)


    def test_get_term_in_proximity(self):
        PDF_Info = PDF_Information()
        
        PDF_Info.network = {(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('down', 198)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('down', 198)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1): [[[5, 1,
        1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('left', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('left', 32)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 335)]], (5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0): [[[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('right', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0): [[[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('left', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 1, 1, 1, 1, 256, 284, 4101, 76, 95, 'Purchase', 0):[]}  
        p_distance = 200
        l_key = (5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0)
        out_put = self.x.get_term_in_proximity(PDF_Info, l_key, p_distance)
        self.assertEqual(out_put, [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)]])

        # key doesnt match
        l_key = (5, 1, 1, 1, 1, 1, 256, 284, 4100, 76, 95, 'Purchase', 0)
        out_put = self.x.get_term_in_proximity(PDF_Info, l_key, p_distance)
        self.assertEqual(out_put, [])
        # key has empty value 
        l_key = (5, 1, 1, 1, 1, 1, 256, 284, 4101, 76, 95, 'Purchase', 0)
        out_put = self.x.get_term_in_proximity(PDF_Info, l_key, p_distance)
        self.assertEqual(out_put, [])        



    def test_get_amount_in_proximity(self):
        PDF_Info = PDF_Information()
        
        PDF_Info.network = {(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'USD', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, '10,000', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('down', 198)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('down', 198)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1): [[[5, 1,
        1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('left', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('left', 32)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 335)]], (5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0): [[[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('right', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0): [[[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('left', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 1, 1, 1, 1, 256, 284, 4101, 76, 95, 'Purchase', 0):[], (5, 1, 1, 1, 1, 1, 256, 284, 41010, 76, 95, '$', 0):[]}  
        p_distance = 200
        l_key = (5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'USD', 0)
        PDF_Info.RawCurrency = [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, '10,000', 0],[None,10000,'10,000']]]
        out_put = self.x.get_amount_in_proximity(PDF_Info, l_key, p_distance)
        self.assertEqual(out_put , [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, '10,000', 0], [None, 10000, '10,000']])

        # no match in rawCurrency
        PDF_Info1 = PDF_Information()
        PDF_Info1.RawCurrency = [[[5, 1, 1, 1, 1, 2, 698, 2834, 271, 77, 91, '100,000', 0],[None,10000,'10,000']]]
        out_put = self.x.get_amount_in_proximity(PDF_Info1, l_key, p_distance)
        self.assertEqual(out_put , [])
        # nothing on right
        l_key = (5, 1, 1, 1, 1, 1, 256, 284, 41010, 76, 95, '$', 0)
        PDF_Info.RawCurrency = [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, '10,000', 0],[None,10000,'10,000']]]
        out_put = self.x.get_amount_in_proximity(PDF_Info, l_key, p_distance)
        self.assertEqual(out_put , [])
        # nothing in proximity
        PDF_Info.network = {(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'USD', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, '10,000', 0], ('right', 332)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 332)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('down', 398)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('down', 398)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1): [[[5, 1,
        1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('left', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('left', 32)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 335)]], (5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0): [[[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('right', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0): [[[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('left', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 1, 1, 1, 1, 256, 284, 4101, 76, 95, 'Purchase', 0):[], (5, 1, 1, 1, 1, 1, 256, 284, 41010, 76, 95, '$', 0):[]}  
        p_distance = 200
        l_key = (5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'USD', 0)
        PDF_Info.RawCurrency = [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, '10,000', 0],[None,10000,'10,000']]]
        out_put = self.x.get_amount_in_proximity(PDF_Info, l_key, p_distance)
        self.assertEqual(out_put , [])

    
    def test_get_currency_in_proximity(self):
        PDF_Info = PDF_Information()
        
        PDF_Info.network = {(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, '10,000', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'USD', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('down', 198)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('down', 198)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1): [[[5, 1,
        1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('left', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('left', 32)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 335)]], (5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0): [[[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('right', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0): [[[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('left', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 1, 1, 1, 1, 256, 284, 4101, 76, 95, 'Purchase', 0):[], (5, 1, 1, 1, 1, 1, 256, 284, 41010, 76, 95, '10,000', 0):[]}  
        p_distance = 200
        l_key = (5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, '10,000', 0)
        PDF_Info.RawCurrency = [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'USD', 0],['USD',None,None]]]
        out_put = self.x.get_currency_in_proximity(PDF_Info, l_key, p_distance)
        self.assertEqual(out_put , [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'USD', 0], ['USD', None, None]])

        # no match in rawCurrency
        PDF_Info1 = PDF_Information()
        PDF_Info1.RawCurrency = [[[5, 1, 1, 1, 1, 2, 698, 2834, 271, 77, 91, '100,000', 0],[None,10000,'10,000']]]
        out_put = self.x.get_currency_in_proximity(PDF_Info1, l_key, p_distance)
        self.assertEqual(out_put , [])
        # nothing on right
        l_key = (5, 1, 1, 1, 1, 1, 256, 284, 41010, 76, 95, '10,000', 0)
        PDF_Info.RawCurrency = [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, '10,000', 0],[None,10000,'10,000']]]
        out_put = self.x.get_currency_in_proximity(PDF_Info, l_key, p_distance)
        self.assertEqual(out_put , [])
        # nothing in proximity
        PDF_Info.network = {(5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, '10,000', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, '10,000', 0], ('right', 332)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 332)], [[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('down', 398)], [[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('down', 398)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1): [[[5, 1,
        1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('equal', 0)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 32)]], (5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0): [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('left', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('left', 32)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('left', 335)]], (5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0): [[[5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0], ('right', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 2, 1, 1, 2, 376, 558, 234, 53, 95, 'purchase', 0): [[[5, 1, 2, 1, 1, 1, 259, 558, 100, 42, 96, 'This', 0], ('left', 17)], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], ('up', 198)]], (5, 1, 1, 1, 1, 1, 256, 284, 4101, 76, 95, 'Purchase', 0):[], (5, 1, 1, 1, 1, 1, 256, 284, 41010, 76, 95, '$', 0):[]}  
        p_distance = 200
        l_key = (5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, '10,000', 0)
        PDF_Info.RawCurrency = [[[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, '10,000', 0],[None,10000,'10,000']]]
        out_put = self.x.get_currency_in_proximity(PDF_Info, l_key, p_distance)
        self.assertEqual(out_put , [])


    def test_search_currency_in_pdf(self):
        PDF_Info = PDF_Information()
        PDF_Info.cleanData = [[5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, '95014'], [5, 1, 5, 4, 1, 8, 3653, 1515, 321, 42, 88, 'AE10071871'], [5, 1, 5, 5, 1, 1, 275, 1624, 132, 42, 94, 'Israel'], [5, 1, 5, 5, 1, 2, 2129, 1608, 157, 42, 95, 'United'], [5, 1, 5, 5, 1, 3, 2309, 1607, 157, 43, 96, 'States'], [5, 1, 5, 5, 1, 4, 3331, 1602, 208, 42, 95, 'Amount:'], [5,
        1, 5, 5, 1, 5, 3562, 1598, 282, 53, 95, '$60,000.00'], [5, 1, 5, 5, 1, 6, 3867, 1601, 114, 43, 94, 'USD'], [5, 1, 5, 5, 2, 1, 2129, 1689, 172, 42, 95, 'Phone:'], [5, 1, 5, 5, 2, 2, 2325, 1689, 52, 41, 95, '+1'], [5, 1, 5, 5, 2, 3, 2406, 1688, 128, 54, 95, '(650)'], [5, 1, 5, 5, 2, 4, 2555, 1689, 219, 42, 95, '6186116'], [5, 1, 5, 5, 2, 5, 3726, 1683, 205, 42, 96, 'Version:'], [5, 1, 5, 5, 2, 6, 3958, 1683, 16, 41, 96, '1'], [5, 1, 5, 5, 3, 1, 2129, 1770, 102, 42, 93, 'Fax:']]
        self.x.search_currency_in_pdf(PDF_Info)

        self.assertEqual(PDF_Info.RawCurrency, [[[5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, '95014'], [None, 95014, '95014']], [[5, 1, 5, 4, 1, 8, 3653, 1515, 321, 42, 88, 'AE10071871'], [None, 10071871, '10071871']], [[5, 1, 5, 5, 1, 5, 3562, 1598, 282, 53, 95, '$60,000.00'], ['$', 60000.00, '60,000.00']], [[5, 1, 5, 5, 1, 6, 3867, 1601, 114, 43, 94, 'USD'], ['USD', None, None]], [[5,
        1, 5, 5, 2, 2, 2325, 1689, 52, 41, 95, '+1'], [None, 1, '1']], [[5, 1, 5, 5, 2, 3, 2406, 1688, 128, 54, 95, '(650)'], [None, 650, '650']], [[5, 1, 5, 5, 2, 4, 2555, 1689, 219, 42, 95, '6186116'], [None, 6186116, '6186116']], [[5, 1, 5, 5, 2, 6, 3958, 1683, 16, 41, 96, '1'], [None, 1, '1']]])

        # empty list
        PDF_Info.cleanData = []
        self.x.search_currency_in_pdf(PDF_Info)
        self.assertEqual(PDF_Info.RawCurrency,[])

        # single entry list
        PDF_Info.cleanData = [[5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, '95014']]
        self.x.search_currency_in_pdf(PDF_Info)
        self.assertEqual(PDF_Info.RawCurrency, [[[5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, '95014'], [None, 95014, '95014']]])

        # no int
        PDF_Info.cleanData = [[5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, 'amkd'], [5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, 'klmdka']]
        self.x.search_currency_in_pdf(PDF_Info)
        self.assertEqual(PDF_Info.RawCurrency, [])


    def test_extract_currency_frm_pdf(self):
        PDF_Info = PDF_Information()
        PDF_Info.cleanData = [[5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, '95014'], [5, 1, 5, 4, 1, 8, 3653, 1515, 321, 42, 88, 'AE10071871'], [5, 1, 5, 5, 1, 1, 275, 1624, 132, 42, 94, 'Israel'], [5, 1, 5, 5, 1, 2, 2129, 1608, 157, 42, 95, '$'], [5, 1, 5, 5, 1, 3, 2309, 1607, 157, 43, 96, '1,000'], [5, 1, 5, 5, 1, 4, 3331, 1602, 208, 42, 95, 'Amount:'], [5,
        1, 5, 5, 1, 5, 3562, 1598, 282, 53, 95, '$60,000.00'], [5, 1, 5, 5, 1, 6, 3867, 1601, 114, 43, 94, 'USD'], [5, 1, 5, 5, 2, 1, 2129, 1689, 172, 42, 95, 'Phone:'], [5, 1, 5, 5, 2, 2, 2325, 1689, 52, 41, 95, '+1'], [5, 1, 5, 5, 2, 3, 2406, 1688, 128, 54, 95, '(650)'], [5, 1, 5, 5, 2, 4, 2555, 1689, 219, 42, 95, '6186116'], [5, 1, 5, 5, 2, 5, 3726, 1683, 205, 42, 96, 'Version:'], [5, 1, 5, 5, 2, 6, 3958, 1683, 16, 41, 96, '1'], [5, 1, 5, 5, 3, 1, 2129, 1770, 102, 42, 93, 'Fax:']]
        p_distance = 200
        PDP = Prepare_Data_PDF()
        PDP.get_pdf_network(PDF_Info,0)
        self.x.extract_currency_frm_pdf(PDF_Info, p_distance)
        self.assertEqual(PDF_Info.Currency, [[[[5, 1, 5, 5, 1, 2, 2129, 1608, 157, 42, 95, '$'], ['$', None, None]], [[5, 1, 5, 5, 1, 3, 2309, 1607, 157, 43, 96, '1,000'], [None, 1000, '1,000']]], [[[5, 1, 5, 5, 1, 5, 3562, 1598, 282, 53, 95, '$60,000.00'], ['$', 60000.00, '60,000.00']]]])

        PDF_Info.cleanData = [[5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, 'mksd'], [5, 1, 5, 4, 1, 8, 3653, 1515, 321, 42, 88, 'lkmkd'], [5, 1, 5, 5, 1, 1, 275, 1624, 132, 42, 94, 'Israel'], [5, 1, 5, 5, 1, 2, 2129, 1608, 157, 42, 95, 'kndkjnd'], [5, 1, 5, 5, 1, 3, 2309, 1607, 157, 43, 96, 'kmsl'], [5, 1, 5, 5, 1, 4, 3331, 1602, 208, 42, 95, 'Amount:'], [5,
        1, 5, 5, 1, 5, 3562, 1598, 282, 53, 95, 'kcd'], [5, 1, 5, 5, 1, 6, 3867, 1601, 114, 43, 94, 'kls'], [5, 1, 5, 5, 2, 1, 2129, 1689, 172, 42, 95, 'Phone:'], [5, 1, 5, 5, 2, 2, 2325, 1689, 52, 41, 95, '+1'], [5, 1, 5, 5, 2, 3, 2406, 1688, 128, 54, 95, '(650)'], [5, 1, 5, 5, 2, 4, 2555, 1689, 219, 42, 95, '6186116'], [5, 1, 5, 5, 2, 5, 3726, 1683, 205, 42, 96, 'Version:'], [5, 1, 5, 5, 2, 6, 3958, 1683, 16, 41, 96, '1'], [5, 1, 5, 5, 3, 1, 2129, 1770, 102, 42, 93, 'Fax:']]
        p_distance = 200
        PDP = Prepare_Data_PDF()
        PDP.get_pdf_network(PDF_Info,0)
        self.x.extract_currency_frm_pdf(PDF_Info, p_distance)
        self.assertEqual(PDF_Info.Currency,[])

        # print(PDF_Info.Currency)
    
    def test_search_currency_in_string(self):
        l_str = '$10,000'
        out_put = self.x.search_currency_in_string(l_str)
        print(out_put)
        


if __name__ == "__main__":
    # unittest.main()
    TECFP = TestExtractCurrencyFrmPDF()
    TECFP.setUp()
    TECFP.test_search_currency_in_string()