from String_compare import String_Compare
from term_proximity import Term_Proximity


class Phrase_Search():
    def __init__(self):
        pass

    def search(self, p_data, p_term, p_phrase_tokens, p_get_term, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_distance, i, listTest = None, matches = None, covered = None ):
        """
        returns a list of tokens that match the phrase tokens.

        Args:
            p_data (dictionary): terms map, dictionary of terms and all terms that align together.
            p_term (list): term around which we are looking for other terms.
            p_phrase_tokens (list): word_token for phrase that we are searching.
            p_get_term (function): returns the term from term information in p_data.
            p_get_direction (function): returns the direction for every entry in p_data.
            p_get_distance (function): returns the distance for every entry in p_data.
            p_get_order_key (function): returns the order of a term in network key(1-D List).
            p_get_order_value (function): returns the order in network value(2-D List, has direction and distance).
            p_distance (int): distance for getting terms in proximity
            i (int): is the index to sart from. set it to 0 as default value.    
            
        Returns:
        
            list of terms that match the phrase tokens.

        """
        if len(p_phrase_tokens) >1:
            out_put = self.search_phrase_in_document_network (p_data, p_term, p_phrase_tokens, p_get_term, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_distance, i, listTest = None, matches = None, covered = None )
            return self.reverse_list_from_index(out_put,1)
        else:
            return [p_term]



    def search_phrase_in_document_network (self, p_data, p_term, p_phrase_tokens, p_get_term, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_distance, i, listTest = None, matches = None, covered = None ):
        """
        returns a list of tokens that match the phrase tokens.

        Args:
            p_data (dictionary): terms map, dictionary of terms and all terms that align together.
            p_term (list): term around which we are looking for other terms.
            p_phrase_tokens (list): word_token for phrase that we are searching.
            p_get_term (function): returns the term from term information in p_data.
            p_get_direction (function): returns the direction for every entry in p_data.
            p_get_distance (function): returns the distance for every entry in p_data.
            p_get_order_key (function): returns the order of a term in network key(1-D List).
            p_get_order_value (function): returns the order in network value(2-D List, has direction and distance).
            p_distance (int): distance for getting terms in proximity
            i (int): is the index to sart from. set it to 0 as default value.    
            
        Returns:
        
            list of terms that match the phrase tokens.

        """
        if(listTest == None):
            listTest = []   
        if (matches == None) :
            matches = []
        if (covered == None) :
            covered = []
        sc = String_Compare()
        TP = Term_Proximity()
        if i < len(p_phrase_tokens)-2:
            matches = self.add_to_match(matches, TP.get_all_terms_in_proximity(p_data[p_term], p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_term, p_distance))
            for match in matches:
                if match not in covered:
                    if sc.str_compare_basic(p_get_term(match[0]), p_phrase_tokens[i+1]) == 1:
                        matches.remove(match)
                        covered.append(match)
                        if not listTest:
                            listTest.append(p_term)
                        if (self.search_phrase_in_document_network(p_data,tuple(match[0]),p_phrase_tokens,p_get_term, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_distance, i+1, listTest, matches, covered)):
                            listTest.append(match)    
        else:
            matches = self.add_to_match(matches, TP.get_all_terms_in_proximity(p_data[p_term], p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_term, p_distance))
            
            for match in matches:
                if i < len(p_phrase_tokens)-1:
                    if match not in covered:
                        if sc.str_compare_basic(p_get_term(match[0]), p_phrase_tokens[i+1]) == 1:
                            covered.append(match)
                            if not listTest:
                                listTest.append(p_term)
                            listTest.append(match)
                            i = i + 1
                    
        return listTest
    

    def add_to_match(self, p_list, p_term):
        p_term.reverse()
        for term in p_term:
            found = False
            for l in p_list:
                if l[0] == term[0]:
                    found = True
            if found == False:
                p_list = [term] + p_list
        return p_list

    
    def reverse_list_from_index(self, list1, i):
        list2 = list1[i:]
        list2.reverse()
        list1[i:] = list2
        return(list1)