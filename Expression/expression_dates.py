from Expression.keywords import Keywords
from Expression.network_navigator import Network_Navigtor

class Expression_Dates():

    def __init__(self, PDF_Info, p_supporting_data, p_attributes):
        self.pdf_info = PDF_Info
        self.supporting_data = p_supporting_data
        self.attributes = p_attributes
        self.KW = Keywords(self.pdf_info, self.supporting_data, self.attributes)
        

    def get(self, p_keyword):
        l_dates = self.search_dates_pdf_info()
        l_dates = self.strip_details(l_dates)
        l_dates = self.qualify(l_dates)
        l_date_expression_dtl = self.date_expression(p_keyword, l_dates)
        return self.extract_date_expression(l_date_expression_dtl)

    def extract_date_expression(self, p_exps_dtls):
        out_put = []
        for expression in p_exps_dtls:
            l_KeyWord, l_Date = expression[0], expression[1]
            l_ExpAlign, l_direction, l_distance, l_value_dtls, l_key_dtls = expression[2], expression[3], expression[4], expression[5], expression[6]
            out_put.append([l_KeyWord, l_Date, [l_ExpAlign, l_direction, l_distance, l_value_dtls, l_key_dtls]])
        return out_put



    def qualify(self, p_dates):
        return p_dates
        

    def search_date_pdf_info(self, p_date):
        out_put = {}
        # for each term in p_date get the details from pdf_info
        for l_date in p_date:
            # get pdf_info information for l_date using keyword class module.
            # each date is added to keyword list before keyword information extraction, thus date details need to be
            # extracted from pdf_info.keywords
            date_terms = self.KW.get(l_date)        
            out_put[l_date] = date_terms
        return out_put


    def search_dates_pdf_info(self):
        out_put = {}
        for key in self.pdf_info.dates:
            pdf_date = self.search_date_pdf_info(self.pdf_info.dates[key])
            if pdf_date:
                out_put.update(pdf_date)
        return out_put


    def date_expression(self, p_keywords, p_dates):
        out_put = []
        NN = Network_Navigtor()
        if p_keywords:
            l_keyword_str = p_keywords[0]
            # using network nvigator check if date aligns with date
            # for two terms to be considered aligned atleast one term in keyword needs to be aligned with one term in date
            # traverse over all occurances of keyword in pdf
            for p_keyword in p_keywords[1]:
                # traverse over all occurances of date in pdf
                for l_date in p_dates:
                    l_date_str = l_date[0]
                    # check if p_keyword aligns with l_date
                    NN.align(self.pdf_info, p_keyword, l_date[1])
                    if NN.alignment_list:
                        out_put.append([l_keyword_str, l_date_str, NN.alignment_list, NN.direction, NN.distance, l_date[1], p_keyword])
        return out_put


    def get_full_date_from_network(self):
        pass


    def strip_details(self, p_dates):
        # convert dictionary to list of format:
        # [["date_str",[[term1], [term2]]], ["date_str",[[term1], [term2]]]]
        out_put = []
        for key in p_dates:
            for l_date in p_dates[key]:
                out_put.append([key, l_date])
        return out_put

