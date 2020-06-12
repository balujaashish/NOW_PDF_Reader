from PDF_OCR_Reader.PDF_information import PDF_Information

from PDF_OCR_Reader.token_network import Token_Network

import cv2
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import csv

import time

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import sys 
from pdf2image import convert_from_path 
import os 


#read your file C:\Users\Win10Office2016\Desktop\Python-Proj\tests\page_1.jpg
def read_tbl_frm_image(p_file):
    img = cv2.imread(file,0)
    img.shape

    #thresholding the image to a binary image
    # if intensity of pixel is greater than 128 then it will be replaced with black(1) else white(0), thus image is translated to binary
    thresh,img_bin = cv2.threshold(img,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #inverting the image 
    img_bin = 255-img_bin


    # countcol(width) of kernel as 100th of total width
    kernel_len = np.array(img).shape[1]//100
    # Defining a vertical kernel to detect all vertical lines of image 
    ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))
    # Defining a horizontal kernel to detect all horizontal lines of image
    hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))
    # A kernel of 2x2
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

    #Use vertical kernel to detect and save the vertical lines in a jpg
    image_1 = cv2.erode(img_bin, ver_kernel, iterations=3)
    vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=3)


    #Use horizontal kernel to detect and save the horizontal lines in a jpg
    image_2 = cv2.erode(img_bin, hor_kernel, iterations=3)
    horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)


    # Combine horizontal and vertical lines in a new third image, with both having same weight.
    img_vh = cv2.addWeighted(vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)
    #Eroding and thesholding the image
    img_vh = cv2.erode(~img_vh, kernel, iterations=2)
    thresh, img_vh = cv2.threshold(img_vh,128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    bitxor = cv2.bitwise_xor(img,img_vh)
    bitnot = cv2.bitwise_not(bitxor)


    # Detect contours for following box detection
    contours, hierarchy = cv2.findContours(img_vh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    def sort_contours(cnts, method="left-to-right"):
        # initialize the reverse flag and sort index
        reverse = False
        i = 0
        # handle if we need to sort in reverse
        if method == "right-to-left" or method == "bottom-to-top":
            reverse = True
        # handle if we are sorting against the y-coordinate rather than
        # the x-coordinate of the bounding box
        if method == "top-to-bottom" or method == "bottom-to-top":
            i = 1
        # construct the list of bounding boxes and sort them from top to
        # bottom
        boundingBoxes = [cv2.boundingRect(c) for c in cnts]
        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
        key=lambda b:b[1][i], reverse=reverse))
        # return the list of sorted contours and bounding boxes
        return (cnts, boundingBoxes)

    # Sort all the contours by top to bottom.
    contours, boundingBoxes = sort_contours(contours, method="top-to-bottom")

    #Creating a list of heights for all detected boxes
    heights = [boundingBoxes[i][3] for i in range(len(boundingBoxes))]

    #Get mean of heights
    mean = np.mean(heights)

    #Create list box to store all boxes in  
    box = []
    # Get position (x,y), width and height for every contour and show the contour on image
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        # if (w<1000 and h<500):
        image = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        box.append([x,y,w,h])


    #Creating two lists to define row and column in which cell is located
    row=[]
    column=[]
    j=0

    #Sorting the boxes to their respective row and column
    for i in range(len(box)):    
            
        if(i==0):
            column.append(box[i])
            previous=box[i]    
        
        else:
            if(box[i][1]<=previous[1]+mean/2):
                column.append(box[i])
                previous=box[i]            
                
                if(i==len(box)-1):
                    row.append(column)        
                
            else:
                row.append(column)
                column=[]
                previous = box[i]
                column.append(box[i])


    #calculating maximum number of cells
    countcol = 0
    for i in range(len(row)):
        countcol = len(row[i])
        if countcol > countcol:
            countcol = countcol

    #Retrieving the center of each column
    center = [int(row[i][j][0]+row[i][j][2]/2) for j in range(len(row[i])) if row[0]]

    center=np.array(center)
    center.sort()
    #Regarding the distance to the columns center, the boxes are arranged in respective order

    finalboxes = []
    for i in range(len(row)):
        lis=[]
        for k in range(countcol):
            lis.append([])
        for j in range(len(row[i])):
            diff = abs(center-(row[i][j][0]+row[i][j][2]/4))
            minimum = min(diff)
            indexing = list(diff).index(minimum)
            lis[indexing].append(row[i][j])
        finalboxes.append(lis)
    
    boxes = []

    # for i in range(len(finalboxes)):
    #     for j in range(len(finalboxes[i])):
    #         for k in range(len(finalboxes[i][j])):
    #             y,x,w,h = finalboxes[i][j][k][0],finalboxes[i][j][k][1], finalboxes[i][j][k][2],finalboxes[i][j][k][3]
    #             boxes.append([x,y,w,h])
    # print('--------------------boxes--------------------------------')
    # print(boxes)

    #from every single image-based cell/box the strings are extracted via pytesseract and stored in a list
    outer=[]
    out_put = {}
    for i in range(len(finalboxes)):
        for j in range(len(finalboxes[i])):
            inner=''
            if(len(finalboxes[i][j])==0):
                outer.append(' ')
            else:
                for k in range(len(finalboxes[i][j])):
                    y,x,w,h = finalboxes[i][j][k][0],finalboxes[i][j][k][1], finalboxes[i][j][k][2],finalboxes[i][j][k][3]
                    finalimg = bitnot[x:x+h, y:y+w]
                    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
                    border = cv2.copyMakeBorder(finalimg,2,2,2,2, cv2.BORDER_CONSTANT,value=[255,255])

                    resizing = cv2.resize(border, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                    # plotting = plt.imshow(resizing,cmap='gray')
                    # plt.show()
                    
                    dilation = cv2.dilate(resizing, kernel,iterations=1)
                    # plotting = plt.imshow(dilation,cmap='gray')
                    # plt.show()

                    erosion = cv2.erode(dilation, kernel,iterations=2)
                    # plotting = plt.imshow(erosion,cmap='gray')
                    # plt.show()

                    out = pytesseract.image_to_string(erosion)
                    if(len(out)==0):
                        out = pytesseract.image_to_string(erosion, config='--psm 3')
                    
                    # out2 = pytesseract.image_to_data(erosion, config='--psm 3')
                    if out:
                        out_put[(x,y,w,h)] = out

                    # print('-------------out2-------------------')
                    # print(out2)
                    inner = inner +" | "+ out
                outer.append(inner)


    return out_put
    # #Creating a dataframe of the generated OCR list
    # arr = np.array(outer)
    # print('--------------------------------------arr----------------------------')
    # print(arr)
    # dataframe = pd.DataFrame(arr.reshape(len(row), countcol))
    # print(dataframe)
    # data = dataframe.style.set_properties(align="left")
    # #Converting it in a excel-file
    # # data.to_excel("output.xlsx")



def is_box1_inside_box2(p_box1, p_box2):
    # left top width height
    b2_x1, b2_y1 = p_box2[0], p_box2[1]
    b2_x2, b2_y2 = b2_x1 + p_box2[3], b2_y1 + p_box2[2]

    b1_x1, b1_y1 = p_box1[0], p_box1[1]
    b1_x2, b1_y2 = b1_x1 + p_box1[3], b1_y1 + p_box1[2]

    if b2_x1 <= b1_x1 and b2_y1 <= b1_y1 and b2_x2 >= b1_x2 and b2_y2 >= b1_y2:
        return True
    else: 
        return False

# 2830, 1929, 790, 352
def get_cells(p_boxes):
    out_put = []
    for b_s in p_boxes:
        outer = False
        for b_t in p_boxes:
            if b_t != b_s:
                if is_box1_inside_box2(b_t, b_s):
                    outer = True
        if not outer:
            out_put.append(b_s)
    return out_put

def get_terms_in_box(p_box, pdf_info):
    out_put = []
    for term in pdf_info.cleanData:
        term_cord = [pdf_info.get_left(term), pdf_info.get_top(term), pdf_info.get_width(term), pdf_info.get_height(term)]
        if is_box1_inside_box2(term_cord, p_box):
            out_put.append(term)
    return out_put

def get_terms_in_boxes(p_boxes, pdf_info):
    out_put = {}
    for box in p_boxes:
        out_put[tuple(box)] = get_terms_in_box(box, pdf_info)
    return out_put

def get_box_map(p_boxes):
    TN = Token_Network()
    return TN.get_neighbor_map(p_boxes, [], get_top, get_left, get_width, get_height, [])
    

def get_left(e):
    return e[1]

def get_top(e):
    return e[0]

def get_width(e):
    return e[2]

def get_height(e):
    return e[3]

if __name__ == "__main__":

    
    l_t = time.time()
    
    file=r'C:/Users/Win10Office2016/Desktop/Python-Proj/tests/page_1.jpg'
    out_put = read_tbl_frm_image(file)
    for key in out_put:
        print('-------------')
        print(key, out_put[key])

    # ---------------------------------------------------------------------------------------------------------------------------


    #Create list box to store all boxes in  
    box = []
    # Get position (x,y), width and height for every contour and show the contour on image
    for key in out_put:
        box.append(key)
            

    print('-------------------boxes-------------------------')
    print(box)
    print(len(box))


    cells = get_cells(box)
    
    for cell in cells:
        print('----------------------------------cell----------------------')
        print(cell)
        print(out_put[cell])
    print(len(cells))

    # ---------------------------------------------------pdf_info-------------------------------------------------------
    pdf_info = PDF_Information()
    pdf_info.cleanData = [[5, 1, 1, 1, 1, 1, 681, 2770, 33, 25, 96, 'c.'],[5, 1, 1, 1, 1, 2, 732, 2762, 106, 42, 95, 'Long'],[5, 1, 1, 1, 1, 3, 856, 2761, 183, 34, 95, 'Distance'],[5, 1, 1, 1, 1, 4, 1057, 2761, 146, 34, 95, 'Radius'],[5, 1, 2, 1, 1, 1, 3031, 2848, 145, 34, 95, 'Radius'],[5, 1, 2, 1, 1, 2, 3193, 2848, 117, 34, 96, 'Class'],[5, 1, 3, 1, 1, 1, 1441, 2975, 196, 34, 95, 'Business'],[5, 1, 3, 1, 1, 2, 1655, 2975, 78, 34, 96, 'Use'],[5, 1, 3, 1, 1, 3, 2837, 2978, 105, 42, 95, 'Long'],[5, 1, 3, 1, 1, 4, 2960, 2977, 184, 34, 96, 'Distance'],[5, 1, 3, 1, 1, 5, 3160, 2977, 117, 43, 96, '(Over'],[5, 1, 3, 1, 1, 6, 3290, 2977, 73, 34, 96, '200'],[5, 1, 3, 1, 1, 7, 3381, 2977, 123, 43, 94, 'Miles)'],[5, 1, 4, 1, 1, 1, 1528, 3053, 116, 34, 94, 'Class'],[5, 1, 4, 1, 1, 2, 2862, 3055, 167, 43, 95, 'Liability'],[5, 1, 4, 1, 1, 3, 3276, 3055, 115, 43, 95, 'Phys.'],[5, 1, 4, 1, 1, 4, 3410, 3056, 105, 33, 95, 'Dam.'],[5, 1, 4, 1, 2, 1, 2878, 3129, 136, 34, 96, 'Factor'],[5, 1, 4, 1, 2, 2, 3329, 3129, 136, 34, 96, 'Factor'],[5, 1, 5, 1, 1, 1, 1508, 3207, 157, 34, 95, 'Service'],[5, 1, 5, 1, 1, 2, 2033, 3207, 181, 34, 90, 'Non-fleet'],[5, 1, 5, 1, 2, 1, 2076, 3259, 96, 34, 95, 'Fleet'],[5, 1, 5, 2, 1, 1, 731, 3335, 107, 43, 95, 'Light'],[5, 1, 5, 2, 1, 2, 853, 3335, 145, 34, 95, 'Trucks'],[5, 1, 5, 2, 1, 3, 2033, 3337, 181, 34, 90, 'Non-fleet'],[5, 1, 5, 2, 2, 1, 709, 3387, 35, 43, 93, '(0'],[5, 1, 5, 2, 2, 2, 760, 3406, 13, 4, 95, '-'],[5, 1, 5, 2, 2, 3, 791, 3387, 132, 39, 95, '10,000'],[5, 1, 5, 2, 2, 4, 940, 3387, 79, 34, 95, 'Lbs.'],[5, 1, 5, 2, 2, 5, 2076, 3389, 96, 34, 95, 'Fleet'],[5, 1, 5, 3, 1, 1, 786, 3465, 157, 43, 83, 'G.V.W.)'],[5, 1, 5, 3, 1, 2, 1459, 3467, 254, 34, 96, 'Commercial'],[5, 1, 5, 3, 1, 3, 2033, 3467, 181, 34, 87, 'Non-fleet'],[5, 1, 5, 3, 2, 1, 2076, 3519, 96, 34, 95, 'Fleet'],[5, 1, 6, 1, 1, 1, 3020, 3597, 295, 34, 90, 'ZONE-RATED']]

    box_terms = get_terms_in_boxes(cells, pdf_info)
    
    for key in box_terms:
        print('----------------box---terms-------------------------')
        print(key)
        print(out_put[key])
        print(box_terms[key])


    # ---------------------------------------------------------box map--------------------------------------
    box_map = get_box_map(cells)
    for key in box_map:
        print('--------------------------------------------------------box---align-------------------------------------------------')
        print(key)
        print('------------------------------------------------')
        print(out_put[key])
        print('-------------------------------------------------')
        for box in box_map[key]:
            print('---------')
            print(out_put[tuple(box[0])])
            print(box[1])



    print( int(time.time() - l_t ))
