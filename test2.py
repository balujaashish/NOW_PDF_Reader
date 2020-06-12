import pytesseract
from PIL import Image 

# p_image_file = 'C:/Users/Win10Office2016/Desktop/Python-Proj/NOW-PDF_Reader/page_1.jpg'
# l_text = str((pytesseract.image_to_string(Image.open(p_image_file))))
import requests 
import io

image_name = 'C:/Users/Win10Office2016/Desktop/Python-Proj/NOW-PDF_Reader/page_1.jpg'
text = pytesseract.image_to_data(Image.open(image_name) )


print(text)