from selenium import webdriver


class Driver:
    """
    对WebDriver的封装类
    """

    def __init__(self, url, wait_time=10, debugger_address=None):
        if debugger_address is None:
            self._driver = webdriver.Chrome()
        else:
            options = webdriver.ChromeOptions()
            options.debugger_address = debugger_address
            self._driver = webdriver.Chrome(options=options)
        self._driver.get(url)
        self._driver.implicitly_wait(wait_time)

    def quit(self):
        self._driver.quit()

    def find_element(self, locator):
        # todo 改造查找元素方法
        return self._driver.find_element(*locator)

    @property
    def current_url(self):
        return self._driver.current_url

    def get(self, url):
        self._driver.get(url=url)

    def execute_script(self, script, *args):
        return self._driver.execute_script(script, *args)

    def add_cookie(self, cookie_dict):
        self._driver.add_cookie(cookie_dict)

    def refresh(self):
        self._driver.refresh()
