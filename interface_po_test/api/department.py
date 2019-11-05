from interface_po_test.api.baseapi import BaseApi


class Department(BaseApi):
    _create_uri = '/cgi-bin/department/create'
    _search_list_uri = '/cgi-bin/department/list'
    _delete = '/cgi-bin/department/delete'

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

    def search_list(self, depart_id=None):
        return self.get(self._search_list_uri, params={'id': depart_id})

    def delete(self, depart_id=None):
        return self.get(self._search_list_uri, params={'id': depart_id})
