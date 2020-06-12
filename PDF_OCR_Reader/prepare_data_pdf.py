from PDF_OCR_Reader.String_compare import String_Compare
from PDF_OCR_Reader.token_network import Token_Network
from PDF_OCR_Reader.Data_cleaner import Data_Cleaner

class Prepare_Data_PDF():

    def __init__(self):
        pass

    def get_pdf_network(self, PDF_Info, p_ml_flag):
        """
        prepares word network for terms in pdf document, also cleans up data

        Args:
            PDF_Info (PDF_Information class objeact): pdf information extracted
            p_ml_flag (boolean): flag to use machine learning while comparing data.
            
        Returns:
            term network in pdf
        """
        # split terms if they can be split
        out_put = self.pdf_data_tokenize(PDF_Info.cleanData, PDF_Info.get_term_index(), PDF_Info.get_term, p_ml_flag)
        # get the term network
        PDF_Info.network = self.get_term_network(out_put, PDF_Info.get_indexes_with_pixel_info(), PDF_Info.get_top, PDF_Info.get_left, PDF_Info.get_width, PDF_Info.get_height, PDF_Info.get_term)
        


    def clean_data(self, PDF_Info):
        # add page height, pytesseract doesnt know about pages it just reads each image idividually,
        # when we build network we need to build it for all pages, thus height must be
        # added to differentiate betweeen pages
        PDF_Info.cleanData = PDF_Info.rawData.copy()
        self.add_page_height(PDF_Info.cleanData, PDF_Info.get_top_index)

        # first entry in p_data is column names we can ignore 
        l_data = []
        for d in PDF_Info.cleanData:
            l_data = l_data+ d[1:]

        DC = Data_Cleaner()
        PDF_Info.cleanData = DC.clean_pdf_data(l_data, PDF_Info.get_term, PDF_Info.get_top, PDF_Info.get_left, PDF_Info.get_height, PDF_Info.get_width, PDF_Info.get_indexes_with_pixel_info(), PDF_Info.get_num_elements())
         
    

    def get_pdf_lines(self, PDF_Info):
        """
        re-constructs pdf lines from term network.

        Args:
            PDF_Info (PDF_Information): pdf information extracted
            
        Returns:
            lines in pdf asa list.
            eg: [[['Purchase order: AE10071871'], [[5, 1, 1, 1, 1, 1, 256, 284, 410, 76, 95, 'Purchase', 0], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, 'order', 0], ('right', 32)], [[5, 1, 1, 1, 1, 2, 698, 283, 271, 77, 91, ':', 1], ('right', 32)], [[5, 1, 1, 1, 1, 3, 1001, 284, 558, 76, 88, 'AE10071871', 0], ('right', 335)]]]]
        """

        l_covered = []
        l_lines = []
        for key in PDF_Info.network:
            line =[]
            line_text = ''
            # all terms will occur as key in network.
            # if a term has already been covered we dont want to add the term again to avaoid partial sentences.
            if list(key) not in l_covered:
                line.append(list(key))
                line_text = PDF_Info.get_term(key)
                l_covered.append(list(key))
                # all terms that are equal or align to right(in network dictionary) will be added to create a pdf line.
                for term in PDF_Info.network[key]:
                    if PDF_Info.get_direction(term) == 'equal' or PDF_Info.get_direction(term) == 'right':
                        line.append(list(term))
                        line_text = self.add_term_to_line(line_text, PDF_Info.get_order_value, PDF_Info.get_term_dict_value, term)
                        l_covered.append(list(term[0]))
            if line:
                l_lines.append([[line_text],line])
            # update pdf information with the lines data
        if l_lines:
            PDF_Info.PDF_Lines = l_lines
    
    def add_term_to_line(self, line_text, p_get_order_value, p_get_term_dict_value, p_term):
        order = p_get_order_value(p_term)
        # if order is greater than 1 then the term was split again. Thus we do not add space when recreating sentence.
        if order > 0:
            line_text = line_text + p_get_term_dict_value(p_term)
        else:
            line_text = line_text +' '+ p_get_term_dict_value(p_term)
        return line_text
        

    
    
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

    def add_page_height(self, p_data, p_get_top_index):
        page_start_height = 0
        # we will just use 100,000 as page height for now, we can calculate the page height if needed.
        page_height = 100000
        # traverse each page of PDF
        for i in range(len(p_data)): 
            # traverse each word token in page.  and update height.
            for j in range(1,len(p_data[i])):
                p_data[i][j][p_get_top_index()] = str(int(p_data[i][j][p_get_top_index()])+page_start_height)
            # for each page increment height by 100,000
            page_start_height = page_start_height + page_height


    