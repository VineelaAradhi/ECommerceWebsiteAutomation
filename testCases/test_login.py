import time
import unittest

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities.customLogger import CustomLogger
from utilities.readProperties import ReadConfig

@pytest.mark.sanity
@pytest.mark.usefixtures('setup')
class Login(unittest.TestCase):
    def test_login(self):
        self.email = ReadConfig.getemail()
        self.password = ReadConfig.getpassword()
        self.log = CustomLogger.getLogger()
        self.hp=HomePage(self.driver)
        self.hp.select_my_account()
        self.hp.click_on_login()
        self.log.info(' Navigated to the Login Page')
        self.lp=LoginPage(self.driver)
        self.lp.sendEmail('abcxyz1234@gmail.com')
        self.log.info(' Entered the email')
        self.lp.sendPassword('test1234')
        self.log.info(' Entered the password')
        self.lp.submitLoginDetails()
        self.log.info(' Login button clicked')
        if self.lp.doMyAccountExists():
            self.log.info(' Login successful')
            assert True
        else:
            screenshotPath = "../screenshots/" + 'test_login.png'
            self.driver.save_screenshot(screenshotPath)
            assert False
