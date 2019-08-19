from appium import webdriver


class Driver:
    __instance = None

    def __init__(self):
        caps = {
            'platformName': 'Android',
            'platformVersion': '8.0.0',
            'deviceName': 'DLQ0215C13000724',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'autoGrantPermissions': True
        }
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=caps)
        self._driver.implicitly_wait(15)
