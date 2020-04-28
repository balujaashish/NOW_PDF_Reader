from String_compare import String_Compare
from term_proximity import Term_Proximity
from token_network import Token_Network


class Phrase_Search():
    def __init__(self):
        pass

    def search(self, p_network, p_phrase_tokens, p_get_term, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_distance):
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
        out_put = []
        search_result = self.search_first_term_phrase(p_network, p_phrase_tokens, p_get_term)
        if len(p_phrase_tokens) >1:
            for key in search_result:
                match = self.search_phrase_in_document_network (p_network, key, p_phrase_tokens, p_get_term, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_distance)
                if match:
                    out_put.append(match)
        else:
            for key in search_result:
                out_put.append([key])
        return out_put



    def search_phrase_in_document_network (self, p_data, p_term, p_phrase_tokens, p_get_term, p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_distance):
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
        listTest = []   
        matches = []
        covered = []
        sc = String_Compare()
        TP = Term_Proximity()
        i = 0
        found = True
        while  i < len(p_phrase_tokens)-1 and found == True:
            matches = self.add_to_match(matches, TP.get_all_terms_in_proximity(p_data[p_term], p_get_direction, p_get_distance, p_get_order_key, p_get_order_value, p_term, p_distance))
            if matches:
                for match in matches:
                    if match not in covered:
                        if sc.str_compare_basic(p_get_term(match[0]), p_phrase_tokens[i+1]) == 1:
                            found = True
                            matches.remove(match)
                            covered.append(match)
                            if not listTest:
                                listTest.append(p_term)
                            listTest.append(match) 
                            i = i + 1
                            p_term = tuple(match[0])
                            break  
                        else: 
                            found = False 
            else: return []
                    
        return listTest
    

    def add_to_match(self, p_list, p_term):
        # remove if term already exits and add again, this will get the distance 
        # and direction from last term matched
        # reverse the list of terms to be added so thatnearest term comes first in match
        p_term.reverse()
        for term in p_term:
            for l in p_list:
                if l[0] == term[0]:
                    p_list.remove(l)
            p_list = [term] + p_list
        return p_list

    
    def reverse_list_from_index(self, list1, i):
        if i < len(list1):
            list2 = list1[i:]
            list2.reverse()
            list1[i:] = list2
        return(list1)


    def search_first_term_phrase(self, p_network, p_phrase_tokens, p_get_term):
        TN = Token_Network()
        search_result = TN.search_neighbor_map(p_network, p_phrase_tokens[0], p_get_term)
        return search_result