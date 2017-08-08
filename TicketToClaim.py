from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput



WarrantyProvider = ''
ClaimNum = 0
SerialNum = ''

def repairQlogin(driver):
    driver.get('https://techdefenders.repairq.io/site/login')
    login = driver.find_element_by_class_name('form-control')
    login.send_keys(username, Keys.TAB, password, Keys.TAB, Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER)
    submit = driver.find_element_by_class_name('btn-primary')
    submit.send_keys(Keys.RETURN)
    findTicket(driver)

def findTicket(driver):
    ticket = '118323'

    searchbox = driver.find_element_by_class_name('quickSearch')
    searchbox.send_keys(ticket, Keys.ENTER)

    # i start using beautifulsoup here

    url = driver.page_source
    soup = BeautifulSoup(url, "html.parser")
    soup.prettify()
    #!! its currently taking the bs4 code to the login page
    warrantyStuff = soup.find(id='summary')
    warrantyStuff = warrantyStuff.find_all(class_='pull-right')
    print(warrantyStuff)
    i = 0



    for data in warrantyStuff:
        i = i + 1


        if i == 1:
            WarrantyProvider = data.text
        if i == 2:
            ClaimNum = data.text
        if i == 3:
            SerialNum = data.text
            break
    print("Cell data",WarrantyProvider,ClaimNum,SerialNum)
    repairWatchLogin(driver,WarrantyProvider,ClaimNum,SerialNum)


def repairWatchLogin(driver,WarrantyProvider,ClaimNum,SerialNum):

    driver.execute_script("window.open('https://www.repairwatch.com/login/', 'new_window')")
    driver.switch_to.window(driver.window_handles[1])
    print(driver.page_source)
    login = driver.find_element_by_name('email')
    login.send_keys('nsmith111498@gmail.com',Keys.TAB,'$repair123',Keys.ENTER)
    repairWatchAccountSelect(driver,WarrantyProvider,ClaimNum,SerialNum)
    # code to switch back to other tab
    #driver.switch_to_window(driver.window_handles[0])

def repairWatchAccountSelect(driver,WarrantyProvider,ClaimNum,SerialNum):
    driver.get('https://www.repairwatch.com/admin/view-accounts.php')
    page = driver.current_url
    while driver.current_url == page:
        driver.implicitly_wait(5)

    print('we moved')
    batchDevices(driver,WarrantyProvider,ClaimNum,SerialNum)


def batchDevices(driver,WarrantyProvider,ClaimNum,SerialNum):
    driver.get('https://www.repairwatch.com/admin/view-client-shipments.php')
    SearchBox = driver.find_element_by_class_name('form-control')
    print(ClaimNum)
    SearchBox.send_keys(ClaimNum)
    CheckBox = driver.find_element_by_class_name('ckbx_ship')
    CheckBox.click()

if __name__ == "__main__":

    username = 'n.smith'
    password = '8462'

    driver = webdriver.Chrome()
    repairQlogin(driver)
    repairWatchLogin(driver)

