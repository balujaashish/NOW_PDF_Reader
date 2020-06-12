from PDF_OCR_Reader.extract_information_frm_pdf import Extract_Information_Frm_PDF

if __name__ == "__main__":
        
    l_dict =  {(2000010, 838, 8389,'Purchase Order Number'): [[9829,939, 883,'6000567751'],[9829,939,921,'fhc']],(2000011, 839, 8390,'Addresses'):[[9830,940, 884,'BOARDWALKTECH, INC 10050 N. Wolfe Rd. #276 Cupertino , CA 95014 United States'], [9831,941, 885,'Teva Bazel 5 5 Bazel St. 4951033 Petah Tikva Israel']],(2000011, 839, 8390,'keywords'):[[9830,940, 884,'Amount'], [9830,940, 884,'PART NUMBER']]}

    FilePath = "C:/Users/Win10Office2016/Desktop/Python-Proj/NOW-PDF_Reader/Test_Files/"
    FilePath = FilePath+"Order No 6000567751.pdf"

    distance= 50
    p_currency_distance = 200

    EIFP = Extract_Information_Frm_PDF()
    out_put = EIFP.extract_information_frm_PDF(FilePath, l_dict, True, distance, p_currency_distance) 

    print("----------------------------------------------------------")
    print("--------------------dates---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.dates)

    # print("----------------------------------------------------------")
    # print("--------------------currency---------------------------------")
    # print("----------------------------------------------------------")
    # print(out_put.Currency)

    # print("----------------------------------------------------------")
    # print("--------------------lines---------------------------------")
    # print("----------------------------------------------------------")
    # print(out_put.PDF_Lines)

    print("----------------------------------------------------------")
    print("--------------------keywords---------------------------------")
    print("----------------------------------------------------------")
    print(out_put.keywords)

    # print("----------------------------------------------------------")
    # print("--------------------integers---------------------------------")
    # print("----------------------------------------------------------")
    # print(out_put.integers)

    # print("----------------------------------------------------------")
    # print("--------------------decimals---------------------------------")
    # print("----------------------------------------------------------")
    # print(out_put.decimals)

    # print("----------------------------------------------------------")
    # print("--------------------clean data---------------------------------")
    # print("----------------------------------------------------------")
    # print(out_put.cleanData)




