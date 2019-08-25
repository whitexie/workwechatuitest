
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class SearchPage:
    _search_input = (By.ID, 'search_input_text')
    _name = (By.ID, 'name')
    _search_prompt = (By.ID, 'fl_suggest')

    # search result
    _stock_data = (By.ID, 'add_attention')
    _stock_name = (By.ID, 'stockName')
    _stock_code = (By.ID, 'stockCode')
    _follow = (By.ID, 'follow_btn')
    _followed = (By.ID, 'followed_btn')

    # 添加自选后弹窗
    _md = (By.ID, 'md_buttonDefaultNegative')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search_stock(self, content):
        el = self.driver.find_element(*self._search_input)
        el.send_keys(content)
        self.driver.press_keycode(67)
        elements = self.driver.find_elements(*self._name)
        elements[0].click()
        return self

    def follow_stock_by_index(self, index):
        self.driver.find_elements(*self._follow)[index].click()
        self.driver.find_element(*self._md).click()
        return self.driver.find_elements(*self._followed)[index].text

    def follow_status(self):
        return self.driver.find_elements(*self._stock_data)[0].find_element(*self._follow).text
