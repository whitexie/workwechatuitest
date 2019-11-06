import json


class Utils:

    @classmethod
    def dict_to_json(cls, dict_obj):
        if isinstance(dict_obj, bytes):
            return json.dumps(str(dict_obj, encoding='utf-8'), ensure_ascii=False, indent=2)
        elif isinstance(dict_obj, dict):
            return json.dumps(dict_obj, ensure_ascii=False, indent=2)
        else:
            return str(dict_obj)


if __name__ == '__main__':
    dict_object = {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
                   'Connection': 'keep-alive'}
    print(Utils.dict_to_json(dict_object))