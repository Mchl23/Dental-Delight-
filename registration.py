import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup 
from kivy.factory import Factory



Window.size= (600,800)

class Registertrue(Popup):
    pass 

class Registerfalse(Popup):
    pass
            
class MyLayout(Widget):
    checklist = []
    def checkboxFunc(self, instance, checkState, LabelName):
        if(checkState == True):
            self.checklist.append(LabelName)
        else:
            self.checklist.remove(LabelName)
            
    
    def build_app(self):
        return Factory.LayoutClassName()
            
    def Modal(self):
        methoduser = self.ids.user.text
        methodname = self.ids.name.text
        methodemail = self.ids.email.text
        methodpas = self.ids.pas.text
        if (len(self.checklist) == 1 and methodname != '' and methodname != '' and methodemail != '' and methodpas !=''):
            Registertrue().open()
        else:
            Registerfalse().open()
            
       
    
class registration(App):
    title="registration"
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    registration().run()