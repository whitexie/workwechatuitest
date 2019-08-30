
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from appium_project.xueqiupages.base_page import BasePage


class SearchPage(BasePage):
    _search_input = (By.ID, 'search_input_text')
    _name = (By.ID, 'name')
    _search_prompt = (By.ID, 'fl_suggest')
    _close_search = (By.ID, 'action_close')

    # search result
    _stock_data = (By.ID, 'add_attention')
    _stock_name = (By.ID, 'stockName')
    _stock_code = (By.ID, 'stockCode')
    _follow = (By.ID, 'follow_btn')
    _followed = (By.ID, 'followed_btn')

    # 添加自选后弹窗
    _md = (By.ID, 'md_buttonDefaultNegative')

    def __init__(self, driver: WebDriver):
        super(SearchPage, self).__init__(driver)

    def _canal_search(self):
        """
        退出搜索页面，返回上一页
        :return:
        """
        self.driver.find_element(*self._close_search).click()
        return self

    def back_to_main_page(self):
        self._canal_search()
        from appium_project.xueqiupages.main_page import MainPage
        return MainPage(self.driver)

    def back_to_optional_page(self):
        self._canal_search()
        from appium_project.xueqiupages.optional_page import OptionalPage
        return OptionalPage(self.driver)

    def search_stock(self, content):
        el = self.driver.find_element(*self._search_input)
        el.send_keys(content)
        self.driver.press_keycode(67)
        elements = self.driver.find_elements(*self._name)
        elements[0].click()
        return self

    def _search_result_list(self):
        return self.driver.find_elements(*self._stock_data)

    def follow_stock_by_index(self, index):
        self.driver.find_elements(*self._follow)[index].click()
        self.driver.find_element(*self._md).click()
        return self.driver.find_elements(*self._followed)[index].text

    def follow_status(self):
        return self._search_result_list()[0].find_element(*self._follow).text

    def followed_status(self):
        return self._search_result_list()[0].find_element(*self._followed).text
