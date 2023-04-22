import kivy
#import App Class functionality located in kivy_venv\Lib\site_packages\kivy\app.py
from kivy.app import App 
#import Label Class functionality in kivy_venv\Lib\site_packages\kivy\uix\label.py
from kivy.uix.label import Label 


class MyApp(App):
    def build(self):
        return Label(text="Hello Kivy"
                    ,font_size=72
                     )

if __name__ == '__main__':
    MyApp().run()

''' 
#---kvtemplate
#    -automatically creates the kivy snippet(Python-kivy-snippet extension is required)

from kivy.app import App


class AppTitle(App):
    def __init__(self, **kwargs):
        super(AppTitle, self).__init__(**kwargs)
        


def main():
    AppTitle().run()


if __name__ == '__main__':
    main()    
'''    