from String_compare import String_Compare


class Search_List():
    def __init__(self):
        self.SC = String_Compare()

    def binary_search(self, p_list, p_position, p_term):        
        p_position = p_position-1
        p_first, p_found_keyWords, p_found = 0, [], False
        p_last = len(p_list)-1
        # for binary search to work the list has to be sorted
        while( p_first<=p_last and p_found == False):
            # check if the mid value is what we are looking for
            mid = (p_first + p_last)//2
            if self.SC.str_compare(p_list[mid][p_position], p_term) == 1:
                # add the found terms in PDF document to p_found_keyWords
                p_found_keyWords = self.search_term_around_index(p_list, p_position+1, p_term, mid)
                p_found = True
            else:
                # check if term we are searching for will fall in first half or second half of sorted list,
                # reset mid accordingly
                if self.SC.str_compare(p_term, p_list[mid][p_position]) == 3:
                    # term is in first half of list
                    p_last = mid - 1
                else:
                    # term is in last half of list
                    p_first = mid + 1    
        return p_found_keyWords

 


    def search_term_around_index(self, p_list, p_position, p_term, p_index):
        """
        In a sorted array look for p_term aound index p_index.

        Args:
            p_list (List 2-D): 2-D sorted list.
            p_position (int): position of terms in a 2-D array(second dimension).
            p_term (string): term we are searching.
            p_index (int): look for term around this index
            
        Returns:
            2-D list of term occurances in p_list
        """
        try: 
            return_list = []
            # search terms occurances before index
            return_list = self.search_term_before_index(p_list, p_position, p_term, p_index)
            # append the term around which we look for similar term
            return_list.append(p_list[p_index])
            # search terms occurances after index
            return_list = return_list + self.search_term_after_index(p_list, p_position, p_term, p_index)
        except: 
            # in case of an error we dont want to stop processing so just return a blank.
            return []
        return return_list


    def search_term_before_index(self, p_list, p_position, p_term, p_index):
        """
        In a sorted array look for p_term before index p_index.

        Args:
            p_list (List 2-D): 2-D sorted list.
            p_position (int): position of terms in a 2-D array(second dimension).
            p_term (string): term we are searching.
            p_index (int): look for term before this index
            
        Returns:
            2-D list of term occurances in p_list
        """
        # passed positions start from 1 and list use zero based indexing thus subtract 1 from possition
        p_position = p_position -1
        found_keys, found = [], True
        # find all term before p_position
        while (p_index > 0 and found == True):
            # start search from index -1 and keep searching  for the term 
            p_index = p_index - 1
            if self.SC.str_compare(p_list[p_index][p_position], p_term) == 1:
                # if term found add to found_keys
                found_keys.append(p_list[p_index])
            else: found = False
        # since we go from index to left the order is not correct in result thus we reverse it.
        found_keys.reverse()
        return found_keys




    def search_term_after_index(self, p_list, p_position, p_term, p_index):
        """
        In a sorted array look for p_term after index p_index.

        Args:
            p_list (List 2-D): 2-D sorted list.
            p_position (int): position of terms in a 2-D array(second dimension).
            p_term (string): term we are searching.
            p_index (int): look for term after this index
            
        Returns:
            2-D list of term occurances in p_list
        """
        # passed positions start from 1 and list use zero based indexing thus subtract 1 from possition
        p_position = p_position -1
        found_keys, found = [], True
        end = len(p_list)-1
        # find all term after p_position
        while (p_index < end and found == True):
            # start search from index +1 and keep searching  for the term 
            p_index = p_index + 1
            if self.SC.str_compare(p_list[p_index][p_position], p_term) == 1:
                # if term found add to found_keys
                found_keys.append(p_list[p_index])
            else: found = False
            
        return found_keys
        