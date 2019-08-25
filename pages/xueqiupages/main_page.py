from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    _optional = (By.XPATH, '//*[contains(@text, "自选") and contains(@resource-id, "tab_name")]')
    _search = (By.ID, 'home_search')
    _profile = (By.ID, 'user_profile_icon')
    _topics = (By.ID, 'today_topic_container')

    def __init__(self):
        caps = dict()
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '8.1.0'
        caps['deviceName'] = '1d8ce5e'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['autoGrantPermissions'] = True
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_capabilities=caps)
        self.driver.implicitly_wait(15)

    def goto_optional(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._topics))
        self.driver.find_element(*self._optional).click()
        from pages.xueqiupages.optional_page import OptionalPage
        return OptionalPage(self.driver)

    def goto_search(self):
        self.driver.find_element(*self._search).click()
        from pages.xueqiupages.search_page import SearchPage
        return SearchPage(self.driver)
