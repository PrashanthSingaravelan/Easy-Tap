from kivy.uix.screenmanager import ScreenManager
from Screens.CameraScreen.camera_screen import CameraScreen
from Screens.HomeScreen.home_screen import HomeScreen
from Screens.LoginScreen.login_screen import LoginScreen
from Screens.ImagetoTextScreen.image_to_text import ImagetoTextScreen
from Screens.TranslateScreen.translate_text import TranslateScreen
from Screens.PronounceScreen.pronounce_text import PronounceScreen
from Screens.ToolScreen.tool_screen import ToolScreen

class ManagerScreens(ScreenManager):
    sm = ScreenManager()
    sm.add_widget(LoginScreen(name='log'))
    sm.add_widget(HomeScreen(name='home'))
    sm.add_widget(CameraScreen(name='cam'))
    sm.add_widget(ImagetoTextScreen(name='imaget'))
    sm.add_widget(TranslateScreen(name='tt'))
    sm.add_widget(PronounceScreen(name='pt'))
    sm.add_widget(ToolScreen(name='tool'))

