# 处理接口的执行方法

import json
import requests


# local_url = 'http://127.0.0.1:8000/login/' imooc_url = 'http://coding.imooc.com/api/cate' data = { "apiname":
# "cate", "cid": 0, "secrect":
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
# .eyJ1bmlxdWUiOiI1MDUxNTQwIiwianRpIjoiMjc5OWUyMTNhOWY2NTJhNWJlMTE5MzU0MmUzODQwNDUiLCJkZXZpY2UiOiJtb2JpbGUifQ
# .EYHnj9qoAGX32SDiGhGj36FuU_4MY42TGrBASnfbJ7c", "timestamp": "1554213141535", "token":
# "17f5148f2d2ca10bdbb850dd0ab2171a", "uid": "5051540", }

class RunMethod:
    # def __init__(self, url, method, data=None):
    #     self.result = self.run_main(url, method, data)

    def send_post(self, url, data, header=None):
        if header:
            res = requests.post(url=url, data=data, headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def send_get(self, url, data=None, header=None):
        if header:
            res = requests.get(url=url, data=data, headers=header).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res

    def test_api(self, url, method, data=None, header=None):
        result = None
        if method.upper() == 'POST':
            result = self.send_post(url, data, header)
        if method.upper() == 'GET':
            result = self.send_get(url, data, header)
        return json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)


# if __name__ == '__main__':
#     urls = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
#     datas = {
#         'cart': '11'
#     }
#     run = RunMain(urls, 'post', datas)
#     print(run.result)
