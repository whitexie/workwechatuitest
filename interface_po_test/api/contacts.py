from interface_po_test.api.baseapi import BaseApi


class Contacts(BaseApi):

    _create_uri = '/cgi-bin/user/create'

    def create(self, user_id, name, department: list, **kwargs):
        user_dict = {
            'userid': user_id,
            'name': name,
            'department': department
        }
        if kwargs:
            user_dict.update(kwargs)
        self.post(self._create_uri, headers=self.headers, json_object=user_dict)
