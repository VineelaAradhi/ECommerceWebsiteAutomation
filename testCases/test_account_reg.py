import os
import time
import unittest

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.AccountRegPage import AccountRegPage
from pageObjects.HomePage import HomePage
from utilities.customLogger import CustomLogger
from utilities.randomstring import randomStringGenerator

@pytest.mark.sanity
@pytest.mark.usefixtures("setup")
class AccountRegister(unittest.TestCase):
    log=CustomLogger.getLogger()

    def test_account_reg(self):
        self.log.info('.....test_account_reg started......')
        self.hp=HomePage(self.driver)
        self.hp.select_my_account()
        self.hp.click_on_register()
        self.rp=AccountRegPage(self.driver)
        self.log.info(' Entering the registration details')
        self.rp.enter_firstname('Sujana')
        self.rp.enter_lastname('Talapaga')
        self.email=randomStringGenerator()+'@gmail.com'
        self.rp.enter_email(self.email)
        self.log.info(' '+self.email)
        self.rp.enter_password('123456')
        self.rp.subscribe()
        self.rp.setPrivacyPolicy()
        self.rp.click_continue()
        time.sleep(2)
        self.successMessage=self.rp.getSuccessMessage()
        if self.successMessage=='Your Account Has Been Created!':
            self.log.info(' Account created!....')
            assert True
        else:
            screenshotPath = "../screenshots/" + 'test_account_reg.png'
            self.driver.save_screenshot(screenshotPath)
            assert False


