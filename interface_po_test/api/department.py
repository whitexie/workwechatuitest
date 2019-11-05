from interface_po_test.api.baseapi import BaseApi


class Department(BaseApi):
    _create_uri = '/cgi-bin/department/create'
    _search_list_uri = '/cgi-bin/department/list'

    def create(self, name, parentid=1, order=1000, id=None):
        return self.post(self._create_uri,{
            'name': name,
            'parentid': parentid,
            'order': order,
            'id': id
        })

    def update(self):
        pass

    def search_list(self, id=None):
        return self.get(self._search_list_uri, params={'id': id})
