from interface_po_test.api.baseapi import BaseApi
import allure


class Department(BaseApi):
    _create_uri = '/cgi-bin/department/create'
    _search_list_uri = '/cgi-bin/department/list'
    _delete_uri = '/cgi-bin/department/delete'

    @allure.step('创建部门')
    def create(self, name, parentid=1, order=1000, id=None):
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }
        json_object = {
            'name': name,
            'parentid': parentid,
            'order': order,
            'id': id
        }
        return self.post(self._create_uri, json_object=json_object, headers=headers)

    def update(self):
        pass

    @allure.step('获取部门列表')
    def search_list(self, depart_id=None):
        return self.get(self._search_list_uri, params={'id': depart_id})

    @allure.step('删除部门')
    def delete(self, depart_id=None):
        return self.get(self._delete_uri, params={'id': depart_id})
