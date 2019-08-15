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
            'value': 'A6uLNE3Z_haX8xdtqr5jDWBo4B6UCy4equm04cfN5haxaRT_W2wu0glm53M78yU-'
        }
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    def teardown_method(self):
        self.driver.refresh()

    @allure.title('验证修改姓名成功')
    def test_001(self):
        edit_result = ContactPage(self.driver).search_user_by_name('testerhome') \
            .go_to_edit_user().edit_name('testerhome是我') \
            .save_edit().get_tips()
        assert edit_result == '保存成功'

    @allure.title('验证置顶成功')
    def test_02(self):
        top_user = ContactPage(self.driver).search_user_by_name('te12121st123').top_user().get_tips()
        assert top_user == '置顶成功'