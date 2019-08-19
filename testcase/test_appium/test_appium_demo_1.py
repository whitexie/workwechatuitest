from appium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By


class TestXueQiu:

    def login_by_account(self, phone, password):
        self.driver.find_element_by_id('com.xueqiu.android:id/user_profile_icon').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/iv_login_phone').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_login_with_account').click()

        self.driver.find_element_by_id('com.xueqiu.android:id/login_account').send_keys(phone)
        self.driver.find_element_by_id('com.xueqiu.android:id/login_password').send_keys(password)
        self.driver.find_element_by_id('com.xueqiu.android:id/button_next').click()

    def search(self, name, expect):
        self.driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys(name)
        search_list = self.driver.find_elements(By.ID, 'com.xueqiu.android:id/name')
        for item in search_list:
            if item.text == expect:
                item.click()
                break

    def setup_method(self):
        caps = {'platformName': 'Android', 'deviceName': '1d8ce5e', 'appPackage': 'com.xueqiu.android',
                'appActivity': '.view.WelcomeActivityAlias', 'autoGrantPermissions': True}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(15)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize('user, password, mess', [
        ('1852012023', '123456', '手机号码填写错误'),
        ('833@qq.com', '123456', '用户名或密码错误')
    ])
    @allure.title('验证错{user},{password}登陆提示->"{mess}"')
    def test_01(self, user, password, mess):
        self.login_by_account(user, password)
        el = self.driver.find_element_by_id('com.xueqiu.android:id/md_content')
        assert el.text == mess
        self.driver.find_element_by_id('com.xueqiu.android:id/md_buttonDefaultPositive').click()

    @pytest.mark.parametrize('name, expect', [
        ('alibaba', '阿里巴巴'),
        ('xiaomi', '小米集团-W'),
        ('google', '谷歌A')
    ])
    @allure.title('验证搜索{name}的结果为{expect}')
    def test_02(self, name, expect):
        self.search(name, expect)
        result_list = self.driver.find_elements(By.ID, 'com.xueqiu.android:id/stockName')
        assert result_list[0].text == expect

