import requests


class TestWorkWechat:
    url = 'https://qyapi.weixin.qq.com'
    corp_id = 'ww33643a02c10ca566'
    corp_secret = 'praUqju6ZdkbWg0M39SFXdWm7xcK-9SPr5dGJkQVNQI'

    def get_url_format(self, path=None):
        return self.url + path

    def test_get_token(self):
        url = self.get_url_format('/cgi-bin/gettoken')
        params = {
            'corpid': self.corp_id,
            'corpsecret': self.corp_secret
        }
        rep = requests.get(url, params=params)
        rep_json = rep.json()
        assert 'ok' == rep_json['errmsg']
        assert rep_json['access_token'] is not None
        TestWorkWechat.access_token = rep_json['access_token']

    def test_get_department_list(self):
        url = self.get_url_format('/cgi-bin/department/list')

        params = {
            'access_token': TestWorkWechat.access_token
        }

        rep_json = requests.get(url, params=params).json()
        assert 'ok' == rep_json['errmsg']
        print()
        print(rep_json)
