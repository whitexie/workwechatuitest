from selenium import webdriver
import time

from pages.contact_page import ContactPage


class TestUserEditPage:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        cookie = {
            'name': 'wwrtx.sid',
            'value': 'A6uLNE3Z_haX8xdtqr5jDTDamG2ZhaWd0Y72F6nsdkO1BPsPdSavnpruK93e6GGJ'
        }
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    def test_001(self):
        ContactPage(self.driver).search_user_by_name('testerhome') \
            .go_to_edit_user().edit_user_info(name='testtesttest')