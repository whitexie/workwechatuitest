from appium import webdriver
from appium.webdriver.webdriver import WebDriver


def get_driver() -> WebDriver:
    caps = dict()
    caps['platformName'] = 'Android'
    caps['platformVersion'] = '8.0.0'
    caps['deviceName'] = 'DLQ0215C13000724'
    caps['appPackage'] = 'com.xueqiu.android'
    caps['appActivity'] = '.view.WelcomeActivityAlias'
    caps['autoGrantPermissions'] = True
    driver = webdriver.Remote('http://mbjvr8.natappfree.cc/wd/hub', desired_capabilities=caps)
    driver.implicitly_wait(15)
    return driver
