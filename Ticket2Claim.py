from bs4 import BeautifulSoup
import requests
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class LateDeviceTracker(App):
    ScannedList = [5]
    def build(self):
        B = BoxLayout()

        lbl = Label(text=str(LateDeviceTracker.ScannedList))
        self.tb = TextInput(text='test',multiline=True)
        btn = Button(text='Search', font_size=14)

        btn.bind(on_press=self.buttonClicked)
        self.tb.bind(on_enter=self.textInput)


        B.add_widget(lbl)
        B.add_widget(self.tb)
        B.add_widget(btn)


        return B

    def textInput(self,):
        print('the widget', self.tb, 'have:', self.tb.text)

    def buttonClicked(self,B):
        print("You wrote ", self.tb.text)

if __name__ == '__main__':
    LateDeviceTracker().run()
