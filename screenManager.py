import os, sys
from kivy.config import Config
Config.set('graphics', 'width', '730')
Config.set('graphics', 'height', '980')
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder 
from kivy.app import App
from kivy.resources import resource_add_path, resource_find
import sqlite3
from datetime import datetime, date, time, timedelta
from kivy.app import App
from kivy.clock import Clock
import datetime 
from kivy.uix.popup import Popup 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.snackbar import BaseSnackbar
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivymd.uix.card import MDCard

class CustomCard(MDCard):
    id = StringProperty(None)
    title = StringProperty(None)
    source = StringProperty(None)
    group = StringProperty(None)
    def assign_texture_from_database(self,dbTexture):
        self.ids.display_image.texture = dbTexture
class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")


class MainLayout(FloatLayout):
    
    def load_cards(self):
        self.ids.scrn1_grid.clear_widgets()
        var_name =CustomCard(id="",title="",source="",group="")
        mdCard = CustomCard(id="1",title="Test",source="f",group="group")
        self.load_cards()
        self.ids.scrn1_grid.add_widget(mdCard)
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)
        self.store = JsonStore("loggedUser.json")
        try:
            if self.store.get('UserInfo')['firstname'] != "":
                self.screen_manager.current = 'dashboard_screen'
        except KeyError:
            {
                "name": "Michaela Palapar",
                "gender": "Female",
                "occupation": "Student"
            }
    def open_icon_snackbar(self):
        snackbar = CustomSnackbar(
            text="This is a sample snackbar error!",
            icon= "close-circle",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x= (Window.width - (dp(10) * 2)) / Window.width,
            bg_color="#B71C1C"
        )
        snackbar.open()
    def assign_user_input(self, input):
        self.ids.userLabel.text = input

    def open_custom_snackbar(self):
        snackbar = Snackbar(text="Yo! this is a custom snackbar!", snackbar_x="10dp", snackbar_y="10dp",size_hint_x= (Window.width - (dp(10) * 2)) / Window.width,bg_color= "pink")
        snackbar.open()
            
            
    
    def slide_left(self, dashboard_screen, left):
        self.ids.screen_manager1.current = dashboard_screen
        self.ids.screen_manager1.transition.direction = left
    def login (self):
        inp_username = self.ids.log_username.text
        inp_password = self.ids.log_password.text
        dbconn = sqlite3.connect("sqlkivy.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        dbcursor = dbconn.cursor()
        dbcursor.execute("SELECT * FROM mstuser WHERE mstuser.username = :var_username and mstuser.password = :var_password",
                         {
                             'var_username' : inp_username,
                             'var_password' : inp_password
                         }
                         )
        records = dbcursor.fetchall()
        if not records:
            print ("No record created")
        else:
            print ("Record exist")
            for user in records:
                print(f"Username:{user[1]}\nFirstName:{user[2]}\nLastName:{user[3]}")
                self.store.put('UserInfo',code=user[0],firstname=user[2],lastname=user[3],username=user[1])
            dbconn.commit()
        
            dbconn.close()
            self.ids.screen_manager1.current = "dashboard_screen"
            self.ids.screen_manager1.transition.direction = "up"
        
    
        
    
#class SetIndex(BoxLayout):
    #def setDate(self, *args):
        #popup = Popup(title='Insert Old Date', content=CalendarWidget(), size_hint=(.9, .5)).open()

            
    def register(self):
        inp_username = self.ids.username.text
        inp_firstname = self.ids.firstname.text
        inp_lastname = self.ids.lastname.text
        inp_email = self.ids.email.text
        inp_password = self.ids.password.text
        
        dbconn = sqlite3.connect("sqlkivy.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        dbcursor = dbconn.cursor()
        dbcursor.execute("INSERT INTO mstuser(username, first_name, last_name, email, password, created_at, updated_at)VALUES(:var_username, :var_firstname, :var_lastname, :var_email, :var_password, :var_created_at, :var_updated_at)",
                         {
                            'var_username' : inp_username,
                            'var_firstname' : inp_firstname,
                            'var_lastname' : inp_lastname,
                            'var_email' : inp_email,
                            'var_password' : inp_password,
                            'var_created_at' : datetime.datetime.now(),
                            'var_updated_at' : datetime.datetime.now(),
                             
                         })
        dbconn.commit()
        dbconn.close()
        self.ids.screen_manager1.current = "login_screen"
        self.ids.screen_manager1.transition.direction = "left"

    


class MainApp(MDApp):
    def build(self):
            self.theme_cls.material_style = "M3"    
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette= "Blue"
            self.theme_cls.accent_palette= "Teal"
            return MainLayout()
     
    
    
   
        
      
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MainApp().run()
