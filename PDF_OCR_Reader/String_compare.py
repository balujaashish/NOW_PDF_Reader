

class String_Compare():
    
    def __init__(self):
        pass

    def str_compare(self, str1, str2):
        """
        compare string and return an enum:
            => 1: when two strings are equal
            => 2: when str1 > str2
            => 3: when str1 < str2
            => 0: when they are not string and cant be compared.
            it takes care of numbers and special char too as long as they are in string form. 

        Args:
            str1 (string): string to be compared.
            str2 (string): string to be compared with.
            
        Returns:
            enum.
        """
        try:
            if str1 == str2: return 1
            elif str1 > str2: return 2
            elif str1 < str2: return 3
        except:
            return 0

    