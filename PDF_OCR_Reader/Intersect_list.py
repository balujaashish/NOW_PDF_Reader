from Search_list import Search_List

class Intersect_List():

    def __init__(self):
        pass

    def Intersect_2_lists(self, p_list1, p_position1, p_list2, p_position2):
        """
        intersect a list with a sorted list, iterate over the list and call binary_search for each term.
        
        Args:
            p_list1 (List 2-D): 2-D sorted list.
            p_position (int): position of terms in p_list1 2-D array(second dimension).
            p_list2 (List 2-D): the lists we want to intersect with p_list1. 
            p_position2(queue): position of terms in p_list2 2-D array(second dimension).
   
        Returns:
            list with the intersected term appended as the first term in 3d array.
        """
        l_SL = Search_List()
        out_put = []
        for term in p_list2:
            l_result = l_SL.binary_search(p_list1, p_position1, term[p_position2-1])
            if l_result:
                out_put.append([term] + l_result )
        return out_put