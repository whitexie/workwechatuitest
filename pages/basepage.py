from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def click(self, locator: set, by_js=False):
        el = self._driver.find_element(*locator)
        if by_js:
            self._driver.execute_script('arguments[0].click();', el)
        else:
            el.click()
        return self

    def send_content(self, locator: set, content, is_clear=True):
        el = self._driver.find_element(*locator)
        if is_clear:
            el.clear()
        el.send_keys(content)

    def find(self, locator):
        el: WebElement = WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return el
