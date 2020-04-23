from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import string


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
            str1 = self.str_prepare(str1)
            str2 = self.str_prepare(str2)
            if str1 == str2: return 1
            elif str1 > str2: return 2
            elif str1 < str2: return 3
        except:
            return 0


    def str_compare_basic(self, str1, str2):
        """
        compare string and return an enum:
            => 1: when two strings are equal
            => 0: when two strings are not equal 

        Args:
            str1 (string): string to be compared.
            str2 (string): string to be compared with.
            
        Returns:
            enum.
        """
        try:
            str1 = str1.strip()
            str2 = str2.strip()
            str1 = str1.lower()
            str2 = str2.lower()
            if str1 == str2: return 1
            else: return 0
        except:
            return 0


    def str_prepare(self, p_str):
        #  trim string
        p_str = p_str.strip()
        # strip punctuation 
        p_str = self.strip_punctuations(p_str)
        #  trim string
        p_str = p_str.strip()
        # cast string to lower case
        p_str = p_str.lower()

        return p_str

    def strip_punctuations(self, p_str):
        table = str.maketrans('', '', string.punctuation)
        return p_str.translate(table)

    
    def prepare_phrase(self, p_text, ml_flag):
        # tokenise phrase
        tokens = word_tokenize(p_text)
        # covert phrase to lower for compare
        words = [word.lower() for word in tokens]
        return words


    def pdf_data_tokenize(self, p_data, term_index, get_term, p_ml_flag):
        out_put = []
        for term in p_data:
            term_tokens = self.prepare_phrase(get_term(term), p_ml_flag)
            if len(term_tokens) > 1:
                term_n = []
                for i,term_token in enumerate(term_tokens):
                    term_n = term.copy()
                    term_n[term_index] = term_token
                    term_n.append(i)
                    # print(term_n)
                    out_put.append(term_n)
            # print(term)
            else: 
                term_n = term.copy()
                term_n.append(0)
                out_put.append(term_n)

        # print(out_put)
        return out_put
    