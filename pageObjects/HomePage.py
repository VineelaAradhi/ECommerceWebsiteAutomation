import time

from selenium.webdriver.common.by import By

from base.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    my_account='My Account'
    register='Register'
    login='Login'

    def select_my_account(self):
        self.clickelement('text',self.my_account)
            #self.driver.find_element(By.LINK_TEXT,self.my_account).click()
    def click_on_register(self):
        self.clickelement('text',self.register)
        #self.driver.find_element(By.LINK_TEXT, self.register).click()
    def click_on_login(self):
        self.clickelement('text',self.login)
        #self.driver.find_element(By.LINK_TEXT, self.login).click()
