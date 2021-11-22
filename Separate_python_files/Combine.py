from gtts import gTTS 
from deep_translator import GoogleTranslator
import os

''' Should be provided with buttons
English --> 'en' 
French --> 'fr'
China  --> 'zh-CN'
Portuguese --> 'pt'
Spanish --> 'es'
'''

def image_to_text(image):
    #image = cv2.imread('..\images\img_1.avif') ## reading the image
    text_pdf = pytesseract.image_to_pdf_or_hocr('..\converted_documents\doc_1.pdf')  ## storing the text in pdf format
    text_img = pytesseract.image_to_string('..\converted_text\text_1.txt')       ## storing the text in image format
    print("Converted Text : ",text_img)
    #text_to_speech(text_img,'en')

def text_to_speech(text,language):
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("..\converted_audio\sample.mp3")       ## saving the converted speech
    os.system("start ..\converted_audio\sample.mp3")   ## opening the converted speech

def text_translate(text):
    translated = GoogleTranslator(source='auto', target='english').translate(text)
    print("Translated Text : ",translated)

if __name__=='__main__':
    image_to_text()