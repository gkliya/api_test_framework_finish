# -*- coding:utf-8 -*-
# @Time     :2021/1/18 17:53
# @Author     :liyuan
# @File      :run_method.py
# @Software  :PyCharm
# coding:utf-8
import requests
import json


class RunMethod:

    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res

    # return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        return res

    def run_main(self, method, url, data=None, headers=None):
        res = None
        if method == 'POST':
            res = self.post_main(url, data, headers)
        if method == 'GET':
            res = self.get_main(url, data,headers)
        return res


# return json.dumps(res,ensure_ascii=False)


# return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == '__main__':
    rm = RunMethod()
    url = "http://q.115.com/mapp/"
    data = 'option=1&type=0&to_tid=8044376'
    cookie = "last_video_volume=40; UID=594277654_A1_1555229820; CID=ba51ac4f4f3b65927647ff40cce12e85; SEID=bd4fb4b5dbf73a308fa3a90b779d7d3bb46f818b7e542d347749e0c3b2ed0006c6fda9a3efc814c201e29510366b9fda848db2809ec53f151ed5546a; 115_lang=zh"
    header = {cookie: cookie}
    res = rm.post_main(url=url, data=data, header=header)
    print(res)
