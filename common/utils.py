# coding=utf-8
import json
from collections import OrderedDict
from functools import wraps
from datetime import datetime
from hashlib import md5
import pymysql

import records
from contextlib import contextmanager

from pithy import request


class DB(object):

    def __init__(self, db_url):
        self.db_url = db_url

    def query(self, statement, **params):
        # conn = pymysql.connect(self.db_url)
        conn = self.db_url
        cursor = conn.cursor()
        cursor.execute(statement)
        print(statement)
        # db = records.Database(self.db_url)
        # res = db.query(statement, **params)
        # db.close()
        res_k = cursor.description
        res_v = cursor.fetchall()[0]
        res = {}
        num = 0
        for i in res_v:
            res[res_k[num][0]] = i
            num = num + 1
        cursor.close()
        # conn.close()
        return res

    def update(self, statement, **params):
        # conn = pymysql.connect(self.db_url)
        # conn = pymysql.connect(host="rdsej341u9483k397ae5.mysql.rds.aliyuncs.com", user="data_mock",
        #                        password="data_mock123",
        #                        db="data_mock", port=3306)
        conn = self.db_url
        cursor = conn.cursor()
        print(statement)
        cursor.execute(statement)
        conn.commit()
        cursor.close()
        # conn.close()


def get_md5(s):
    m = md5()
    m.update(s)
    return m.hexdigest()

def response_headers(headers):
    res_headers = {}
    header_list = headers.split('\n')
    # print(header_list)
    for i in header_list:
        print(i)
        if ':' in i:
            print(i.split(':')[0])
            key = i.split(':')[0].strip()
            value = i.split(':')[1].strip()
            if key in ['Content-Length','Host','Date']:
                continue
            else:
                res_headers[key] = value

    return res_headers

if __name__ == '__main__':

    db = DB(pymysql.connect(host="rdsej341u9483k397ae5.mysql.rds.aliyuncs.com",user="data_mock", password="data_mock123",db="data_mock",port=3306))
    db.update('update mock_count_add set count = 50 WHERE usertoken = "Y6ccUGAN4eBJkIxQTA5kq3gXyHMKtjYN" ;')


    header='''
    Host: localhost:5000
    Connection: keep-alive
    Content-Length: 75
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
    Cache-Control: no-cache
    Origin: chrome-extension://fhbjgbiflinjbdggehcddcbncdddomop
    Postman-Token: 1d3f1ce0-c7a1-fb1b-03dd-74d87b7279d2
    Content-Type: application/json
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8


    '''
    print(response_headers(headers=header))