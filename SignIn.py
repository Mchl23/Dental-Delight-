import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup

Window.size= (600,800)

Builder.load_file('SignIn.kv')
class LoginTrue(Popup):
    pass 

class LoginFalse(Popup):
    pass
            
class MyLayout(Widget):
    
    def Modal(self):
        User = 'sdca.itpe02'
        methodusern = self.ids.usern.text
        Password = '@itpe02'
        methodpasn = self.ids.pasn.text
        if (User == methodusern and Password == methodpasn):
            LoginTrue().open()
        else:
            LoginFalse().open()
            
       
    
class registration(App):
    title="SignIn"
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    registration().run()