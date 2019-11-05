import requests
import allure


class Request:

    @classmethod
    def request(cls, method, url, **kwargs):
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        r = requests.request(method, url, proxies=proxies, verify=False, **kwargs)
        return r


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.67 Safari/537.36 '
    }
    r = requests.get(url, headers=headers)
    print(r.request.__dict__)
