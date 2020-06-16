
from PDF_OCR_Reader.prepare_data_keywords import Prepare_Data_Keywords
from PDF_OCR_Reader.PDF_reader import PDF_Reader
from PDF_OCR_Reader.prepare_data_pdf import Prepare_Data_PDF
from PDF_OCR_Reader.phrase_search import Phrase_Search
from PDF_OCR_Reader.PDF_information import PDF_Information
from PDF_OCR_Reader.extract_currency_frm_pdf import Extract_Currency_Frm_PDF
from PDF_OCR_Reader.extract_dates_frm_pdf import Extract_Dates_Frm_PDF
from PDF_OCR_Reader import extract_tbl_frm_pdf
import os
from PDF_OCR_Reader.String_compare import String_Compare


class Extract_Information_Frm_PDF():
    def __init__(self):
        self.pdf_r = PDF_Reader()
        self.ECFP = Extract_Currency_Frm_PDF()
        self.EDFP = Extract_Dates_Frm_PDF()
        self.PDK = Prepare_Data_Keywords()

        

    def get_keyword(self, e):
        return e[3]

    def extract_information_frm_PDF(self, p_pdf_path, p_keyword_dict, p_exact_match_only, p_distance, p_currency_distance, p_scan_for_tbl = 0):
        """
        extracts information from pdf with location in document. Extracts:
                => keywords
                => currency
                => integers
                => dates
        Args:
            p_pdf_path (string): path to pdf document.
            p_keyword_dict (dictionary): keyword dictionary: key = list name, value = list.
            p_exact_match_only (Boolean): 1 = returns only exact match, 0 = return partial match as well.
            p_distance (int): distance in pixel while looking for term in proximity
        Returns:       
        """
        # get pdf term network.
        PDF_Info = PDF_Information()
        self.get_pdf_term_network(PDF_Info, p_pdf_path)

        # get pdf lines
        self.get_pdf_lines(PDF_Info)
        # get keywords from term network
        PDF_Info.keywords = self.extract_keywords_frm_PDF(PDF_Info, p_keyword_dict, p_exact_match_only, p_distance)

        # search dates
        self.EDFP.extract_dates_frm_pdf(PDF_Info, self.get_exact_match, p_distance)

        #search currency
        self.ECFP.extract_currency_frm_pdf(PDF_Info, p_currency_distance)

        # search numbers
        self.extract_numbers_frm_PDF(PDF_Info)

        # extract table
        if p_scan_for_tbl:
            self.extract_information_frm_table(PDF_Info, p_keyword_dict)

        # remove all images created
        self.pdf_r.clear_image_files(PDF_Info.page_count)

        return PDF_Info



    def extract_keywords_frm_PDF(self, PDF_Info, p_keyword_dict, p_exact_match_only, p_distance):
        """
        extracts keywords from pdf with location in document.

        Args:
            p_net_work (dictionary): term network in pdf document.
            p_keyword_dict (dictionary): keyword dictionary: key = list name, value = list.
            p_exact_match_only (Boolean): 1 = returns only exact match, 0 = return partial match as well.
            p_distance (int): distance in pixel while looking for term in proximity

        Returns:
            
        """     
        out_put = {}
        phrases = self.PDK.tokenize_keywords_dictionary(p_keyword_dict)

        PS = Phrase_Search()
        # for key in search_result:
        for key in phrases:
            match = PS.search(PDF_Info, phrases[key], p_distance)
            if match and p_exact_match_only:
                out_put[(key, tuple(phrases[key]))] = self.get_exact_match(match,phrases[key])      
        return out_put


    def extract_numbers_frm_PDF(self, PDF_Info):
        out_put_int = []
        out_put_float = []
        for key in PDF_Info.network:
            if PDF_Info.get_term(key).isdigit():
                out_put_int.append(list(key))
            else:
                try:
                    float(PDF_Info.get_term(key))
                    out_put_float.append(key)
                except ValueError:
                    pass
        PDF_Info.integers = out_put_int
        PDF_Info.decimals = out_put_float

    def extract_numbers_frm_str(self, p_term):
        out_put_int = []
        if p_term.isdigit():
            out_put_int.append(p_term)
        return out_put_int 
        
    def extract_decimals_frm_str(self, p_term):
        out_put_float = []
        try:
            float(p_term)
            out_put_float.append(p_term)
        except ValueError:
            pass
        return out_put_float

    def extract_keywords_frm_str(self, p_keywords, p_text, p_exact_match_only, p_distance):     
        out_put = {}
        for keyword in p_keywords:
            if self.is_substring(p_text, keyword):
                return keyword
        return ''


    def is_sublist(self, a, b):
        if not a: return True
        if not b: return False
        return b[:len(a)] == a or self.is_sublist(a, b[1:])

    def is_substring(self, str1, str2):
        sc = String_Compare()
        str1 = sc.strip_punctuations(str1)
        w1 = sc.prepare_phrase(str1,0)
        str2 = sc.strip_punctuations(str2)
        w2 = sc.prepare_phrase(str2,0)
        print(w1)
        print(w2)
        if self.is_sublist(w2, w1):
            return True
        else: return False
    

    
    def extract_tbl_frm_pdf(self, PDF_Info):
        E_TBL_pdf = extract_tbl_frm_pdf
        for i in range(1, PDF_Info.page_count + 1): 
            # Set filename to recognize text from page_n.jpg  
            filename = "page_"+str(i)+".jpg"
            if os.path.exists(filename):
                E_TBL_pdf.get_tbl_frm_img(filename, PDF_Info)
                # print('-----------------------------------------------------------------------------')
                # print('-----------------------------------Boxes-------------------------------------')
                # print('------------------------------------------------------------------------------')
                # print(PDF_Info.Boxes)
                # print('-----------------------------------------------------------------------------')
                # print('-----------------------------------cells-------------------------------------')
                # print('------------------------------------------------------------------------------')
                # print(PDF_Info.cells)
                # print('-----------------------------------------------------------------------------')
                # print('-----------------------------------box_terms-------------------------------------')
                # print('------------------------------------------------------------------------------')
                # print(PDF_Info.box_terms)
                # print('-----------------------------------------------------------------------------')
                # print('-----------------------------------box_map-------------------------------------')
                # print('------------------------------------------------------------------------------')
                # print(PDF_Info.box_map)
    
    def extract_information_frm_table(self, PDF_Info, p_keyword_dict):
        self.extract_tbl_frm_pdf(PDF_Info)
        l_keywords = self.PDK.get_vocab(p_keyword_dict, self.PDK.get_term, self.PDK.get_key_term)
        print('---------------------------keywords vocab---------------------------')
        print (l_keywords)

        box_currency = []
        box_dates = []
        box_numbers = []
        box_decimals = []
        box_keywords = []
        for cell in PDF_Info.cells:
            print('------------------------cell----------------')
            print(cell)
            text = PDF_Info.Boxes[cell]
            print(text)
            # check for currency
            l_currency = self.ECFP.search_currency_in_string(text)
            if l_currency:
                box_currency.append([cell, text, l_currency])
            # check for date
            l_dates = self.EDFP.search_dates_in_str(text)
            if l_dates:
                box_dates.append([cell, text, l_dates])
            # check for keywords
            l_keyword = self.extract_keywords_frm_str(l_keywords, text, 0, 50)
            if l_keyword:
                box_keywords.append([cell, text, l_keyword])
            # check for numbers
            l_number = self.extract_numbers_frm_str(text)
            if l_number:
                box_numbers.append([cell, text, l_number])
            # check for decimals
            else:
                l_decimal = self.extract_decimals_frm_str(text)
                if l_decimal:
                    box_decimals.append([cell, text, l_decimal])
            

        PDF_Info.box_currency = box_currency
        PDF_Info.box_dates = box_dates
        PDF_Info.box_numbers = box_numbers
        PDF_Info.box_decimals = box_decimals
        PDF_Info.box_keywords = box_keywords

        
            


    def get_pdf_term_network(self, PDF_Info, p_pdf_path):
        # read pdf data
        PDF_Info.rawData, PDF_Info.page_count = self.pdf_r.read(p_pdf_path)

        PDP = Prepare_Data_PDF()
        # clean pdf data: remove blanks and convert string to int where needed.
        PDP.clean_data(PDF_Info)
        # get network of term(all terms that allign with a term)
        PDP.get_pdf_network(PDF_Info, 0)


    def get_pdf_lines(self, PDF_Info):
        PD_PDF = Prepare_Data_PDF()
        PD_PDF.get_pdf_lines(PDF_Info)

                    

    def get_exact_match(self, p_search_results, p_phrase):
        out_put = []
        for p_search_result in p_search_results:
            if len(p_phrase) == len(p_search_result):
                out_put.append(p_search_result)
        return out_put

    


    


if __name__ == "__main__":

    l_dict =  {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'6000567751'],[9829,939,921,'fhc']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'PART NUMBER']]}

    FilePath = "C:/Users/Win10Office2016/Desktop/Python-Proj/NOW-PDF_Reader/Test_Files/"
    FilePath = FilePath+"Order No 6000567751.pdf"

    distance= 50
    p_currency_distance = 200

    EIFP = Extract_Information_Frm_PDF()
    out_put = EIFP.extract_information_frm_PDF(FilePath, l_dict, True, distance, p_currency_distance, p_scan_for_tbl=1) 
    
    print("----------------------------------------------------------")
    print("--------------------dates---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.dates)

    print("----------------------------------------------------------")
    print("--------------------currency---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.Currency)

    print("----------------------------------------------------------")
    print("--------------------lines---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.PDF_Lines)

    print("----------------------------------------------------------")
    print("--------------------keywords---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.keywords)

    print("----------------------------------------------------------")
    print("--------------------integers---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.integers)

    print("----------------------------------------------------------")
    print("--------------------decimals---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.decimals)

    print("----------------------------------------------------------")
    print("--------------------clean data---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.cleanData)
    



    