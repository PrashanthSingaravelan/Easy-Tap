from kivymd.uix.screen import MDScreen
import pyperclip as pc
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

class ImagetoTextScreen(MDScreen):
    def return_button(self):
        self.manager.current = 'cam'

    def on_tab_press(self,type):
        self.text = pc.paste()

        if type == "translate":
            print("Translation Takes Place")
            self.translated = GoogleTranslator(source='auto', target='english').translate(self.text)
            print(self.translated)

        elif type == "loud":
            print("loud")
            self.speech = gTTS(text=self.text, lang="en", slow=False)
            self.speech.save("sample.mp3")
            os.system("sample.mp3")

        elif type == "copy":
            print("copy")

        elif type == "share":
            print("share")



