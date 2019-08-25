from appium import webdriver
from appium.webdriver.webdriver import WebDriver


def get_driver() -> WebDriver:

    caps = {
        'platformName': 'Android',
        'platformVersion': '8.1.0',
        'deviceName': '1d8ce5e',
        'appPackage': 'com.xueqiu.android',
        'appActivity': '.view.WelcomeActivityAlias',
        'autoGrantPermissions': True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=caps)
    driver.implicitly_wait(15)
    return driver
