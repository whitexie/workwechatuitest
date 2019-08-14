import allure
import time
from baseframe.driver import Driver
from pages.contact_page import ContactPage


class TestUserEditPage:

    def setup_class(self):
        self.url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver = Driver(self.url)
        cookie = {
            'name': 'wwrtx.sid',
            'value': 'A6uLNE3Z_haX8xdtqr5jDWj078gMG_ltZK4fDZj2p4x1rijMXeN09ywRQm5T3u9-'
        }
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    @allure.title('验证修改姓名成功')
    def test_001(self):
        edit_result = ContactPage(self.driver).search_user_by_name('testerhome') \
            .go_to_edit_user().edit_name('testerhome是我') \
            .save_edit().edit_status
        assert edit_result is True
