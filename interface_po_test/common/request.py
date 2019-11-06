import allure
import requests
from interface_po_test.common.utils import Utils


class Request:

    @classmethod
    def request(cls, method, url, **kwargs):
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        rep = requests.request(method, url, proxies=proxies, verify=False, **kwargs)

        # 请求报文
        allure.attach(rep.request.url, 'req_url', allure.attachment_type.URI_LIST)
        allure.attach(Utils.dict_to_json(rep.request.headers), 'req_headers', allure.attachment_type.JSON)
        allure.attach(Utils.dict_to_json(rep.request.body), 'req_body', allure.attachment_type.JSON)

        # 响应报文
        allure.attach(str(rep.status_code), 'status_code', allure.attachment_type.TEXT)
        allure.attach(Utils.dict_to_json(rep.headers), 'rep_hreaders', allure.attachment_type.JSON)
        if rep.headers['Content-Type'].find('json'):
            allure.attach(Utils.dict_to_json(rep.json()), 'rep_body', allure.attachment_type.JSON)

        return rep


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.67 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    print(r.request.__dict__)
