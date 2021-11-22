import pytesseract
import cv2
import os

# Configuring the module
pytesseract.pytesseract.tesseract_cmd = r'C:/Program File/Tesseract-OCR/tesseract.exe'

def image_to_text():
    image = os.open('../images/img_1.avif')          ## reading the image
    flags = os.O_RDWR | os.O_CREAT
    mode = 0o666

    text_img = pytesseract.image_to_string(image,flags,mode)       ## storing the text in image format
    print(text_img)
  
if __name__ == '__main__':
    image_to_text()

#text_pdf = pt.image_to_pdf_or_hocr('..\converted_documents\doc_1.pdf')  ## storing the text in pdf format

