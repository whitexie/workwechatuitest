import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


def get_driver(config_path) -> WebDriver:
    caps = dict()
    caps['platformName'] = 'Android'
    caps['appPackage'] = 'com.xueqiu.android'
    caps['appActivity'] = '.view.WelcomeActivityAlias'
    caps['autoGrantPermissions'] = True
    with open(config_path, 'r') as data:
        caps.update(yaml.load(data))
    print(caps)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=caps)
    driver.implicitly_wait(15)
    return driver
