import json
from collections import OrderedDict
from functools import wraps
import datetime
from hashlib import md5
import pymysql

import records
from contextlib import contextmanager
from pithy import request


class DateFormat(object):
    def date_now(self):
        GMT_FORMAT = '%Y-%m-%d 00:00:00'
        date_now = datetime.datetime.now().strftime(GMT_FORMAT)
        return date_now

    def time_now(self):
        GMT_FORMAT = '%Y-%m-%d %H:%M:%S'

        time_now = datetime.datetime.now().strftime(GMT_FORMAT)
        return time_now
    def time_add(self,seconds):
        now = datetime.datetime.now()
        time = datetime.timedelta(seconds=seconds)
        time_add = now - time
        GMT_FORMAT = '%Y-%m-%d %H:%M:%S'
        time_add = (time_add).strftime(GMT_FORMAT)
        return time_add

d = DateFormat()
print(type(d.time_now()))
print(d.time_now())
print(d.time_add(50))



class DB(object):

    def __init__(self, db_url):
        self.db_url = db_url

    def query(self, statement, **params):
        conn = self.db_url
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute(statement)
        return (cursor.fetchall())

        cursor.close()

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