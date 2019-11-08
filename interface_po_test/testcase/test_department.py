import random
import time

import allure

from interface_po_test.api.department import Department


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
        assert r['errmsg'] == 'created'

        depart_id = r['id']
        result = self.depart.search_list(depart_id)

        assert result['errmsg'] == 'ok'
        assert result['department'][0]['name'] == name

    @allure.title('删除部门')
    def test_delete(self):
        name = '子部门%d%d' % (int(time.time()), random.randint(10000, 99999))
        r = self.depart.create(name)
        depart_id = r['id']
        assert self.depart.delete(depart_id)['errcode'] == 0

    @allure.title('更新部门')
    def test_update(self):
        department = self.depart.search_list()['department'][1]
        id = department['id']
        name = '子部门%d%d' % (int(time.time()), random.randint(10000, 99999))
        assert self.depart.update(id, name=name)['errcode'] == 0
        assert self.depart.search_list(id)['department'][0]['name'] == name
