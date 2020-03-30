

class String_Compare():
    
    def __init__(self):
        pass

    def str_compare(self, str1, str2):
        try:
            if str1 == str2: return 1
            elif str1 > str2: return 2
            elif str1 < str2: return 3
        except:
            return 0

    