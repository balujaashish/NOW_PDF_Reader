import unittest
from extract_information_frm_pdf import Extract_Information_Frm_PDF
import z_test_data
from prepare_data_pdf import Prepare_Data_PDF
from PDF_information import PDF_Information

class testExtractInformationFrmPDF(unittest.TestCase):

    def setUp(self):
        self.x = Extract_Information_Frm_PDF()

    def test_get_exact_match(self):
        search_result = [['a','b','c'], ['a','b']]
        phrase = ['a','b','c']
        out_put = self.x.get_exact_match(search_result, phrase)
        self.assertEqual(out_put, [['a','b','c']])
        # single term in search-match
        search_result = [['a','b','c']]
        phrase = ['a','b','c']
        out_put = self.x.get_exact_match(search_result, phrase)
        self.assertEqual(out_put, [['a','b','c']])
        # single term in search-no match
        search_result = [['a','b','c']]
        phrase = ['a','b']
        out_put = self.x.get_exact_match(search_result, phrase)
        self.assertEqual(out_put, [])
        # empty search
        search_result = []
        phrase = ['a','b','c']
        out_put = self.x.get_exact_match(search_result, phrase)
        self.assertEqual(out_put, [])
        # single term
        search_result = [['a','b','c'], ['a']]
        phrase = ['a']
        out_put = self.x.get_exact_match(search_result, phrase)
        self.assertEqual(out_put, [['a']])
        # print(out_put)


    def test_extract_keywords_frm_PDF(self):
        PDF_I = PDF_Information()
        l_dict =  {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871'],[9829,939,921,'fhc']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'Qty (Unit)']]}
        PDF_I.rawData = [z_test_data.pdf_test_data1]
        PDP = Prepare_Data_PDF()
        # clean pdf data: remove blanks and convert string to int where needed.
        PDP.clean_data(PDF_I)
        # get network of term(all terms that allign with a term)
        PDP.get_pdf_network(PDF_I, 0) 
        distance= 50
        out_put = self.x.extract_keywords_frm_PDF(PDF_I, l_dict, 1,distance)
        self.assertEqual(out_put[('AE10071871', ('ae10071871',))], [[(5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0)], [(5, 1, 5, 4, 1, 8, 3653, 1515, 321, 42, 88, 'AE10071871', 0)]])

        self.assertEqual(out_put[('BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States', ('boardwalktech', ',', 'inc', '10050', 'n', '.', 'wolfe', 'rd', '.', '#', '276', 'cupertino', ',', 'ca', '95014', 'united', 'states'))], [[(5, 1, 5, 2, 1, 4, 2128, 1365, 531, 52, 89, 'boardwalktech', 0), [[5, 1, 5, 2, 1, 4, 2128, 1365, 531, 52, 89, ',', 1], ('equal', 0)], [[5, 1, 5, 2, 1, 5, 2682, 1365, 94, 44, 95, 'INC', 0], ('right', 23)], [[5, 1, 5, 3, 1, 4, 2131, 1447, 150, 42, 96, '10050', 0], ('down', 30)], [[5, 1, 5, 3, 1, 5, 2304, 1447, 48, 41, 96, 'n', 0], ('right', 23)], [[5, 1, 5, 3, 1, 5, 2304, 1447,
        48, 41, 96, '.', 1], ('equal', 0)], [[5, 1, 5, 3, 1, 6, 2374, 1446, 143, 43, 95, 'Wolfe', 0], ('right', 22)], [[5, 1, 5, 3, 1,
        7, 2539, 1447, 80, 42, 95, 'rd', 0], ('right', 22)], [[5, 1, 5, 3, 1, 7, 2539, 1447, 80, 42, 95, '.', 1], ('equal', 0)], [[5, 1, 5, 3, 1, 8, 2640, 1446, 125, 43, 96, '#', 0], ('right', 21)], [[5, 1, 5, 3, 1, 8, 2640, 1446, 125, 43, 96, '276', 1], ('equal', 0)], [[5, 1, 5, 4, 1, 4, 2128, 1527, 243, 54, 94, 'Cupertino', 0], ('down', 39)], [[5, 1, 5, 4, 1, 5, 2394, 1563, 6, 14, 94, ',', 0], ('right', 23)], [[5, 1, 5, 4, 1, 6, 2423, 1527, 77, 43, 96, 'CA', 0], ('right', 23)], [[5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, '95014', 0], ('right', 18)], [[5, 1, 5, 5, 1, 2, 2129, 1608, 157, 42, 95, 'United', 0], ('down', 27)], [[5, 1, 5, 5, 1, 3, 2309, 1607, 157, 43, 96, 'States', 0], ('right', 23)]]])


if __name__ == "__main__":
    unittest.main()