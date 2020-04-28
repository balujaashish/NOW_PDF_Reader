from String_compare import String_Compare


class Prepare_Data_Keywords():

    def __init__(self):
        pass

    def tokenize_keyword(self, p_KeyWord):
        """
        creates word token and cleans data.

        Args:
            p_KeyWord (string): phrase to be tokenized.
            
        Returns:
            keyword tokens
        """
        SC = String_Compare()
        search_str = SC.prepare_phrase(p_KeyWord, 0)
        search_tokens = []
        for token in search_str:
            # tokenize again just in case terms can be split again
            str_tokens = SC.prepare_phrase(token,0)
            search_tokens = search_tokens + str_tokens
        return search_tokens