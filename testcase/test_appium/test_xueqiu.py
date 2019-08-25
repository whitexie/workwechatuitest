from appium.webdriver.webdriver import WebDriver

from baseframe.remotedriver import get_driver
import allure

from pages.xueqiupages.main_page import MainPage

"""
    20190818作业
    点击自选，添加股票，判断股票添加成功
    再次添加股票，添加股票的按钮要变成“已添加”
    删除已经添加的股票，再次搜索股票，股票的按钮变成“加自选”
    注意“自选”菜单，可能会动态浮动
"""


class TestXueQiu:

    def setup_class(self):
        pass

    @allure.title('点击自选，添加股票，判断股票添加成功')
    def test_01(self):
        assert MainPage().goto_optional().goto_search() \
                   .search_stock('alibaba') \
                   .follow_stock_by_index(0) == '已添加'

    @allure.title('搜索已添加的自选股，显示已添加')
    def test_02(self):
        assert MainPage().goto_search().search_stock('alibaba').followed_status() == '已添加'

    @allure.title('删除已经添加的股票，再次搜索股票，股票的按钮变成“加自选”')
    def test_03(self):
        assert MainPage().goto_optional().delete_stock('阿里巴巴').goto_search().search_stock('alibaba') \
            .follow_status() == '加自选'
