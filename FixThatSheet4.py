
# kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput





def DisplayWelcome():
    lbl1 = Label(text='Welcome!')
    return lbl1




class PythonForSheets(App):

    def build(self):
        self.title = "PythonForSheets"

        return DisplayWelcome()


if __name__ == '__main__':
    PythonForSheets().run()