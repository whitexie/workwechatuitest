from interface_po_test.api.department import Department
import jsonpath
import random
import time


class TestDepartment:
    depart = Department()

    def test_search_list(self):
        r = self.depart.search_list()

        assert r['errmsg'] == 'ok'
        assert len(r['department']) > 0

    def test_create(self):
        name = '子部门%d%d' % (int(time.time()), random.randint(10000, 99999))
        r = self.depart.create(name)
        depart_id = r['id']
        result = self.depart.search_list(depart_id)

        assert result['department'][0]['name'] == name
