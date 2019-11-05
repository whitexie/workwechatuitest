import requests
from requests import Request


class Request:

    @classmethod
    def request(cls, method, url, **kwargs):
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }

        return requests.request(method, url, proxies=proxies, verify=False, **kwargs)
