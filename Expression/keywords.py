
class Keywords():
    # extract out keywords from pdf_info

    def __init__(self, PDF_Info, p_supporting_data, p_attributes):
        self.pdf_info = PDF_Info
        self.supporting_data = p_supporting_data
        self.attributes = p_attributes


    def get(self, p_keyword):
        """
        looks for keywords in pdf_info.

        Args:
            p_keyword (string): keyword of expression
            
        Returns:  
            returns a list of term combinations that match keyword
        """
        out_put = self.search_keyword_pdf_info(p_keyword)
        return self.strip_details(out_put)


    def synonyms_keyword(self, p_keyword):
        """ 
        look for synonyms of keyword in supporting data
        """
        pass


    def search_keyword_pdf_info(self, p_keyword):
        """ 
        search keyword in pdf_info.
        """
        out_put = []
        pdf_keywords = []
        for key in self.pdf_info.keywords:
            if key[0] == p_keyword:
                pdf_key = key
                pdf_keywords = self.pdf_info.keywords[key]
        if pdf_keywords:
            for pdf_keyword in pdf_keywords:
                if self.qualify(pdf_key, pdf_keyword):
                    out_put.append(pdf_keyword)
        return out_put




    def qualify(self, p_keyword, p_pdf_keyword):
        """ 
        verify the results found in pdf_info.
        """
        out_put = True
        if len(p_keyword[1]) != len(p_pdf_keyword):
            out_put = False
        return out_put

    def strip_details(self, p_keywords):
        out_put = []
        for keyword in p_keywords:
            s_keyword = []
            s_keyword.append(list(keyword[0]))
            for term in keyword[1:]:
                s_keyword.append(term[0])
            out_put.append(s_keyword)
        return out_put