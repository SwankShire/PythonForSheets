from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class TicketToClaim(App):
    WarrantyProvider = ''
    ClaimNum = 0
    SerialNum = ''

    RpqUsername = 'n.smith'
    RpqPassword = '8462'


    driver = webdriver.Chrome()

    ClaimList =[]
    ScannedList = []
    def build(self):
        B = BoxLayout()

        self.lbl = Label(text='')
        self.tb = TextInput(text='test',multiline=False)
        btn = Button(text='Add', font_size=14)
        self.btnAccounts = Button(text='Account', font_size=15)
        self.btnSubmit = Button(text='Submit', font_size=18)

        self.btnAccounts.bind(on_press=self.selectAccount)
        btn.bind(on_press=self.btnClick)
        self.btnSubmit.bind(on_press=self.submit)

        B.add_widget(self.lbl)
        B.add_widget(self.tb)
        B.add_widget(btn)
        #B.add_widget(self.btnAccounts)
        B.add_widget(self.btnSubmit)

        return B







    def btnClick(self,a):
        print("You wrote ", self.tb.text)
        if self.tb.text == '':
            self.tb.text = '123'
        self.ScannedList.append(self.tb.text)
        self.tb.text = ''

        self.lbl.text = str(self.ScannedList)


    def submit(self,B):
        TicketToClaim.repairQlogin(self)
        i = 0
        for i in self.ScannedList:
            TicketToClaim.findTicket(self, self.driver,i)
        TicketToClaim.repairWatchLogin(self, 1)

    def repairQlogin(self):
        TicketToClaim.driver.get('https://techdefenders.repairq.io/site/login')
        login = TicketToClaim.driver.find_element_by_class_name('form-control')
        login.send_keys(TicketToClaim.RpqUsername, Keys.TAB, TicketToClaim.RpqPassword, Keys.TAB, Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER)
        submit = TicketToClaim.driver.find_element_by_class_name('btn-primary')
        submit.send_keys(Keys.RETURN)
        # findTicket(TicketToClaim.driver)


    def findTicket(self,driver, ticket):


        searchbox = driver.find_element_by_class_name('quickSearch')
        searchbox.send_keys(ticket, Keys.ENTER)

        # i start using beautifulsoup here

        url = driver.page_source
        soup = BeautifulSoup(url, "html.parser")
        soup.prettify()
        # !! its currently taking the bs4 code to the login page
        warrantyStuff = soup.find(id='summary')
        warrantyStuff = warrantyStuff.find_all(class_='pull-right')
        # print(warrantyStuff)
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
        print("Cell data",'Warranty Provider =', WarrantyProvider, 'Claim number =', ClaimNum,'Serial number =', SerialNum)
        TicketToClaim.ClaimList.append(ClaimNum)

    def repairWatchLogin(self, obj):


        self.driver.execute_script("window.open('https://www.repairwatch.com/login/', 'new_window')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        # print(self.driver.page_source)
        login = self.driver.find_element_by_name('email')
        login.send_keys('nsmith111498@gmail.com', Keys.TAB, '$repair123', Keys.ENTER)
        TicketToClaim.selectAccount(self)
        # code to switch back to other tab
        # self.driver.switch_to.window(self.driver.window_handles[0])
    def selectAccount(self):
        self.driver.get('https://www.repairwatch.com/admin/view-accounts.php')
        self.driver.implicitly_wait(5)
        page = self.driver.current_url
        while self.driver.current_url == 'https://www.repairwatch.com/admin/view-accounts.php':
            self.driver.implicitly_wait(5)


        print('we moved')
        TicketToClaim.batchDevices(self)

    def batchDevices(self):
        self.driver.get('https://www.repairwatch.com/admin/view-client-shipments.php')
        print(TicketToClaim.ClaimList)

        i = 0
        for claim in TicketToClaim.ClaimList:
            SearchBox = self.driver.find_element_by_class_name('form-control')
            print('adding this to batch', claim)
            SearchBox.clear()
            self.driver.implicitly_wait(1)
            SearchBox.send_keys(claim)
            CheckBox = self.driver.find_element_by_class_name('ckbx_ship')
            CheckBox.click()
if __name__ == '__main__':
    TicketToClaim().run()

