from Expression.separator import Separator
from Expression.keywords import Keywords
from Expression.expression_currency import Expression_Currency
from Expression.expression_dates import Expression_Dates
from Expression.expression_list import Expression_List
from Expression.expression_numbers import Expression_Numbers
from Expression.expression_qualify import Expression_Qualify
import re

class Expression():
    # class to resolve an expression in form of key-value pair: 
    # search for terms that occur together where pattern of expression matches with terms in pdf

        
    def __init__(self, PDF_Info, p_supporting_data, p_attributes):
        self.PDF_Info = PDF_Info
        self.supporting_data = p_supporting_data
        self.attributes = p_attributes
        self.keyword = Keywords(self.PDF_Info, self.supporting_data, self.attributes)
        self.Expression_Currency = Expression_Currency(self.PDF_Info, self.supporting_data, self.attributes)
        self.Expression_Dates = Expression_Dates(self.PDF_Info, self.supporting_data, self.attributes)
        self.Expression_List = Expression_List(self.PDF_Info, self.supporting_data, self.attributes)
        self.Expression_Numbers = Expression_Numbers(self.PDF_Info, self.supporting_data, self.attributes)
        self.Expression_Qualify = Expression_Qualify(self.PDF_Info, self.supporting_data, self.attributes)
        self.seperators = Separator()

    def findAll(self, p_expression, p_attribute_name='', p_list_name=''):
        """
        returns key-value pairs that matches the pattern of expression.

        Args:
            p_expression (dictionary): 
            p_supporting_data (dictionary): contains master data, synonyms..etc.
            PDF_Info (PDF_Information): information extracted from pdf by PDF_OCR_Reader.
            p_attributes (list): atributes that will qualify/verify the results.    
            
        Returns:
        
            list of terms combination that match the expression.

        """
        l_Keyword = p_expression['Keyword']
        l_Separator = p_expression['Separator']
        l_Value = p_expression['Value']
        expression_match = self.get_expression_match(l_Value, p_attribute_name=p_attribute_name,p_keyword=l_Keyword, p_list_name=p_list_name)
        if l_Keyword:
            return self.extract_expression_match(expression_match)
        else:
            return expression_match

    def extract_expression_match(self, p_expression_match):
        out_put = []
        for match in p_expression_match:
            out_put.append([match[0], match[1], match[2][3], match[2][4]])
        return out_put
        


    

    def initialize_objects(self, PDF_Info, p_supporting_data, p_attributes):
        """ 
        based on value type this initiallize the correct class object: date, currency, list, decimal.
        returns he class object
        """
        pass

    def get_expression_match(self, p_value, p_attribute_name = '', p_keyword = '', p_list_name = ''):
        l_keyword_list=[]
        if p_keyword:
            l_keyword_list = self.keyword_pdf_info(p_keyword)
        if p_value.startswith('Currency'):
            l_expression_currency =  self.get_expression_currency(l_keyword_list, p_attribute_name)
            return l_expression_currency
        elif p_value.startswith('Date'):
            l_expression_dates =  self.get_expression_dates(l_keyword_list, p_attribute_name)
            return l_expression_dates
        elif p_value.startswith('Number'):
            l_expression_numbers =  self.get_expression_numbers(l_keyword_list, p_attribute_name)
            return l_expression_numbers
        elif p_value.startswith('List'):
            # l_list_name re.search(r"\(([A-Za-z0-9_]+)\)", s)
            # l_list_name = l_list_name.group(1))
            l_expression_lists = self.get_expression_lists(l_keyword_list, p_list_name, p_attribute_name)
            return l_expression_lists


    def keyword_pdf_info(self, p_keyword):
        return [p_keyword, self.keyword.get(p_keyword)]
    

    def get_expression_currency(self, p_keyword_list, p_attribute_name):
        currency_match = self.Expression_Currency.get(p_keyword_list)
        return self.Expression_Qualify.qualify(currency_match, p_attribute_name)

    
    def get_expression_dates(self, p_keyword_list, p_attribute_name):
        date_match = self.Expression_Dates.get(p_keyword_list)
        return self.Expression_Qualify.qualify(date_match, p_attribute_name)

    
    def get_expression_numbers(self, p_keyword_list, p_attribute_name):
        numbers_match = self.Expression_Numbers.get(p_keyword_list)
        return self.Expression_Qualify.qualify(numbers_match, p_attribute_name)


    def get_expression_lists(self, p_keyword_list, p_list_name, p_attribute_name =''):
        list_match = self.Expression_List.get(p_list_name, p_keyword_list)
        if p_keyword_list:
            return self.Expression_Qualify.qualify(list_match, p_attribute_name)
        else:
            return list_match



    
    