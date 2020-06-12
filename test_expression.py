import unittest
from Expression.expression import Expression
import z_test_data
from Expression.supporting_data import Supporting_Data


class testExpressionNumbers(unittest.TestCase):

    def setUp(self):
        self.PDF_Info = z_test_data.PDF_Info
        p_supporting_data = {(2000010, 838, 8389,'Purchase order number'): [[9829,939, 883,'6000567751'],[9829,939,921,'February 20, 2020']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'ORDER NO']]}
        supporting_data = Supporting_Data(p_supporting_data)
        self.supporting_data = supporting_data
        self.attributes = {}
        self.x = Expression(self.PDF_Info, self.supporting_data, self.attributes)



    # def test_tokenize_expression(self):
    #     pass

    # def test_initialize_objects(self):
    #     pass

    def test_keyword_pdf_info(self):
        out_put = self.x.keyword_pdf_info('QTY')
        print(out_put)
        print('-------------------')

    def test_get_expression_currency(self):
        p_key_word = ['Amount', [[[5, 1, 7, 1, 1, 3, 3460, 1338, 356, 55, 94, 'AMOUNT', 0]], [[5, 1, 16, 1, 1, 7, 2836, 4285, 274, 47, 95, 'AMOUNT', 0]], [[5, 1, 4, 1, 1, 2, 3402, 100848, 356, 55, 96, 'AMOUNT', 0]]]]
        p_allowed_terms = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        self.x.supporting_data.data['allowed_terms date'] = p_allowed_terms
        self.x.attributes['allowed_terms date'] = 'allowed_terms date'
        out_put = self.x.get_expression_currency(p_key_word, 'allowed_terms date')
        # print(out_put)
        for o in out_put:
            print('------------------')
            print(o)

    def test_get_expression_dates(self):
        l_keywords = ['Issued on',[[[5, 1, 4, 1, 1, 1, 454, 973, 203, 53, 95, 'Issued', 0], [5, 1, 4, 1, 1, 2, 685, 986, 74, 40, 96, 'on', 0]]]]
        p_allowed_terms = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        self.x.supporting_data.data['allowed_terms date'] = p_allowed_terms
        self.x.attributes['allowed_terms date'] = 'allowed_terms date'
        out_put = self.x.get_expression_dates(l_keywords,'allowed_terms date')
        print(out_put)

    def test_get_expression_numbers(self):
        l_keywords = ['QTY', [[[5, 1, 16, 1, 1, 4, 1779, 4285, 125, 50, 89, 'QTY', 0]]]]
        p_allowed_terms = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        self.x.supporting_data.data['allowed_terms date'] = p_allowed_terms
        self.x.attributes['allowed_terms date'] = 'allowed_terms date'
        out_put = self.x.get_expression_numbers(l_keywords, 'allowed_terms date')
        print(out_put)


    def test_get_expression_lists(self):
        l_keywords = ['ORDER NO',[[[5, 1, 3, 1, 1, 1, 452, 852, 389, 81, 95, 'ORDER', 0], [5, 1, 3, 1, 1, 2, 881, 852, 179, 81, 93, 'no', 0]]]]
        l_list_name = 'Purchase order number'
        p_allowed_terms = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        self.x.supporting_data.data['allowed_terms date'] = p_allowed_terms
        self.x.attributes['allowed_terms date'] = 'allowed_terms date'
        out_put = self.x.get_expression_lists(l_keywords, l_list_name, 'allowed_terms date')
        print('-------------------------keyword list--------------------------------------------')
        print(out_put)
        # for o in out_put:
        #     print('------------------------')
        #     print(o)
        print('----------------------------no keyword list-----------------------------------------')
        l_keywords = []
        l_list_name = 'Purchase order number'
        out_put = self.x.get_expression_lists(l_keywords, l_list_name)
        print(out_put)


    def test_get_expression_match(self):
        p_allowed_terms = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        self.x.supporting_data.data['allowed_terms date'] = p_allowed_terms
        self.x.attributes['allowed_terms date'] = 'allowed_terms date'
        out_put = self.x.get_expression_match(p_value='Currency', p_keyword='Amount', p_attribute_name='allowed_terms date')
        print('----------------currency-----------------------')
        print(out_put)
        out_put = self.x.get_expression_match(p_value='Number', p_keyword='QTY', p_attribute_name='allowed_terms date')
        print('----------------number-----------------------')
        print(out_put)
        out_put = self.x.get_expression_match(p_value='Date', p_keyword='Issued on', p_attribute_name='allowed_terms date')
        print('----------------date-----------------------')
        print(out_put)
        # # # -----------------------list--------------------------
        out_put = self.x.get_expression_match(p_value='List', p_keyword='ORDER NO', p_list_name='Purchase order number',p_attribute_name='allowed_terms date')
        print('----------------list with name-----------------------')
        print(out_put)
        out_put = self.x.get_expression_match(p_value='List', p_list_name='Purchase order number', p_attribute_name='allowed_terms date')
        # print(out_put)
        print('----------------list with no name-----------------------')
        print(out_put)
        # for o in out_put:
        #     print('--------------------------------------------')
        #     print(o)

    def test_extract_expression_match(self):
        l_match = [['Amount', '$10,000.00', [[[[5, 1, 7, 1, 1, 3, 3460, 1338, 356, 55, 94, 'AMOUNT', 0], [[[[5, 1, 8, 1, 1, 3, 3100, 1420, 480, 90, 95, '$', 0], ('down', 27)], []], [[[5, 1, 8, 1, 1, 3, 3100, 1420, 480, 90, 95, '10,000.00', 1], ('down', 27)], []]]]], {'right': 0, 'down': 2, 'equal': 0}, {'min': 27, 'max': 27}, [[5, 1, 8, 1, 1, 3, 3100, 1420, 480, 90, 95, '$10,000.00']], [[5, 1, 7, 1, 1, 3, 3460, 1338, 356, 55, 94, 'AMOUNT', 0]]]], ['Amount', '$10,000.00', [[[[5, 1, 16, 1, 1, 7, 2836, 4285, 274, 47, 95, 'AMOUNT', 0], [[[[5, 1, 16, 1, 4, 8, 2809, 4548, 299, 60, 90, '$', 0], ('down', 216)], []], [[[5, 1, 16, 1, 4, 8, 2809, 4548, 299, 60, 90, '10,000.00', 1], ('down', 216)], []]]]], {'right': 0, 'down': 2, 'equal': 0}, {'min': 216, 'max': 216}, [[5, 1, 16, 1, 4, 8, 2809, 4548, 299, 60, 90, '$10,000.00']], [[5, 1, 16, 1, 1, 7, 2836, 4285, 274, 47, 95, 'AMOUNT', 0]]]], ['Amount', '$10,000.00', [[[[5, 1, 4, 1, 1, 2, 3402, 100848, 356, 55, 96, 'AMOUNT', 0], [[[[5, 1, 4, 1, 2, 1, 3042, 100930, 480, 90, 95, '$', 0], ('down', 27)], []], [[[5, 1, 4, 1, 2, 1, 3042, 100930, 480, 90, 95, '10,000.00', 1], ('down', 27)], []]]]], {'right': 0, 'down': 2, 'equal': 0}, {'min': 27, 'max': 27}, [[5, 1, 4, 1, 2, 1, 3042, 100930, 480, 90, 95, '$10,000.00']], [[5, 1, 4, 1, 1, 2, 3402, 100848, 356, 55, 96, 'AMOUNT', 0]]]]]

        out_put = self.x.extract_expression_match(l_match)
        print(out_put)

    
    def test_findAll(self):
        p_allowed_terms = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        self.x.supporting_data.data['allowed_terms date'] = p_allowed_terms
        self.x.attributes['allowed_terms date'] = 'allowed_terms date'
        p_expression = {}

        p_expression['Keyword'] = 'Amount'
        p_expression['Separator'] = '='
        p_expression['Value'] = 'Currency'
        out_put = self.x.findAll(p_expression, p_attribute_name='allowed_terms date')
        print('----------------currency-----------------------')
        print(out_put)

        p_expression['Keyword'] = 'QTY'
        p_expression['Separator'] = '='
        p_expression['Value'] = 'Number'
        out_put = self.x.findAll(p_expression, p_attribute_name='allowed_terms date')
        print('----------------number-----------------------')
        print(out_put)

        p_expression['Keyword'] = 'Issued on'
        p_expression['Separator'] = '='
        p_expression['Value'] = 'Date'
        out_put = self.x.findAll(p_expression, p_attribute_name='allowed_terms date')
        print('----------------date-----------------------')
        print(out_put)

        # # # -----------------------list--------------------------
        p_expression['Keyword'] = 'ORDER NO'
        p_expression['Separator'] = '='
        p_expression['Value'] = 'List'
        out_put = self.x.findAll(p_expression, p_attribute_name='allowed_terms date', p_list_name='Purchase order number')
        print('----------------list with name-----------------------')
        print(out_put)

        p_expression['Keyword'] = ''
        p_expression['Separator'] = '='
        p_expression['Value'] = 'List'
        out_put = self.x.findAll(p_expression, p_attribute_name='allowed_terms date', p_list_name='Purchase order number')
        print('----------------list with no name-----------------------')
        print(out_put)
        # for o in out_put:
        #     print('--------------------------------------------')
        #     print(o)

if __name__ == "__main__":
    # unittest.main()
    TEN = testExpressionNumbers()
    TEN.setUp()
    TEN.test_findAll()
