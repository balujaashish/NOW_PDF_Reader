from operator import itemgetter


class sort_List():
    def __init__(self):
        pass

        
    def sort_2D_list(self, p_list, p_position):
        """
        sort a list or tuple that is 2 dimentional, thus we need a position using which we will sort the list.

        Args:
            p_list (list/tuple): list that needs to be sorted.
            p_position (int): position at which the value sits using which we will sort the array.
            
        Returns:
            sorted List or tuple
        """
        self.p = p_position
        return sorted(p_list,key=self.l_key)

    def l_key(self,e):
        # if key is string covert to lower
        if type(e[self.p-1]) == str:
            return e[self.p-1].lower()
        # handle for int and other types
        else:
            return e[self.p-1]

    
    
