import pytest

from base.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    email_id='input-email'
    password_id='input-password'
    btn_login='//button[@type="submit"]'
    proceed_to_register='Continue'
    myAccount='Edit your account information'

    def sendEmail(self,mail):
        self.sendData('id',self.email_id,mail)
    def sendPassword(self,pwd):
        self.sendData('id',self.password_id,pwd)
    def submitLoginDetails(self):
        self.clickelement('xpath',self.btn_login)
    def registerAccount(self):
        self.clickelement('text',self.proceed_to_register)
    def doMyAccountExists(self):
        try:
            return self.isElementDisplayed('text',self.myAccount)
        except:
            return False