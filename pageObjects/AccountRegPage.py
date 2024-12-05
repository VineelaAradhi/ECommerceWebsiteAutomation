from selenium.webdriver.common.by import By

from base.BasePage import BasePage


class AccountRegPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # By default, xpath is being used

    firstname='//input[@name="firstname"]'
    lastname='//input[@name="lastname"]'
    email='//input[@name="email"]'
    password='//input[@name="password"]'
    chk_subscribe_css='#input-newsletter'
    chk_agree_css='[name="agree"]'
    btn_continue_css='[type="submit"]'
    account_created_message='//div[@id="content"]/h1'


    def enter_firstname(self,fname):
        self.sendData('xpath',self.firstname,fname)
        #self.driver.find_element(By.XPATH,self.firstname).send_keys(fname)
    def enter_lastname(self,lname):
        self.sendData('xpath', self.lastname, lname)
        #self.driver.find_element(By.XPATH,self.lastname).send_keys(lname)
    def enter_email(self,mail):
        self.sendData('xpath', self.email, mail)
        #self.driver.find_element(By.XPATH,self.email).send_keys(mail)
    def enter_password(self,pwd):
        self.sendData('xpath', self.password, pwd)
        #self.driver.find_element(By.XPATH,self.password).send_keys(pwd)
    def subscribe(self):
        self.clickelement('css',self.chk_subscribe_css)
        #self.driver.find_element(By.CSS_SELECTOR,self.chk_subscribe_css).click()
    def setPrivacyPolicy(self):
        self.clickelement('css', self.chk_agree_css)
        #self.driver.find_element(By.CSS_SELECTOR,self.chk_agree_css).click()
    def click_continue(self):
        self.clickelement('css',self.btn_continue_css)
        #self.driver.find_element(By.CSS_SELECTOR,self.btn_continue_css).click()
    def getSuccessMessage(self):
        try:
            message=self.gettext('xpath',self.account_created_message)
            return message
        except:
            None