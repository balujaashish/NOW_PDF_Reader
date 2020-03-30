class Data_Cleaner():
    def __init__(self):
        pass
    def clean(self, p_Data):
        """
        get address for a term in the database. this module searches the hierarchy and the string_value also search the terms in filter cuboid.

        Args:
            term (string): terms to be serched in database (comma seperated).
            filters (int): filter cuboid ids(comma seperated)
            flag_structure_only (int): where to search.
                0 : search hierarchy and string_values.
                1 : search hierarchy only
            
        Returns:
            JSON: address of all matches
        """
        pass




    def remove_blanks(self, p_Data, p_Position):
        """
        For an array remove blanks entries of data.
        Args:
            p_Data (2-D Array): Array of data from which we need to remove entries with Balnks.
            p_Position (int): position in array that needs to be checked for an array.    
        Returns:
            Array with Blank entries removed
        """
        l_Data = []
        [l_Data.append(row) for row in p_Data if row[p_Position-1] != '']
        return l_Data