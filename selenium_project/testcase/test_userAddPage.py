from appium_project.baseframe import Driver
import time
from selenium_project.pages.contact_page import ContactPage
import allure


class TestUserAddPage:

    def setup_class(self):
        self.url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver = Driver(self.url)
        cookie = {
            'name': 'wwrtx.sid',
            'value': 'A6uLNE3Z_haX8xdtqr5jDZGAUPvGSA0FAtZcqDq0u469SCIn8hUGpRm75S6J18tR'
        }
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    def teardown_class(self):
        self.driver.quit()

    def teardown_method(self):
        if self.driver.current_url != self.url:
            self.driver.get(self.url)

    @allure.title('验证新增用户成功')
    def test_add_user(self):
        time.sleep(2)
        name = 'tester{}'.format(str(time.time()).split('.')[0])
        save_status = ContactPage(self.driver) \
            .go_to_add_user() \
            .add_user(name, name, '{}@qq.com'.format(name)).save_status
        assert save_status is True
