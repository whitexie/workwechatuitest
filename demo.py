import time

from selenium import webdriver
from baseframe.driver import Driver
from pages.add_user import UserAddPage


def print_v(name):
    print(name.__name__)
    pass


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    # page = ContactPage(driver)
    # page.search_user_by_name('tester home')
    # page.go_to_add_user()
    # page = UserAddPage(driver)
    # contact = page.add_user('`1221`', '13123dd322g221132211222', '123131123221gd212123231@qq.com')
    # assert contact.save_status is True
    # page = UserAddPage(driver)
    # page.add_user('123123112312', '123132131sdfsaf', '131231dsjflsdjl@qq.com')
    # url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
    # driver = Driver(url)
    # time.sleep(5)
    # driver.quit()
    # print(driver)
    # print(UserAddPage.add_user.__name__)
    name = '1234'
    print(print_v.__name__)
