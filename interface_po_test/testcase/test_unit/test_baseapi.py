from interface_po_test.api.baseapi import BaseApi


class TestBaseApi:
    api = BaseApi()

    def test_get_token(self):
        assert self.api.get_token() is not None
