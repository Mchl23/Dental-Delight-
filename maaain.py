import os, sys
from kaki.app import App 
from kivy.factory import Factory
from kivy.config import Config
from kivy.resources import resource_add_path, resource_find
from kivy.core.window import Window

from kivymd.app import MDApp
Window.size= (600,800)

class screenManagerApp(App,MDApp):    
    DEBUG = True
    
    KV_FILES = {
        os.path.join(os.getcwd(), "Manager.kv")
        #os.path.join('.', 'logic.screen_manager.kv')
    }

    CLASSES = {"MainLayout": "screenManager"}

    AUTORELOADER_PATHS = [('.', {"recursive": True})]
    
    def build_app(self):
        self.theme_cls.material_style = "M3"    
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.accent_palette= "Teal"
        return Factory.MainLayout()
    


if hasattr(sys, '_MEIPASS'):
    resource_add_path(os.path.join(sys._MEIPASS))
screenManagerApp().run()