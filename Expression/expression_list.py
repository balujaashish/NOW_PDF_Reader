from Expression.network_navigator import Network_Navigtor
from Expression.keywords import Keywords

class Expression_List():

    def __init__(self, PDF_Info, p_supporting_data, p_attributes):
        self.pdf_info = PDF_Info
        self.supporting_data = p_supporting_data
        self.attributes = p_attributes
        self.KW = Keywords(self.pdf_info, self.supporting_data, self.attributes)

    
    def get(self, p_list_name, p_keyword = []):
        l_list_data = self.get_list_data_pdf_info(p_list_name)
        l_list_data = self.strip_details(l_list_data)
        l_list_data = self.qualify(l_list_data)
        if p_keyword:
            l_list_expression_dtl = self.list_expression(p_keyword, l_list_data)
            return self.extract_list_expression(l_list_expression_dtl)
        else:
            for i, data in enumerate(l_list_data):
                l_list_data[i].insert(0, p_list_name)
            return l_list_data


    

    def extract_list_expression(self, p_exps_dtls):
        out_put = []
        for expression in p_exps_dtls:
            l_KeyWord, l_list_data = expression[0], expression[1]
            l_ExpAlign, l_direction, l_distance, l_value_dtls,l_key_dtls = expression[2], expression[3], expression[4], expression[5], expression[6]
            out_put.append([l_KeyWord, l_list_data, [l_ExpAlign, l_direction, l_distance, l_value_dtls, l_key_dtls]])
        return out_put



    def qualify(self, p_dates):
        return p_dates

            
                
    def list_expression(self, p_keywords, p_list_data):
        out_put = []
        NN = Network_Navigtor()
        l_keyword_str = p_keywords[0]
        for p_keyword in p_keywords[1]:
            for l_list_data in p_list_data:
                l_list_data_str = l_list_data[0]
                NN.align(self.pdf_info, p_keyword, l_list_data[1])
                if NN.alignment_list:
                    out_put.append([l_keyword_str, l_list_data_str, NN.alignment_list, NN.direction, NN.distance, l_list_data[1], p_keyword])
        return out_put



    def strip_details(self, p_dates):
        out_put = []
        for key in p_dates:
            for l_date in p_dates[key]:
                out_put.append([key, l_date])
        return out_put



    def get_list_data_pdf_info(self, p_name):
        list_terms = []
        # get list from supporting data
        l_list_data = self.supporting_data.get(p_name)
        # search each term in list in keywords, match will be found only if term exixts in pdf.
        if l_list_data:
            for l_data in l_list_data:
                list_terms.append(self.supporting_data.get_term(l_data))
        out_put = self.search_list_data_pdf_info(list_terms)
        return out_put

            
    
    def search_list_data_pdf_info(self, p_list_data):
        out_put = {}
        # list data is added to keywords before searching keywords in pdf term network.
        # need to fetch list data from keywords.
        for l_list_data in p_list_data:
            list_terms = self.KW.get(l_list_data)        
            out_put[l_list_data] = list_terms
        return out_put