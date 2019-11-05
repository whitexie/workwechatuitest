from interface_po_test.common.request import Request


class BaseApi:
    _base_url = 'https://qyapi.weixin.qq.com'
    _corpid = 'ww33643a02c10ca566'
    _contacts_secret = 'HucYaAh4kQcxINjCJ-CU8oswIlN-bGUEpr2ULJQULEw'

    _get_token_path = '/cgi-bin/gettoken'
    _contacts_token = None

    def get_token(self):
        if self._contacts_token:
            return self._contacts_token
        else:
            url = self._base_url + self._get_token_path
            params = {
                'corpid': self._corpid,
                'corpsecret': self._contacts_secret
            }
            r = Request.request('get', url, params=params).json()
            token = r['access_token']
            self._contacts_token = token
            return token

    def post(self, uri, json_object):
        url = self._base_url+uri
        return Request.request('post', url, params={'access_token': self.get_token()}, json=json_object).json()

    def get(self, uri, params):
        url = self._base_url+uri
        param = {'access_token': self.get_token()}
        param.update(params)
        return Request.request('get', url, params=param).json()
