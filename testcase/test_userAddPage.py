from baseframe.driver import Driver
from pages.contact_page import ContactPage
import allure


class TestUserAddPage:

    def setup_class(self):
        self.url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver = Driver(self.url, debugger_address='127.0.0.1:9222')

    def teardown_class(self):
        self.driver.quit()

    def teardown_method(self):
        if self.driver.current_url != self.url:
            self.driver.get(self.url)

    @allure.title('验证新增用户成功')
    def test_add_user(self):
        save_status = ContactPage(self.driver) \
            .go_to_add_user() \
            .add_user('te12121st123', 'test1212444', 'tes12321312t222@qq.com').save_status
        assert save_status is True

