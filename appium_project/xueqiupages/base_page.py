from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    # 黑名单
    black_list = [
        (By.ID, 'image_cancel'),
    ]

    max = 0

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator) -> WebElement:
        """
        处理浮窗
        :param locator:
        :return:
        """
        try:
            return self.driver.find_element(*locator)
        except Exception as e:
            if BasePage.max > 3:
                raise e

            for black in BasePage.black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()
            return self.find(locator)
