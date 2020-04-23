import string


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


    def clean_pdf_data(self, p_data, get_key, indexes):
        """
        cleans data read from pdf:
            =>converts integer in string to int
            => removes blank entries

        Args:
            p_data (2-D Array): pdf data in 2-D array
            get_key (function): function to return term for each iterable
            indexes (list): Array of indexes that need to be converted from string to int.
            
        Returns:
            2D-Array: with clean data
        """
        p_data = self.convert_string_to_int_at_indexes(p_data, indexes)
        p_data = self.remove_blanks(p_data, get_key)
        return p_data




    def remove_blanks(self, p_Data, get_key):
        """
        For an array remove blanks entries of data.
        Args:
            p_Data (2-D Array): Array of data from which we need to remove entries with Balnks.
            p_Position (int): position in array that needs to be checked for an array.    
        Returns:
            Array with Blank entries removed
        """
        l_Data = []
        [l_Data.append(row) for row in p_Data if get_key(row).strip() != '']
        return l_Data




    def convert_string_to_int_at_indexes(self, p_data, p_indexes):
        """
        when pytesserect returns pixel information in strings these need to be converted to
        int for correct comparison.
        Args:
            p_Data (2-D Array): Array of data which was read from pdf usinf pytesserect.
            p_indexes (list): indexes at which string needs to be converted to int.    
        Returns:
            Array with string converted to int at indexes
        """
        # iterater for first 1st dimension of 2-d array.
        for i in range(len(p_data)):
            # iterate over each index in indexes and convert string to int
            try:
                for j in p_indexes:
                    # checkinf string for integer before converting to avoid exception
                    if p_data[i][j].isdigit():
                        p_data[i][j] = int(p_data[i][j])
            except:
                continue
        return p_data


    def is_punctuation(self, term):
        """
        checks if a string is punctuation only:eg 
           -> 'bw,' is not punctuation, 
           -> ',' is punctuation

        Args:
            term (string): term that needs to be checked.    
        Returns:
            boolean
        """
        if term in string.punctuation:
            return True
        else:
            return False

    def is_ignore_term(self, term):
        """
        Checks if a string is to be ignored for comparison eg if it is just a punctuation or empty string
        Args:
            term (string): term that needs to be checked.    
        Returns:
            boolean
        """
        term = term.strip()
        out_put = self.is_punctuation(term)
        return out_put