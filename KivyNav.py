import os, sys
from kivy.config import Config
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.resources import resource_add_path, resource_find
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
    
Builder.load_file('kivyNav.kv')
class MainLayout(MDBoxLayout):
    dialog = None
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog (
                title="Exit?",
                text = "Confirm Logout?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        font_size= '18sp',
                        on_release= self.close_dialog
            
                    ),
                    MDRaisedButton(
                        text="LOGOUT",
                        text_color= 'white',
                        font_size= '18sp',  
                        on_release= self.close_dialog
                    ),
                ],
            )
        self.dialog.open()
    def close_dialog(self,obj):
        self.dialog.dismiss()
    click= NumericProperty(0)
    def clickspam(self):
        self.click+=1
        if self.click <10:
            self.ids.screen.badge_icon=f'numeric-{self.click}'
    
    def notif(self):
        self.click=0
        self.ids.screen.badge_icon=''
    
        
    def kivytheme(self,kiv):
        if kiv.theme_cls.theme_style == 'Dark':
            kiv.theme_cls.theme_style = 'Light'
            kiv.theme_cls.primary_palette= "Pink"
        else:
            kiv.theme_cls.theme_style = 'Dark'
            kiv.theme_cls.primary_palette= "Purple"
class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty ()


             
class KivyNavigation(MDApp):
    def build(self):
            self.theme_cls.material_style = "M3"    
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette= "Pink"
            self.theme_cls.accent_palette= "Teal"
            return MainLayout()  
      
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    KivyNavigation().run()