# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
import time
import errno

class PDF_Reader():

    def __init__(self):
        pass

    def read(self, p_PDF_file):
        """
        Reads text from pdf using ocr, pdf is converted into images and the read text using tesseract.
        
        Args:
            PDF_file (string): filepathto pdf file
            
        Returns:
            A 3-diamentional array [page][row][column]
        """
        l_t = time.time()
        # Path of the pdf: 
        # PDF_file = "C:/Users/Win10Office2016/Desktop/Python-Proj/NOW-PDF_Reader/Test_Files/test1.pdf" 
        # check to see if file exists if not raise filenotfound exception
        if not os.path.exists(p_PDF_file):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), p_PDF_file)
        ''' 
        Part #1 : Converting PDF to images 
        '''
        l_image_counter = self.convert_pdf_to_image(p_PDF_file)
        ''' 
        Part #2 - Recognizing text from the images using OCR 
        '''
        # Variable to collect data read from PDF.
        l_data = []
        
        # Iterate from 1 to total number of pages 
        for i in range(1, l_image_counter + 1): 
            # Set filename to recognize text from page_n.jpg  
            filename = "page_"+str(i)+".jpg"
            l_data.append(self.Read_images_for_data(filename))           

        # Delete all image files
        # self.clear_image_files(l_image_counter)

        # Print the time taken to read text from pdf.
        print( int(time.time() - l_t ))
        
        return l_data, l_image_counter



 
    def convert_pdf_to_image(self, p_PDF_file):
        """
        converts a pdf file to multiple image files, 1 image file per page.
        For each page, filename will be: 
            => PDF page 1 -> page_1.jpg 
            => PDF page 2 -> page_2.jpg 
            => PDF page 3 -> page_3.jpg 
            
        arg:
            PDF_file: path to pdf file

        Returns: 
            counter of nmber of images created.
        """
        # check to see if file exists if not raise filenotfound exception
        if not os.path.exists(p_PDF_file):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), p_PDF_file)
        # Store all the pages of the PDF in a variable 
        l_pages = convert_from_path(p_PDF_file, 500) 
        # Counter to store images of each page of PDF to image 
        l_image_counter = 1

        # Iterate through all the pages stored above 
        for page in l_pages: 
            # Declaring filename for each page of PDF as JPG 
            filename = "page_"+str(l_image_counter)+".jpg"
            # Save the image of the page in system 
            page.save(filename, 'JPEG') 
            # Increment the counter to update filename 
            l_image_counter = l_image_counter + 1
        # return the number of images(pages) created.
        return l_image_counter - 1




    def Read_images_for_data(self, p_image_file):
        """
        reads the text from an image along with pixel information of each word. 
            
        arg:
            filename

        Returns: 
            text 
        """
        # check to see if file exists if not raise filenotfound exception
        if not os.path.exists(p_image_file):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), p_image_file)

        # Recognize the text as string in image using pytesserct.
        l_text = str((pytesseract.image_to_data(Image.open(p_image_file), config='-c preserve_interword_spaces=0')))

        # Here, basic formatting has been done: 
        # In many PDFs, at line ending, if a word can't 
        # be written fully, a 'hyphen' is added. 
        # The rest of the word is written in the next line 
        # Eg: This is a sample text this word here GeeksF- 
        # orGeeks is half on first line, remaining on next. 
        # To remove this, we replace every '-\n' to ''. 
        # text = text.replace('-\n', '')


        # Data is returned as text, with newline('\n') as seperator of rows and tab('\t') is used as column seperator.
        # Split text into rows using newline.
        l_data_rows = l_text.split('\n')
        # Split text into columns using tab this will create a two diamentional array.
        l_data = [dr.split('\t') for dr in l_data_rows]
        return l_data

    def clear_image_files(self, p_image_counter):
        for i in range(1, p_image_counter + 1): 
            # Set filename to recognize text from page_n.jpg  
            filename = "page_"+str(i)+".jpg"
            if os.path.exists(filename):
                os.remove(filename)