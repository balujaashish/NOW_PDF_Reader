from String_compare import String_Compare
from token_network import Token_Network
from Data_cleaner import Data_Cleaner

class Prepare_Data_PDF():

    def __init__(self):
        pass

    def get_pdf_network(self, p_data, p_ml_flag):
        """
        prepares word network for terms in pdf document, also cleans up data

        Args:
            p_data (list): pdf data as read by Pyteseract
            p_ml_flag (boolean): flag to use machine learning while comparing data.
            
        Returns:
            term network in pdf
        """
        
        # add page height, pytesseract doesnt know about pages it just reads each image idividually,
        # when we build network we need to build it for all pages, thus height must be
        # added to differentiate betweeen pages
        self.add_page_height(p_data)

        # first entry in p_data is column names we can ignore 
        l_data = []
        for d in p_data:
            l_data = l_data+ d[1:]

        # clean pdf data: remove blanks and convert string to int where needed.
        l_data = self.clean_data(l_data)

        # split terms if they can be split
        out_put = self.pdf_data_tokenize(l_data, self.get_term_index(), self.get_term, p_ml_flag)
        # get the term network
        out_put = self.get_term_network(out_put, self.get_indexes_with_pixel_info(), self.get_top, self.get_left, self.get_width, self.get_height, self.get_term)
        return out_put


    def clean_data(self, p_data):
        DC = Data_Cleaner()
        p_data = DC.clean_pdf_data(p_data, self.get_term, self.get_indexes_with_pixel_info())
        return p_data
         
    def get_term_network(self, p_data, indexes, get_top, get_left, get_width, get_height, get_term):
        TN = Token_Network()
        net_work = TN.get_neighbor_map(p_data, indexes, get_top, get_left, get_width, get_height, get_term)
        return net_work

    def pdf_data_tokenize(self, p_data, p_term_index, p_get_term, p_ml_flag):
        """
        check to see if any term in PDF tokenized terms can be further split, 
        this will allow us to compare phrases, as both keywords and pdf needs to be split in similar way.

        Args:
            p_data (list): pdf data as read by Pyteseract
            p_term_index (int): positon of term in data.(should be 11 for pdf)
            p_get_term (function) : returns term from a list.
            p_ml_flag (boolean): flag to use machine learning while preparing data.
            
        Returns:
            split terms in pdf data
        """
        out_put = []
        for term in p_data:
            term_n = self.pdf_term_tokenize(term, p_term_index, p_get_term, p_ml_flag)
            out_put = out_put + term_n
        return out_put



    
    def pdf_term_tokenize(self, p_term, p_term_index, p_get_term, p_ml_flag):
        out_put = []
        term_n = []
        SC= String_Compare()
        if p_term:
            # check if term can be further split
            term_tokens = SC.prepare_phrase(p_get_term(p_term), p_ml_flag)
            if len(term_tokens) > 1:
                # if term can be split copy all the pixel information and split the term.
                for i,term_token in enumerate(term_tokens):
                    term_n = p_term.copy()
                    term_n[p_term_index] = term_token
                    # add sequence number of split term in term.(we call it order)
                    term_n.append(i)
                    out_put.append(term_n)
            else: 
                # if term cant be split add order for consistency of data and return term
                term_n = p_term.copy()
                term_n.append(0)
                out_put.append(term_n)
            return out_put
        else: return []

    def add_page_height(self, p_data):
        page_start_height = 0
        # we will just use 100,000 as page height for now, we can calculate the page height if needed.
        page_height = 100000
        # traverse each page of PDF
        for i in range(len(p_data)): 
            # traverse each word token in page.  and update height.
            for j in range(1,len(p_data[i])):
                p_data[i][j][self.get_top_index()] = str(int(p_data[i][j][self.get_top_index()])+page_start_height)
            # for each page increment height by 100,000
            page_start_height = page_start_height + page_height


    def get_term(self, e):
        return e[self.get_term_index()]

    def get_term_index(self):
        return 11
    
    def get_top_index(self):
        return 7

    def get_indexes_with_pixel_info(self):
        return [0,1,2,3,4,5,6,7,8,9,10]

    def get_top(self, e):
        return e[7]

    def get_left(self, e):
        return e[6]

    def get_height(self, e):
        return e[9]

    def get_width(self, e):
        return e[8]
