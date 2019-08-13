from baseframe.driver import Driver
class TestUserAddPage:

    def setup_class(self):
        url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver = Driver(url, debugger_address='127.0.0.1:9222')

    def test_add_user(self):
        pass
