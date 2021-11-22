from gtts import gTTS 
import os

'''
English --> 'en' 
French --> 'fr'
China  --> 'zh-CN'
Portuguese --> 'pt'
Spanish --> 'es'
'''

text = "This is Prashanth S following king Mothish"
language = "en"

speech = gTTS(text = text, lang = language, slow = False)
speech.save("converted_audio/sample.mp3")       ## saving the converted speech
os.system("start converted_audio/sample.mp3")   ## opening the converted speech



