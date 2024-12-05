import time
import unittest

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtility
from utilities.XLUtility import getRowCount


@pytest.mark.datadriven
@pytest.mark.usefixtures('setup')
class DataDrivenTesting(unittest.TestCase):

    def test_login_ddt(self):
        file = '/home/hp/PycharmProjects/EcommercePageObjectModel/testData/Book 1.xlsx'
        lst_status=[]
        self.hp=HomePage(self.driver)
        self.lp=LoginPage(self.driver)
        self.ap=MyAccountPage(self.driver)
        max_row=XLUtility.getRowCount(file,'Sheet1')
        for r in range(2,max_row+1):
            email=XLUtility.getData(file,"Sheet1",r,1)
            pwd=XLUtility.getData(file,"Sheet1",r,2)
            typeOfData=XLUtility.getData(file,"Sheet1",r,3)

            self.hp.select_my_account()
            self.hp.click_on_login()
            self.lp.sendEmail(email)
            self.lp.sendPassword(pwd)
            self.lp.submitLoginDetails()
            time.sleep(2)
            self.targetpage=self.lp.doMyAccountExists()

            if typeOfData=="Valid":
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.ap.selectMyAccount()
                    self.ap.clickOnLogout()
                    self.ap.continueToLogin()
                else:
                    lst_status.append('Fail')
            elif typeOfData=="Invalid":
                if self.targetpage==True:
                    lst_status.append('Fail')
                    self.ap.selectMyAccount()
                    self.ap.clickOnLogout()
                    self.ap.continueToLogin()
                else:
                    lst_status.append('Pass')

        print(lst_status)

        if "Fail" not in lst_status:
            assert True
        else:
            assert False







