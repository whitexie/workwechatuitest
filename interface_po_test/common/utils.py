import json
import time
import random
import allure
from requests.structures import CaseInsensitiveDict


class Utils:

    @classmethod
    def format_json(cls, object_json):
        if isinstance(object_json, CaseInsensitiveDict):
            return json.dumps(dict(object_json), ensure_ascii=False, indent=2)
        elif isinstance(object_json, dict):
            return json.dumps(object_json, ensure_ascii=False, indent=2)

    @classmethod
    def print_http(cls, rep):

        # 请求报文
        allure.attach(rep.request.url, 'req_url', allure.attachment_type.URI_LIST)
        allure.attach(cls.format_json(rep.request.headers), 'req_headers', allure.attachment_type.JSON)
        if rep.request.body:
            body = str(rep.request.body, encoding='utf-8')
            allure.attach(body, 'req_body', allure.attachment_type.JSON)

        # 响应报文
        allure.attach(str(rep.status_code), 'status_code', allure.attachment_type.TEXT)
        allure.attach(cls.format_json(rep.headers), 'rep_hreaders', allure.attachment_type.JSON)
        if rep.headers['Content-Type'].find('json'):
            allure.attach(cls.format_json(rep.json()), 'rep_body', allure.attachment_type.JSON)

    @classmethod
    def build_user(cls):
        """
        返回一个9位数的字符串
        :return:
        """
        return 'test_' + str(random.randint(1000, 9999))


if __name__ == '__main__':
    print(Utils.build_user())
