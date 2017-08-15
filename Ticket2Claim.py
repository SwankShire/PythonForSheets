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
        tb = TextInput(multiline=True)
        btn = Button(text='Search', font_size=14)


        tb.bind(on_text=self.on_text())


        B.add_widget(lbl)
        B.add_widget(tb)
        B.add_widget(btn)


        return B

    def on_text(self, ):
        print('the widget', self.tb, 'have:', self.tb.text)

    def buttonClicked(self,B):
        print("You wrote ", self.tb.text)

if __name__ == '__main__':
    LateDeviceTracker().run()
