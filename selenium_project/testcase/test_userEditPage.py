import allure
import time

import pytest

from appium_project.baseframe import Driver
from selenium_project.pages.contact_page import ContactPage


class TestUserEditPage:

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

    @allure.title('验证禁用员工成功-{}')
    @pytest.mark.parametrize('name', [('tester1565852805',), ('testerhome750960',)])
    def test_03(self, name):
        tips = ContactPage(self.driver).search_user_by_name(name).disable_user().get_tips()
        assert tips == '禁用成功'

    @allure.title('验证启用员工成功-{}')
    @pytest.mark.parametrize('name', [('tester1565852805',), ('testerhome750960',)])
    def test_04(self, name):
        tips = ContactPage(self.driver).search_user_by_name(name).enable_user().get_tips()
        assert tips == '启用成功'
