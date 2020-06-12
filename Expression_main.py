from PDF_OCR_Reader.extract_information_frm_pdf import Extract_Information_Frm_PDF
from Expression.expression import Expression
from Expression.supporting_data import Supporting_Data


def get(p_expressions, FilePath, p_supporting_data):
    """
        check if any term in list1 aligns with any term in list2.

        Args:
            PDF_Info (PDF_Information class objeact): pdf information extracted.
            p_list1 (list): list of terms that could come from lets say a phrase.
            p_list2 (list): list of terms that could come from lets say a phrase.

        Returns:
            none. updates public property of this class:
                self.alignment_list , self.direction , self.distance
            
    """
    l_expressions, keyword_list = extract_expression_details_expression(p_expressions)
    p_supporting_data[(0, 0, 0,'keywords')] = keyword_list

    pdf_info = get_pdf_info(FilePath, p_supporting_data)
    supporting_data = get_supporting_data(p_supporting_data)
    attributes = get_attributes()

    exp = Expression(pdf_info, supporting_data, attributes)
    for l_exp in l_expressions:
        print('--------------------------------------------------------------------------------------------------------------------')
        print('--------------expression------------')
        print(l_exp[0])
        print('--------------list name------------')
        print(l_exp[1])
        match = exp.findAll(l_exp[0], p_list_name=l_exp[1], p_attribute_name='allowed_terms date')
        print(match)



def tokenize_expression( p_expression, e_sep = ']', s_sep = '['):
        """ 
        splits the expression to individual parts:
            -> Keyword
            -> Seperator
            -> Value Type
        """
        l1 = p_expression.split(e_sep)
        out_put = []
        for t1 in l1:
            t1 = t1.strip()
            if t1:
                l2 = t1.split(s_sep)
                for t2 in l2:
                    t2 = t2.strip()
                    if t2:
                        out_put.append(t2)
        if e_sep == ']':
            if len(out_put) == 3:
                return {'Keyword':out_put[0], 'Separator':out_put[1], 'Value':out_put[2]}
            else:
                return {'Keyword':'', 'Separator':out_put[0], 'Value':out_put[1]}
        else:
            return {'Type':out_put[0], 'Type_value':out_put[1]}


def extract_expression_details_expression(p_expressions):
    print('******************************get expressions details and keyword******************************')

    keyword_list = []
    l_expressions = []
    for expression in p_expressions:
        Exp_tokens = tokenize_expression(expression)
        p_expression = {}
        p_attribute_name = ''
        p_expression['Keyword'] = Exp_tokens['Keyword']
        p_expression['Separator'] = Exp_tokens['Separator']
        p_expression['Value'] = Exp_tokens['Value']
        # get parameter names like list name from expression
        if p_expression['Value'].startswith('List'):
            value_tokens = tokenize_expression(Exp_tokens['Value'], s_sep='(', e_sep=')')
            p_expression['Value'] = value_tokens['Type']
            p_attribute_name = value_tokens['Type_value']
        # print('------------------------p_expression-----------------------------')
        # print(p_expression)
        # print('------------------------p_attribute_name-----------------------------')
        # print(p_attribute_name)
        l_expressions.append([p_expression, p_attribute_name])
        if p_expression['Keyword']:
            keyword_list.append([0,0,0,p_expression['Keyword']])  
    return l_expressions, keyword_list     


def get_pdf_info(FilePath, l_dict):
    distance= 50
    p_currency_distance = 200
    EIFP = Extract_Information_Frm_PDF()
    pdf_info = EIFP.extract_information_frm_PDF(FilePath, l_dict, True, distance, p_currency_distance) 
    return pdf_info


def get_supporting_data(p_supporting_data):
    # ------Supporting_Data----------
    p_allowed_terms = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    p_supporting_data['allowed_terms date'] = p_allowed_terms
    supporting_data = Supporting_Data(p_supporting_data)
    return supporting_data


def get_attributes():
    attributes = {}
    attributes['allowed_terms date'] = 'allowed_terms date'
    return attributes
    


    

if __name__ == "__main__":
    expressions = ['[ORDER NO]=[List(Purchase Order Number)]', '[Amount]=[Currency]', '[QTY]=[Number]', '[Issued on]=[Date]', '[]=[List(Purchase Order Number)]']

    l_dict =  {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'6000567751'],[9829,939,921,'fhc']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']]}

    # FilePath = "C:/Users/Win10Office2016/Desktop/Python-Proj/NOW-PDF_Reader/Test_Files/"
    # FilePath = FilePath+"Order No 6000567751.pdf"


    FilePath = "C:/Users/Win10Office2016/Desktop/test files/ANI/"
    FilePath = FilePath+"Class_Code_Light_Trucks_Long_Distance_Radius_200.pdf"

    # get(expressions, FilePath, l_dict)

    pdf_info = get_pdf_info(FilePath, l_dict)




    # define expression first
    # # keywords = {(0, 0, 0,'keywords'):[]}
    # print('******************************get expressions details and keyword******************************')
    # keyword_list = []
    # # out_put = self.x.findAll(p_expression, p_attribute_name='allowed_terms date', p_list_name='Purchase order number')
    # p_expressions = []
    # for expression in expressions:
    #     # expression = '[]=[List(Purchase Order Number)]'
    #     Exp_tokens = tokenize_expression(expression)
    #     p_expression = {}
    #     p_attribute_name = ''
    #     p_expression['Keyword'] = Exp_tokens['Keyword']
    #     p_expression['Separator'] = Exp_tokens['Separator']
    #     p_expression['Value'] = Exp_tokens['Value']
        
    #     if p_expression['Value'].startswith('List'):
    #         value_tokens = tokenize_expression(Exp_tokens['Value'], s_sep='(', e_sep=')')
    #         p_expression['Value'] = value_tokens['Type']
    #         p_attribute_name = value_tokens['Type_value']

    #     print('------------------------p_expression-----------------------------')
    #     print(p_expression)
    #     print('------------------------p_attribute_name-----------------------------')
    #     print(p_attribute_name)
    #     p_expressions.append([p_expression, p_attribute_name])
    #     if p_expression['Keyword']:
    #         keyword_list.append([0,0,0,p_expression['Keyword']])
        
        
        
    # print('------------------------keyword list-----------------------------')
    # print(keyword_list)
    # p_expressions, keyword_list = extract_expression_details_expression(expressions)
    # l_dict[(0, 0, 0,'keywords')] = keyword_list
    # print('------------------------l_dict list-----------------------------')
    # print(l_dict)

    # # get keywords from expressions:



    # # ------------------------------------------------get pdf_info-----------------------------------------------------------------
    # print('***************************************get pdf_info******************************************')

    # # l_dict =  {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'6000567751'],[9829,939,921,'fhc']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'PART NUMBER']]}

    

    # distance= 50
    # p_currency_distance = 200

    # EIFP = Extract_Information_Frm_PDF()
    # pdf_info = EIFP.extract_information_frm_PDF(FilePath, l_dict, True, distance, p_currency_distance) 

    # pdf_info = get_pdf_info(FilePath, l_dict)
    # print("----------------------------------------------------------")
    # print("--------------------dates---------------------------------")
    # print("----------------------------------------------------------")
    # print(pdf_info.dates)

    # print("----------------------------------------------------------")
    # print("--------------------currency---------------------------------")
    # print("----------------------------------------------------------")
    # print(pdf_info.Currency)

    # print("----------------------------------------------------------")
    # print("--------------------lines---------------------------------")
    # print("----------------------------------------------------------")
    # print(pdf_info.PDF_Lines)

    # print("----------------------------------------------------------")
    # print("--------------------keywords---------------------------------")
    # print("----------------------------------------------------------")
    # print(pdf_info.keywords)

    # print("----------------------------------------------------------")
    # print("--------------------integers---------------------------------")
    # print("----------------------------------------------------------")
    # print(pdf_info.integers)

    # print("----------------------------------------------------------")
    # print("--------------------decimals---------------------------------")
    # print("----------------------------------------------------------")
    # print(pdf_info.decimals)

    print("----------------------------------------------------------")
    print("--------------------clean data---------------------------------")
    print("----------------------------------------------------------")
    for term in pdf_info.rawData[0]:
        print(term)
    # print(pdf_info.cleanData)






    # # extract list of expressions

    # ------Supporting_Data----------
    # p_supporting_data = l_dict
    # p_allowed_terms = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # p_supporting_data['allowed_terms date'] = p_allowed_terms
    # supporting_data = get_supporting_data(l_dict)

    # attributes = get_attributes()

    # exp = Expression(pdf_info, supporting_data, attributes)

    # # # ---------------loop over each expression and extract data----------------

    # for l_exp in p_expressions:
    #     print('--------------expression------------')
    #     print(l_exp[0])
    #     print('--------------list name------------')
    #     print(l_exp[1])
    #     match = exp.findAll(l_exp[0], p_list_name=l_exp[1], p_attribute_name='allowed_terms date')
    #     print(match)

