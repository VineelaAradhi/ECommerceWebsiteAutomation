from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def waitforelement(self,locatortype,locatorvalue,timeout=5):
        element=None
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait=WebDriverWait(self.driver,timeout, poll_frequency=.2, ignored_exceptions=errors)
        if locatortype=='xpath':
            element=wait.until(lambda x:x.find_element(By.XPATH,locatorvalue))
        elif locatortype=='css':
            element=wait.until(lambda x:x.find_element(By.CSS_SELECTOR,locatorvalue))
        elif locatortype=='text':
            element=wait.until(lambda x:x.find_element(By.LINK_TEXT,locatorvalue))
        elif locatortype=='name':
            element=wait.until(lambda x:x.find_element(By.NAME,locatorvalue))
        elif locatortype=='class':
            element=wait.until(lambda x:x.find_element(By.CLASS_NAME,locatorvalue))
        elif locatortype=='id':
            element=wait.until(lambda x:x.find_element(By.ID,locatorvalue))
        return element
    def clickelement(self,locatortype,locatorvalue):
        element=self.waitforelement(locatortype,locatorvalue)
        element.click()
    def sendData(self,locatortype,locatorvalue,data):
        element=self.waitforelement(locatortype,locatorvalue)
        element.send_keys(data)
    def gettext(self,locatortype,locatorvalue):
        element = self.waitforelement(locatortype, locatorvalue)
        txt=element.text
        return txt
    def isElementDisplayed(self,locatortype, locatorvalue):
        element=self.waitforelement(locatortype, locatorvalue)
        return element.is_displayed()

