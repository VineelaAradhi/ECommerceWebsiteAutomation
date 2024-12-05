import configparser
from distutils.command.config import config

config=configparser.RawConfigParser()
config.read('/home/hp/PycharmProjects/EcommercePageObjectModel/configurations/config.ini')

class ReadConfig:
    @staticmethod
    def getemail():
        email=(config.get('commonInfo','email'))
        return email

    @staticmethod
    def getpassword():
        password = (config.get('commonInfo', 'password'))
        return password