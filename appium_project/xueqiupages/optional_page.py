from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from appium_project.xueqiupages.base_page import BasePage


class OptionalPage(BasePage):

    _snb = (By.ID, 'snb_tip_text')
    _search = (By.ID, 'action_search')
    _main = (By.ID, '//*[contains(@text, "雪球") and contains(@resource-id, "tab_name")]')
    _optionals_content = (By.ID, 'content_recycler')
    _optionals = (By.ID, 'row_layout')
    _stock_name = (By.ID, 'portfolio_stockName')

    _delete = (By.XPATH, '//*[@text="删除"]')
    _move_top = (By.XPATH, '//*[@text="置顶"]')

    def __init__(self, driver: WebDriver):
        super(OptionalPage, self).__init__(driver)

        # 取消浮层
        elements = self.driver.find_elements(*self._snb)
        if len(elements) >= 1:
            size = self.driver.get_window_size()
            x, y = size.values()
            TouchAction(driver).press(x=x * 0.5, y=y * 0.5).release().perform()

    def goto_search(self):

        self.driver.find_element(*self._search).click()
        from appium_project.xueqiupages.search_page import SearchPage
        return SearchPage(self.driver)

    def goto_main_page(self):
        self.driver.find_element(*self._main).click()
        from appium_project.xueqiupages.main_page import MainPage
        return MainPage(self.driver)

    def get_optionals(self):
        return self.driver.find_elements(*self._optionals)

    def delete_stock(self, stock_name):
        els = self.driver.find_elements(*self._stock_name)
        for el in els:
            if el.text == stock_name:
                TouchAction(self.driver).long_press(el=el).wait(3000).perform()
                self.driver.find_element(*self._delete).click()
                break
            else:
                raise Exception('该自选股不存在')
        return self
