import requests


class TestCaseDemo:

    def test_testerhome(self):
        url = 'https://testerhome.com/api/v3/topics.json'
        params = {
            'limit': 2
        }
        rep = requests.get(url, params=params)
        assert 'Arlene' == rep.json()['topics'][1]['user']['name']

    def test_xueqiu_search(self):
        url = 'https://xueqiu.com/stock/search.json'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Cookie': 'device_id=24700f9f1986800ab4fcc880530dd0ed; aliyungf_tc=AQAAAOTGXRY/YQUAFgm3c9RY0OWcM+Al; acw_tc=2760827f15709520483665936e798d7d5df765e1672a47048c3f51b14b0625; xq_a_token=d831cd39b53563679545656fba1f4efd8e48faa0; xq_r_token=fd2f0f487c8298cad8e7519f1560abb7a18c589d; u=821570952049723; Hm_lvt_1db88642e346389874251b5a1eded6e3=1569419106,1569504678,1570952051; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1570952072'
        }
        params = {
            'code': 'SOGO',
            'size': 1,
            'page': 1
        }
        rep = requests.get(url, headers=headers, params=params)
        print(rep.content)
        assert 'SOGO' == rep.json()['stocks'][0]['code']