
# kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class WelcomeScreen(GridLayout):


    def DisplayWelcome(self):
        lbl1 = Label(text='helloworld')
        return lbl1



class PythonForSheets(App):

    def build(self):
        self.title = "PythonForSheets"

        return WelcomeScreen()


if __name__ == '__main__':
    PythonForSheets().run()