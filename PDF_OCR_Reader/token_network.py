# class to create and manage token network.
# token netwrok is a netwrok of tokens that allign either horizontally or vertically
from Data_cleaner import Data_Cleaner
from String_compare import String_Compare

class Token_Network():

    def __init__(self):
        pass


    def get_neighbor_map(self, p_data, p_indexes, p_get_top, p_get_left, p_get_width, p_get_height, p_get_term):
        """
        creates a dictionary of terms as key and all term that align with that term as value of dictionary.

        Args:
            p_data (list): list of terms with there loction information
            p_indexes (list): list of indexes that contain term location information
            p_get_top (function): returns the distance from top key from term location info.
            p_get_left (function): returns the distance from left key from term location info.
            p_get_width (function): returns the distance from width key from term location info.
            p_get_height (function): returns the distance from height key from term location info.
            p_get_term (function): returns the distance from term key from term location info.
            
        Returns:
            dictionary
        """
        # {[5, 1, 9, 1, 1, 1, 263, 2563, 244, 43, '96', 'Comment']: [[5, 1, 7, 1, 1, 1, 264, 2212, 223, 55, '93', 'Payment'],[5, 1, 7, 1, 2, 1, 264, 2304, 109, 41, '95', 'NET']] } 
        DC = Data_Cleaner()
        p_data = DC.clean_pdf_data(p_data, p_get_term, p_indexes)
        output = self.get_aligned_terms(p_data,p_get_top, p_get_left, p_get_width, p_get_height)
        output = self.sort_by_distance(output, self.get_distance)
        return output

    
    def search_neighbor_map(self, p_data, p_term, p_get_term):
        # function to search neighbor map to get all matching terms
        SC = String_Compare()
        output = {key : p_data[key] for key in p_data if SC.str_compare(p_get_term(key),p_term) == 1}
        return output

    def get_aligned_terms(self,p_data, p_get_top, p_get_left, p_get_width, p_get_height):
        output = {}
        # iterate over each term and get the aligned terms
        for i in range(len(p_data)):
            output[tuple(p_data[i])]=[]
            # for a selected term check all terms see if they align
            for j in range(len(p_data)):
                if i != j:
                    x = self.is_aligned_2d (p_data[i], p_data[j], p_get_left, p_get_top, p_get_width, p_get_height)
                    if x:
                        # if terms align ad it to output dictionary with direction and distance
                        output[tuple(p_data[i])].append([p_data[j],x])  
        return output


    def get_distance(self, e):
        return e[1][1]

    def is_aligned_2d(self, p_list1, p_list2, p_left_key, p_top_key, p_width_key, p_height_key):
        """
        checks if the two terms align verically or horizontally based on the pixel information in list

        Args:
            p_list1 (List): pdf term1 with pixel details
            p_list2 (List): pdf term2 with pixel details
            p_left_key (function): returns the distance from left from term list.
            p_top_key (function): returns the distance from top from term list.
            p_width_key (function): returns the width of term from term list.
            p_height_key (function): returns the height of term from term list.

        Returns:
            direction and distance of term2 from term1
        """
        # check if terms align vertically
        IVA = self.is_align_1D(p_list1, p_list2, p_left_key, p_width_key)
        # check if terms align horizonally
        IHA = self.is_align_1D(p_list1, p_list2, p_top_key, p_height_key)
        if IVA == True:
            # if terms align vertically get direction and distance
            return self.get_vertical_align_direction(p_list1, p_list2, p_top_key, p_height_key)
        elif IHA == True:
            # if terms align vertically get direction and distance
            return self.get_horizontal_align_direction(p_list1, p_list2, p_left_key, p_width_key)
        else: return None

    def get_vertical_align_direction(self, p_list1, p_list2, p_top_key, p_height_key):
        # checks the direction in which the terms are aligned vertically, needs terms to be alligned 
        # we check that then only call this function
        
        # if term1 from top os greater than term2 then term1 is bellow term2 and thus term 2 is in 'up' direction and vice versa
        if p_top_key(p_list1) > p_top_key(p_list2):
            # subtract height to top before calculating distance as we want distance b/n end of term2 and beginning of term1
            distance = p_top_key(p_list1) - p_top_key(p_list2) - p_height_key(p_list2)
            return 'up',distance
        elif p_top_key(p_list1) < p_top_key(p_list2): 
            distance = p_top_key(p_list2) - p_top_key(p_list1) - p_height_key(p_list1)
            return 'down',distance
        else: return ('equal',0)

    def get_horizontal_align_direction(self, p_list1, p_list2, p_left_key, p_width_key):
        # checks the direction in which the terms are aligned horizontally, needs terms to be alligned 
        # we check that then only call this function
        
        # if term1 from left is greater than term2 then term1 is on right of term2 and thus term 2 is in 'right' direction and vice versa
        if p_left_key(p_list1) > p_left_key(p_list2):
            # subtract width to top before calculatinf distance as we want distance b/n end of term2 and beginning of term1
            distance = p_left_key(p_list1) - p_left_key(p_list2) - p_width_key(p_list2)
            return 'left',distance
        elif p_left_key(p_list1) < p_left_key(p_list2):
            distance = p_left_key(p_list2) - p_left_key(p_list1) - p_width_key(p_list1)
            return 'right',distance
        else: return ('equal',0)


    def is_align_coordinates(self, l1, w1, l2, w2):
        # checks that the x coordinates of term overlap at all, if they do partially we will consider 
        # them to be alligned
        l1_start = l1
        # add width to x1 to get the end coodinate for term
        l1_end = l1_start + w1
        l2_start = l2
        l2_end = l2_start + w2
        if l1_start <= l2_end and l2_start <= l1_end:       
            return True
        else: return False

    def is_align_1D(self, p_list1, p_list2, p_left_key, p_width_key):
        # checks that the x coordinates of term in a list overlap at all, 
        # if they do partially we will consider them to be aligned
        return self.is_align_coordinates(p_left_key(p_list1), p_width_key(p_list1), p_left_key(p_list2), p_width_key(p_list2))

    
    def sort_by_distance(self, p_data, p_key):
        # sorts data by distance for each term in Network dictionary
        for l_key in p_data:
            p_data[l_key] = sorted(p_data[l_key],key=p_key)
        return p_data
