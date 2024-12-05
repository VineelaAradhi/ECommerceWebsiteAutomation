from selenium.webdriver.support.select import Select

from base.BasePage import BasePage


class MyAccountPage(BasePage):

    myAccount_css='[class="dropdown"]'
    logout='Logout'
    btn_continue='Continue'


    def selectMyAccount(self):
        self.clickelement('css',self.myAccount_css)

    def clickOnLogout(self):
        self.clickelement('text',self.logout)
    def continueToLogin(self):
        self.clickelement('text',self.btn_continue)
