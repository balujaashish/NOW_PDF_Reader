from Expression.network_navigator import Network_Navigtor

class Expression_Numbers():

    def __init__(self, PDF_Info, p_supporting_data, p_attributes):
        self.pdf_info = PDF_Info
        self.supporting_data = p_supporting_data
        self.attributes = p_attributes


    def get(self, p_keyword):
        l_number = self.pdf_info.integers
        l_number = self.qualify(l_number)
        l_number = self.prepare_number_data(l_number)
        l_number_expression_dtl = self.number_expression(p_keyword, l_number)
        return self.extract_number_expression(l_number_expression_dtl)

    

    def extract_number_expression(self, p_exps_dtls):
        out_put = []
        for expression in p_exps_dtls:
            l_KeyWord, l_number = expression[0], expression[1]
            l_ExpAlign, l_direction, l_distance, l_value_dtls, l_key_dtls = expression[2], expression[3], expression[4], expression[5], expression[6]
            out_put.append([l_KeyWord, l_number, [l_ExpAlign, l_direction, l_distance, l_value_dtls, l_key_dtls]])
        return out_put

    def qualify(self, p_numbers):
        out_put = []
        for l_int in p_numbers:
            l_int_i = int(self.pdf_info.get_term(l_int))
            l_int_s = str(l_int_i)
            if l_int_s == self.pdf_info.get_term(l_int):
                out_put.append(l_int)
        return out_put

            
                
    def number_expression(self, p_keywords, p_number):
        out_put = []
        NN = Network_Navigtor()
        l_keyword_str = p_keywords[0]
        for p_keyword in p_keywords[1]:
            for l_number in p_number:
                l_number_str = l_number[0]
                l_number_i = self.pdf_info.get_matching_key(l_number[1][0])
                NN.align(self.pdf_info, p_keyword, l_number_i)
                if NN.alignment_list:
                    out_put.append([l_keyword_str, l_number_str, NN.alignment_list, NN.direction, NN.distance, l_number[1], p_keyword])
        return out_put
    
    # def get_full_number_from_network(self):
    #     pass

    # # def strip_details(self, p_dates):

    def prepare_number_data(self, p_number):
        out_put = []
        for i_number in p_number:
            l_number_str = self.pdf_info.get_term(i_number)
            out_put.append([l_number_str,[i_number]])
        return out_put



    
