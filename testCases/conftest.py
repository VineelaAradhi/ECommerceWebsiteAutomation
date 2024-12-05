import time
from datetime import datetime
from time import strftime

import pytest
from pytest_metadata.plugin import metadata
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver

from utilities.customLogger import CustomLogger

driver=None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    log=CustomLogger.getLogger()
    log.info(' Launching the application')
    base_url = 'https://demo-opencart.com/'

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.get(base_url)
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver=driver
    yield
    driver.close()


def pytest_configure(config):
    config._metadata['Project Name']='Open Cart'
    config._metadata['Tester'] = 'Vineela'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins', None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath='/home/hp/PycharmProjects/EcommercePageObjectModel/reports/'+datetime.now().strftime('%d-%m-%Y %H-%M-%S')+'.html'


