# coding=utf-8
from pithy import request

from common.utils import sign


class Demo(object):
    def __init__(self):
        self.base_url = 'http://gateway.test.apitops.com'


    @sign()
    @request(url='/oauth/Authorization/Login', method='post')
    def loign(self,loginName,password):
        aaa={
            'b':1
        }
        data = {'agent': 'android',
                'appcode': 'app_broker',
                'loginName': loginName,
                'password': password}
        headers={
            'a':'1'
        }
        return {'data': data,'headers' :headers,'params':aaa}


if __name__ == '__main__':
    d = Demo()
    d.loign().to_json()