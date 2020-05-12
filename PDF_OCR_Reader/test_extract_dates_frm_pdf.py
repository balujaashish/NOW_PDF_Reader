import unittest
from extract_dates_frm_pdf import Extract_Dates_Frm_PDF
from PDF_information import PDF_Information
from prepare_data_pdf import Prepare_Data_PDF

class TestExtractDatesFrmPDF(unittest.TestCase):

    def setUp(self):
        self.x = Extract_Dates_Frm_PDF()

    def get_exact_match(self, p_search_results, p_phrase):
        out_put = []
        for p_search_result in p_search_results:
            if len(p_phrase) == len(p_search_result):
                out_put.append(p_search_result)
        return out_put


    def test_get_unique_dates(self):
        PDF_Info = PDF_Information()
        PDF_Info.dates = {'a mar 2020':['mar 2020'], 'a mar 2021':['mar 2021'], 'a mar 2020 hello':['mar 2020']}
        out_put = self.x.get_unique_dates(PDF_Info)
        self.assertEqual(out_put, {'mar 2020', 'mar 2021'})

        PDF_Info.dates = {'a mar 2020':['mar 2020'], 'a mar 2020 hello':['mar 2020']}
        out_put = self.x.get_unique_dates(PDF_Info)
        self.assertEqual(out_put, {'mar 2020'})
        # single entry
        PDF_Info.dates = {'a mar 2020':['mar 2020']}
        out_put = self.x.get_unique_dates(PDF_Info)
        self.assertEqual(out_put, {'mar 2020'})
        # empty dates
        PDF_Info.dates = {}
        out_put = self.x.get_unique_dates(PDF_Info)
        self.assertEqual(out_put, set({}))

    
    def test_search_dates_in_pdf(self):
        PDF_Info = PDF_Information()
        PDF_Info.PDF_Lines = [[['hey todat is 5/7/2020!']], [['hey todat is May 7th 2020']], [['hey todat is May 2020!']]]
        self.x.search_dates_in_pdf(PDF_Info)
        self.assertEqual(PDF_Info.dates, {'hey todat is 5/7/2020!': ['5/7/2020'], 'hey todat is May 7th 2020': ['May 7th 2020'], 'hey todat is May 2020!': ['May 2020']})
        # single entry
        PDF_Info.PDF_Lines = [[['hey todat is 5/7/2020!']]]
        self.x.search_dates_in_pdf(PDF_Info)
        self.assertEqual(PDF_Info.dates, {'hey todat is 5/7/2020!': ['5/7/2020']})
        # no date found
        PDF_Info.PDF_Lines = [[['hey todat is !']], [['hey todat is May ']], [['hey todat is !']]]
        self.x.search_dates_in_pdf(PDF_Info)
        self.assertEqual(PDF_Info.dates, {})
        # empty dates
        PDF_Info.PDF_Lines = []
        self.x.search_dates_in_pdf(PDF_Info)
        self.assertEqual(PDF_Info.dates, {})


    def test_extract_dates_frm_pdf(self):
        PDF_Info = PDF_Information()
        PDF_Info.rawData = [[5, 1, 5, 4, 1, 7, 2518, 1528, 154, 42, 95, '95014'], [5, 1, 5, 4, 1, 8, 3653, 1515, 321, 42, 88, 'AE10071871'], [5, 1, 5, 5, 1, 1, 275, 1624, 132, 42, 94, 'Israel'], [5, 1, 5, 5, 1, 2, 2129, 1608, 157, 42, 95, '$'], [5, 1, 5, 5, 1, 3, 2309, 1607, 157, 43, 96, '1,000'], [5, 1, 5, 5, 1, 4, 3331, 1602, 208, 42, 95, 'Mar2020'], [5,
        1, 5, 5, 1, 5, 3562, 1598, 282, 53, 95, '$60,000.00'], [5, 1, 5, 5, 1, 6, 3867, 1601, 114, 43, 94, 'USD'], [5, 1, 5, 5, 2, 1, 2129, 1689, 172, 42, 95, 'Phone:'], [5, 1, 5, 5, 2, 2, 2325, 1689, 52, 41, 95, '+1'], [5, 1, 5, 5, 2, 3, 2406, 1688, 128, 54, 95, '(650)'], [5, 1, 5, 5, 2, 4, 2555, 1689, 219, 42, 95, '6186116'], [5, 1, 5, 5, 2, 5, 3726, 1683, 205, 42, 96, 'Version:'], [5, 1, 5, 5, 2, 6, 3958, 1683, 16, 41, 96, '1'], [5, 1, 5, 5, 3, 1, 2129, 1770, 102, 42, 93, 'Fax:']]
        p_distance = 50
        PDP = Prepare_Data_PDF()
        PDP.get_pdf_network(PDF_Info,0)
        PDP.get_pdf_lines(PDF_Info)
        self.x.extract_dates_frm_pdf(PDF_Info, self.get_exact_match,  p_distance)
        print(PDF_Info.PDF_Lines)
        print(PDF_Info.dates)




if __name__ == "__main__":
    # unittest.main()
    EDF_pdf = TestExtractDatesFrmPDF()
    EDF_pdf.setUp()
    EDF_pdf.test_extract_dates_frm_pdf()
