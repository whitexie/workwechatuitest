from interface_po_test.api.baseapi import BaseApi


class Contacts(BaseApi):

    _create_uri = '/cgi-bin/user/create'


    def create(self):
        pass