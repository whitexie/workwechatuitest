import os
import allure
from interface_po_test.common.request import Request


class BaseApi:
    _base_url = 'https://qyapi.weixin.qq.com'
    _corpid = 'ww33643a02c10ca566'
    _contacts_secret = 'HucYaAh4kQcxINjCJ-CU8oswIlN-bGUEpr2ULJQULEw'

    _get_token_path = '/cgi-bin/gettoken'

    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }

    @allure.step('获取token')
    def get_access_token(self):
        url = self._base_url + self._get_token_path
        params = {
            'corpid': self._corpid,
            'corpsecret': self._contacts_secret
        }
        r = Request.request('get', url, params=params).json()
        return r['access_token']

    def get_token(self):
        if os.environ.get('access_token'):
            return os.environ.get('access_token')
        else:
            token = self.get_access_token()
            os.environ['access_token'] = token
            return token

    def post(self, uri, json_object, **kwargs):
        url = self._base_url+uri
        params = {'access_token': self.get_token()}
        return Request.request('post', url, params=params, json=json_object, **kwargs).json()

    def get(self, uri, params):
        url = self._base_url+uri
        param = {'access_token': self.get_token()}
        param.update(params)
        return Request.request('get', url, params=param).json()


if __name__ == '__main__':
    api = BaseApi()
    print(api.get_token())
    print(api.get_token())