from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from appium_project.xueqiupages.base_page import BasePage


class MainPage(BasePage):

    _optional = (By.XPATH, '//*[contains(@text, "自选") and contains(@resource-id, "tab_name")]')
    _search = (By.ID, 'home_search')
    _profile = (By.ID, 'user_profile_icon')
    _topics = (By.ID, 'today_topic_container')

    def goto_optional(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._topics))
        self.driver.find_element(*self._optional).click()
        from appium_project.xueqiupages.optional_page import OptionalPage
        return OptionalPage(self.driver)

    def goto_search(self):
        self.driver.find_element(*self._search).click()
        from appium_project.xueqiupages.search_page import SearchPage
        return SearchPage(self.driver)
