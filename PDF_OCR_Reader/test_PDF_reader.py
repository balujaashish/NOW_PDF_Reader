import unittest
from PDF_reader import PDF_Reader
import os

class TestPDFReader(unittest.TestCase):
    
    def setUp(self):
        self.x = PDF_Reader()
        self.FilePath = "C:/Users/Win10Office2016/Desktop/Python-Proj/NOW-PDF_Reader/Test_Files/"

    # def test_x(self):
    #     open("page_1.jpg","w+")
    #     x = PDF_Reader()
    #     x.clear_image_files(1)



    def test_convert_pdf_to_image(self):
        count = self.x.convert_pdf_to_image(self.FilePath+"test1.pdf")
        self.assertEqual(count,1)
        self.assertTrue(os.path.exists("page_1.jpg"))
        self.assertRaises(FileNotFoundError,self.x.convert_pdf_to_image,self.FilePath+"njnjn.pdf")
        # tests with 2 page document
        if os.path.exists("page_1.jpg"):
            os.remove("page_1.jpg")
        count = self.x.convert_pdf_to_image(self.FilePath+"test2.pdf")
        self.assertEqual(count,2)
        self.assertTrue(os.path.exists("page_1.jpg"))
        self.assertTrue(os.path.exists("page_2.jpg"))
        
    def test_Read_images_for_data(self):
        data = self.x.Read_images_for_data(self.FilePath+"testImage1.jpg")
        self.assertEqual(data[5][11],'Name:')
        self.assertEqual(data[6][11],'Ashish')
        self.assertEqual(len(data),7)
        self.assertRaises(FileNotFoundError,self.x.convert_pdf_to_image,self.FilePath+"njnjn.pdf")


    def test_Read(self):
        data = self.x.read(self.FilePath+"test2.pdf")
        print(data)
        self.assertEqual(data[0][5][11],'Name:')
        self.assertEqual(data[0][6][11],'Ashish')
        self.assertEqual(data[1][5][11],'Last')
        self.assertEqual(data[1][6][11],'Name:')
        self.assertEqual(data[1][7][11],'Baluja')
        
        self.assertEqual(len(data),2)
        self.assertEqual(len(data[0]),7)
        self.assertEqual(len(data[1]),8)

        self.assertRaises(FileNotFoundError,self.x.read,self.FilePath+"njnjn.pdf")


    # def test_clear_image_files(self):
    #     open("page_1.jpg","w+")
    #     open("page_2.jpg","w+")
    #     self.x.clear_image_files(2)
    #     self.assertEqual(os.path.exists("page_1.jpg"), False)
    #     self.assertEqual(os.path.exists("page_2.jpg"), False)


    def tearDown(self):
        if os.path.exists("page_1.jpg"):
            os.remove("page_1.jpg")
        if os.path.exists("page_2.jpg"):
            os.remove("page_2.jpg")
        if os.path.exists("page_3.jpg"):
            os.remove("page_3.jpg")


if __name__ == "__main__":
    unittest.main()
    # hf = TestPDFReader()
    # hf.test_x()
