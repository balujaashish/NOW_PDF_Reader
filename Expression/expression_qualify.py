class Expression_Qualify():

    def __init__(self, PDF_Info, p_supporting_data, p_attributes):
        self.pdf_info = PDF_Info
        self.supporting_data = p_supporting_data
        self.attributes = p_attributes


    def qualify(self, p_expression_match, p_attribute_name):
        out_put =[]
        if p_attribute_name:
            l_allowed_terms = self.supporting_data.data[self.attributes[p_attribute_name]]
            for match in p_expression_match:
                if self.qualify_each_expression_match(match, l_allowed_terms):
                    out_put.append(match)
        return out_put
    
    def qualify_each_expression_match(self, p_match, p_allowed_terms):
        details = {}
        details = self.get_expression_match_details(p_match)
        # l_keywords, l_value = self.get_keywod_and_value_terms(details['Align-dtls'])
        for l_align in details['Align-dtls']:
            if not self.qualify_expression_match_term_align_dtls(l_align, p_allowed_terms):
                return False
        return True


    def qualify_expression_match_term_align_dtls(self, p_align_dtls, p_allowed_terms):
        for p_align_dtl in p_align_dtls[1]:
            for term in p_align_dtl[1]:
                term_txt = self.pdf_info.get_term(term[0])
                if term_txt.lower() not in p_allowed_terms:
                    return False
        return True



    def get_expression_match_details(self, p_match):
        out_put = {}
        l_keyword, l_value, l_details = p_match[0], p_match[1], p_match[2]
        l_align_dtls, l_dir_dtls, l_dist_dtls = l_details[0], l_details[1], l_details[2]
        out_put['Keyword'] = l_keyword
        out_put['Value'] = l_value
        out_put['Direction'] = l_dir_dtls
        out_put['Distance'] = l_dist_dtls
        out_put['Align-dtls'] = l_align_dtls
        return out_put


    def get_keywod_and_value_terms(self, p_align_dtls):
        l_keywords, l_values = {}, {}
        l_keywords = set()
        l_values = set()
        for p_align_dtl in p_align_dtls:
            l_keywords.add(tuple(p_align_dtl[0]))
            for t in p_align_dtl[1]:
                l_values.add(tuple(t[0][0]))
        return l_keywords, l_values

    

