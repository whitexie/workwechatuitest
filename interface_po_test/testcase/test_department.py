import allure
from interface_po_test.api.department import Department

import random
import time


@allure.feature('部门管理')
class TestDepartment:
    depart = Department()

    @allure.title('获取部门列表')
    def test_search_list(self):
        r = self.depart.search_list()

        assert r['errmsg'] == 'ok'
        assert len(r['department']) > 0

    @allure.title('创建部门')
    def test_create(self):
        name = '子部门%d%d' % (int(time.time()), random.randint(10000, 99999))
        r = self.depart.create(name)
        depart_id = r['id']
        result = self.depart.search_list(depart_id)

        assert result['department'][0]['name'] == name

    @allure.title('删除部门')
    def test_delete(self):
        name = '子部门%d%d' % (int(time.time()), random.randint(10000, 99999))
        r = self.depart.create(name)
        depart_id = r['id']
        assert self.depart.delete(depart_id)['errcode'] == 0
