from bs4 import BeautifulSoup
import requests
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import selenium


class LateDeviceTracker(App):
    def build(self):

        return Button(text='Hello world', font_size=14)




if __name__ == '__main__':
    LateDeviceTracker().run()



# r =  requests.get("https://www.repairwatch.com/admin/ops-shipping-outbound.php")

# c = r.content

# soup = BeautifulSoup(c, 'html.parser')
# print(soup.find_all("a"))
# soup = BeautifulSoup(r)
# print(soup.prettify())







