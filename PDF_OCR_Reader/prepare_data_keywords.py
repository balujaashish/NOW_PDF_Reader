from String_compare import String_Compare


class Prepare_Data_Keywords():

    def __init__(self):
        pass

    def tokenize_keyword(self, p_KeyWord):
        """
        creates word token and cleans data.

        Args:
            p_KeyWord (string): phrase to be tokenized.
            
        Returns:
            keyword tokens
        """
        SC = String_Compare()
        search_str = SC.prepare_phrase(p_KeyWord, 0)
        search_tokens = []
        for token in search_str:
            # tokenize again just in case terms can be split again
            str_tokens = SC.prepare_phrase(token,0)
            search_tokens = search_tokens + str_tokens
        return search_tokens
    
    def tokenize_keywords_dictionary(self, p_dictionary):
        """
        for vocab in keyword lists, we tokenize each keyword. this will be used in intersecting list.

        Args:
            p_dictionary (dictionary): dictionary of keywords, where keyword list name is the key.
            
        Returns:
            dictionary where key is keyword and value is tokenises term list.
            eg:{'fhc': ['fhc'], 'AE10071871': ['ae10071871'], 'Purchase Order Number': ['purchase', 'order', 'number']}
        """
        out_put = {}
        l_vocab = self.get_vocab(p_dictionary, self.get_term, self.get_key_term)
        for term in l_vocab:
            out_put[term] = self.tokenize_keyword(term)
        return out_put
        

    def get_vocab(self, p_dictionary, p_get_term, p_get_key_term):
        """
        get vocab in keyword lists(list of unique keywords)

        Args:
            p_dictionary (dictionary): dictionary of keywords, where keyword list name is the key.
            p_get_term (function): returns term from keywords list in value.
            p_get_key_term (function): returns term from keyword list name in key.

        Returns:
            list of unique keywords
            eg:{'AE10071871', 'fhc', 'Purchase Order Number'}
        """
        out_put = {}
        out_put = set()
        for key in p_dictionary:
            key_term = p_get_key_term(key)
            out_put.add(key_term)
            for Key_Word in p_dictionary[key]:
                term = p_get_key_term(Key_Word)
                out_put.add(term)
        if not out_put:
            out_put = {}
        return out_put


    def get_term(self, e):
        return e[3]

    def get_key_term(self, e):
        return e[3]
