from deep_translator import GoogleTranslator

text = 'I want to translate this text'
translated = GoogleTranslator(source='auto', target='french').translate(text)

##'மோதிஷ் ஒரு விளையாட்டுப்பிள்ளை'
text = input("Enter the text : ")
translated = GoogleTranslator(source='auto', target='english').translate(text)
print(translated)