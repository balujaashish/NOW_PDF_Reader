from Expression.network_navigator import Network_Navigtor

class Expression_Currency():

    def __init__(self, PDF_Info, p_supporting_data, p_attributes):
        self.pdf_info = PDF_Info
        self.supporting_data = p_supporting_data
        self.attributes = p_attributes


    def get(self, p_keyword):
        l_currency = self.pdf_info.Currency
        l_currency = self.qualify(l_currency)
        l_currency = self.prepare_currency_data(l_currency)
        l_currency_expression_dtl = self.currency_expression(p_keyword, l_currency)
        return self.extract_currency_expression(l_currency_expression_dtl)

    

    def extract_currency_expression(self, p_exps_dtls):
        out_put = []
        for expression in p_exps_dtls:
            l_KeyWord, l_currency = expression[0], expression[1]
            l_ExpAlign, l_direction, l_distance, l_value_dtls, l_key_dtls = expression[2], expression[3], expression[4], expression[5], expression[6]
            out_put.append([l_KeyWord, l_currency, [l_ExpAlign, l_direction, l_distance, l_value_dtls, l_key_dtls]])
        return out_put

    def qualify(self, p_currency):
        # we only look at terms that alone qualify as currency. 
        # terms around that contribute to currency will be handled in later release
        out_put = []
        for l_currency_dtl in p_currency:
            for l_currency in l_currency_dtl:
                # for each term make sure all thhree fields have a value curency type, currency numerical value.
                if l_currency[1][0] is not None and l_currency[1][1] is not None and l_currency[1][2] is not None:
                    out_put.append(l_currency)
        return out_put

            
                
    def currency_expression(self, p_keywords, p_currency):
        out_put = []
        NN = Network_Navigtor()
        if p_keywords:
            # get currency keyword string from p_keyword, example: "Amount"
            l_keyword_str = p_keywords[0]
            # traverse over each occurance of keyword in document, captured in p_keywords[1]
            for p_keyword in p_keywords[1]:
                # using network navigator to check if keyword aligns with any currency occurance in pdf_info
                for l_currency in p_currency:
                    l_currency_str = l_currency[0]
                    l_currency_i = self.pdf_info.get_matching_key(l_currency[1][0])
                    # check if currency aligns with keyword
                    NN.align(self.pdf_info, p_keyword, l_currency_i)
                    if NN.alignment_list:
                        out_put.append([l_keyword_str, l_currency_str, NN.alignment_list, NN.direction, NN.distance, l_currency[1], p_keyword])
        return out_put
    
    # def get_full_currency_from_network(self):
    #     pass

    # def strip_details(self, p_dates):

    def prepare_currency_data(self, p_currency):
        out_put = []
        # for currency data remove currency details at index = 1, and extraxt currency text
        for i_currency in p_currency:
            # get currency text
            l_currency_str = self.pdf_info.get_term(i_currency[0])
            # while preparing output ignore currency details at index = 1
            out_put.append([l_currency_str,[i_currency[0]]])
        return out_put



    
