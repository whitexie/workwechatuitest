from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class OptionalPage:
    _snb = (By.ID, 'snb_tip_wrapper')

    _search = (By.ID, 'action_search')
    _optionals_content = (By.ID, 'content_recycler')
    _optionals = (By.ID, 'row_layout')
    _stock_name = (By.ID, 'portfolio_stockName')

    _delete = (By.XPATH, '//*[@text="删除"]')
    _move_top = (By.XPATH, '//*[@text="置顶"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

        # 取消浮层
        if self.driver.find_element(*self._snb):
            size = self.driver.get_window_size()
            x, y = size.values()
            TouchAction(driver).press(x=x * 0.5, y=y * 0.5).release().perform()

    def goto_search(self):

        self.driver.find_element(*self._search).click()
        from pages.xueqiupages.search_page import SearchPage
        return SearchPage(self.driver)

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
