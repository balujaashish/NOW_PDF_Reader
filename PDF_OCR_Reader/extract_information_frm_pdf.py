
from prepare_data_keywords import Prepare_Data_Keywords
from PDF_reader import PDF_Reader
from prepare_data_pdf import Prepare_Data_PDF
from phrase_search import Phrase_Search
from PDF_information import PDF_Information
from extract_currency_frm_pdf import Extract_Currency_Frm_PDF
from extract_dates_frm_pdf import Extract_Dates_Frm_PDF

class Extract_Information_Frm_PDF():
    def __init__(self):
        pass

    def get_keyword(self, e):
        return e[3]

    def extract_information_frm_PDF(self, p_pdf_path, p_keyword_dict, p_exact_match_only, p_distance, p_currency_distance):
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
        EDFP = Extract_Dates_Frm_PDF()
        EDFP.extract_dates_frm_pdf(PDF_Info, self.get_exact_match, p_distance)

        #search currency
        ECFP = Extract_Currency_Frm_PDF()
        ECFP.extract_currency_frm_pdf(PDF_Info, p_currency_distance)

        # search numbers
        self.extract_numbers_frm_PDF(PDF_Info)

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
        
        PDK = Prepare_Data_Keywords()
        phrases = PDK.tokenize_keywords_dictionary(p_keyword_dict)

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
        
            


    def get_pdf_term_network(self, PDF_Info, p_pdf_path):
        pdf_r = PDF_Reader()
        # read pdf data
        PDF_Info.rawData = pdf_r.read(p_pdf_path)

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
    FilePath = FilePath+"teva po.pdf"

    distance= 50
    p_currency_distance = 200

    EIFP = Extract_Information_Frm_PDF()
    out_put = EIFP.extract_information_frm_PDF(FilePath, l_dict, True, distance, p_currency_distance) 
    
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
    for line in out_put.PDF_Lines:
        print (line)

    print("----------------------------------------------------------")
    print("--------------------keywords---------------------------------")
    print("----------------------------------------------------------")
    for key in out_put.keywords:
        print(key)
        print (out_put.keywords[key])

    print("----------------------------------------------------------")
    print("--------------------integers---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.integers)

    print("----------------------------------------------------------")
    print("--------------------decimals---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.decimals)