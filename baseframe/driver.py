from selenium import webdriver


class Driver:

    def __init__(self, url, wait_time=10, debugger_address=None):
        if debugger_address is None:
            self.driver = webdriver.Chrome()
        else:
            options = webdriver.ChromeOptions()
            options.debugger_address = debugger_address
            self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)
        self.driver.implicitly_wait(wait_time)

    def quit(self):
        self.driver.quit()

    def find_element(self, locator):
        # todo 改造查找元素方法
        pass
