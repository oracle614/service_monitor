# coding=utf-8
import pymysql
import os


class Aliyun:

    # mock db
    ALIYUN_HOST = os.getenv('ALIYUN_HOST','rdsej341u9483k397ae5.mysql.rds.aliyuncs.com')
    ALIYUN_MOCK = pymysql.connect(host=ALIYUN_HOST,user="service_monitor", password="service_monitor123", db="service_monitor",
                                  port=3306, charset="utf8")


CONFIG = Aliyun

if __name__ == '__main__':

    a = Aliyun
    conn = a.ALIUYUN_MOCK
    cursor = conn.cursor()
    sql = 'update mock_count_add set count = 40 WHERE usertoken = "Y6ccUGAN4eBJkIxQTA5kq3gXyHMKtjYN" ;'
    # sql = "SELECT * FROM mock_count_add WHERE usertoken = 'Y6ccUGAN4eBJkIxQTA5kq3gXyHMKtjYN'"
    # cursor.execute(sql)
    # res_k = cursor.description
    # res_v = cursor.fetchall()[0]
    # # print(res_k)
    # # print(res_v)
    # res ={}
    # num = 0
    # for i in res_v:
    #     res[res_k[num][0]]=i
    #     num = num +1
    # print(res)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
