
from prepare_data_keywords import Prepare_Data_Keywords
from PDF_reader import PDF_Reader
from prepare_data_pdf import Prepare_Data_PDF
from phrase_search import Phrase_Search
from PDF_information import PDF_Information

class Extract_Information_Frm_PDF():
    def __init__(self):
        pass

    def get_term1(self,e):
        return e[11]

    def get_order_term(self, e):
        return e[12]

    def get_order_value(self, e):
        return e[0][12]

    def get_direction(self, e):
        return e[1][0]

    def get_distance(self, e):
        return e[1][1]

    def get_term(self, e):
        return e[3]

    def extract_information_frm_PDF(self, p_pdf_path, p_keyword_dict, p_exact_match_only, p_distance):
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
        PDF_Info = PDF_Information()
        PDF_Info.network = self.get_pdf_term_network(p_pdf_path)

        PDF_Info.keywords = self.extract_keywords_frm_PDF(PDF_Info.network, p_keyword_dict, p_exact_match_only, p_distance)
        return PDF_Info
    
    def get_pdf_term_network(self, p_pdf_path):
        pdf_r = PDF_Reader()
        data = pdf_r.read(p_pdf_path)

        PDP = Prepare_Data_PDF()
        # clean pdf data: remove blanks and convert string to int where needed.
        l_data = PDP.clean_data(data)
        # get network of term(all terms that allign with a term)
        net_work = PDP.get_pdf_network(l_data, 0)
        return net_work




    def extract_keywords_frm_PDF(self, p_net_work, p_keyword_dict, p_exact_match_only, p_distance):
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
            match = PS.search(p_net_work, phrases[key], self.get_term1, self.get_direction, self.get_distance, self.get_order_term, self.get_order_value, p_distance)
            if match and p_exact_match_only:
                out_put[(key, tuple(phrases[key]))] = self.get_exact_match(match,phrases[key])      
        return out_put
                    

    def get_exact_match(self, p_search_results, p_phrase):
        out_put = []
        for p_search_result in p_search_results:
            if len(p_phrase) == len(p_search_result):
                out_put.append(p_search_result)
        return out_put


if __name__ == "__main__":

    l_dict =  {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'AE10071871'],[9829,939,921,'fhc']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'Qty (Unit)']]}

    FilePath = "C:/Users/Win10Office2016/Desktop/Python-Proj/NOW-PDF_Reader/Test_Files/"
    FilePath = FilePath+"teva po.pdf"

    distance= 50

    EIFP = Extract_Information_Frm_PDF()
    out_put = EIFP.extract_information_frm_PDF(FilePath, l_dict, True, distance) 
    for search_result in out_put.keywords:
        print("-----------------------------------------------------")
        print (search_result)
        print(out_put.keywords[search_result])