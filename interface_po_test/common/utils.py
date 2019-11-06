import json


class Utils:

    @classmethod
    def dict_to_json(cls, dict_obj):
        try:
            return json.dumps(dict(dict_obj), ensure_ascii=False, indent=2)
        except Exception:
            return str(dict_obj)


if __name__ == '__main__':
    dict_object = {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
                   'Connection': 'keep-alive'}
    print(Utils.dict_to_json(dict_object))