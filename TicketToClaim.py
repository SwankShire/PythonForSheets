from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

def repairQlogin(driver):
    driver.get('https://techdefenders.repairq.io/site/login')
    login = driver.find_element_by_class_name('form-control')
    login.send_keys(username, Keys.TAB, password, Keys.TAB, Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER)
    submit = driver.find_element_by_class_name('btn-primary')
    submit.send_keys(Keys.RETURN)
    findTicket(driver)

def findTicket(driver):
    ticket = '121839'

    searchbox = driver.find_element_by_class_name('quickSearch')
    searchbox.send_keys(ticket, Keys.ENTER)

    # i start using requests and beautifulsoup here

    url = driver.page_source
    soup = BeautifulSoup(url, "html.parser")
    soup.prettify()
    #!! its currently taking the bs4 code to the login page
    warrantyStuff = soup.find(id='summary')
    warrantyStuff = warrantyStuff.find_all(class_='pull-right')
    print(warrantyStuff)
    i = 0
    for i in warrantyStuff:
        i = i + 1

        if i == 3: break


    # data = warrantyStuff.find_all('pull-right')
    # for things in data:
    #    print(things.text)
if __name__ == "__main__":

    username = 'n.smith'
    password = '8462'

    driver = webdriver.Chrome()
    repairQlogin(driver)