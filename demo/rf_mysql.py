#!/usr/bin/python
#coding=utf8
'''
Created on 2016年8月17日

@author: Administrator
'''

import sys
import md5
import time
import urllib
import sys

import MySQLdb
import re


def Mysql_jf(db1,sql,host1,user1,passwd1,port1):
    db=MySQLdb.connect(host=host1, user=user1,passwd=passwd1,db=db1,port=port1,charset='utf8')
	#db=MySQLdb.connect(host='test.mysql.apitops.com', user='finance_test',passwd='23txjXmoX9dNQrCGBWranDcHxd8pJP',db=db1,port=4310,charset='utf8')
    cursor = db.cursor()
    sql=sql
    cursor.execute(sql)
    data=cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    return data

def Mysql_db_all(db1,sql):
    db=MySQLdb.connect(host='cat.in.apitops.com', user='lvjunjie2757',passwd='bMCk64Ja4tQdRYqikMgcertrxhL7YY',db=db1,port=8066,charset='utf8')
    cursor = db.cursor()
    sql=sql
    cursor.execute(sql)
    data=cursor.fetchall()
    data=cursor.fetchall()
    if 'UPDATE' in sql or 'DELETE' in sql:   
        db.commit()
    cursor.close()
    db.close()
    return data


def Mysql_test_new(db1,sql):
    db=MySQLdb.connect(host='test.mysql.apitops.com', user='root',passwd='root12qw!@QW',db=db1,port=4310,charset='utf8')
    cursor = db.cursor()
    sql=sql
    cursor.execute(sql)
    data=cursor.fetchall()
    if 'UPDATE' in sql or 'DELETE' in sql:   
        db.commit()
    cursor.close()
    db.close()
    return data

def Mysql_dev_notify(sql):
    db=MySQLdb.connect(host='dev.mysql.apitops.com', user='top_notifica',passwd='ZB5OFe3Fz2XsA1Gwd1WNVQWS3QdE83',db='top_notifica',port=4307,charset='utf8')
    cursor = db.cursor()
    sql=sql
    cursor.execute(sql)
    data=cursor.fetchall()
    if 'UPDATE' in sql or 'DELETE' in sql:   
        db.commit()
    cursor.close()
    db.close()
    return data


def Mysql_notify_ga(db1,sql):
    db=MySQLdb.connect(host='cat.in.apitops.com', user='qa_team',passwd='A7kmZwSYGc2EEEEAiXPNfudeEH5Vyi',db=db1,port=8066,charset='utf8')
    cursor = db.cursor()
    sql=sql
    cursor.execute(sql)
    data=cursor.fetchall()
    if 'UPDATE' in sql or 'DELETE' in sql:   
        db.commit()
    cursor.close()
    db.close()
    return data
    
def Mysql_release_new(db1,sql):
    db=MySQLdb.connect(host='cat.in.apitops.com', user='wusong161',passwd='N6YjYkiruKwGz9rfjWrU5js6nfzrXQ',db=db1,port=8066,charset='utf8')
    cursor = db.cursor()
    sql=sql
    cursor.execute(sql)
    data=cursor.fetchall()
    if 'UPDATE' in sql or 'DELETE' in sql:   
        db.commit()
    cursor.close()
    db.close()
    return data
    
def Mysql_msg_test(phone):
    db=MySQLdb.connect(host='dev.mysql.apitops.com', user='msg_dba',passwd='aPAYQR4ziboYLYspZovT',db='tops_message',port=4307,charset='utf8')
    cursor = db.cursor()
    sql="SELECT content FROM notify_sms_log WHERE target_phone LIKE '%"+phone+"%' ORDER BY create_time DESC limit 1"
    print sql
    cursor.execute(sql)
    data=cursor.fetchall()
    print data
    if  len(data)>=1:
        print data[0][0]
        re_str = re.findall(u'(验证码).+?'+'(\d+).+', data[0][0]) 
        code=re_str[0][1]
        if 'UPDATE' in sql or 'DELETE' in sql:   
            db.commit()
    else:
        code = 'null'
    db.close()
    cursor.close()
    return code


    
def Mysql_msg_ga(phone):
    db=MySQLdb.connect(host='cat.in.apitops.com', user='qa_team',passwd='A7kmZwSYGc2EEEEAiXPNfudeEH5Vyi',db='top_notifica_ga',port=8066,charset='utf8')
    cursor = db.cursor()
    sql="SELECT Params  FROM sms_messages WHERE Phone = '"+phone+"' ORDER BY SentDate DESC LIMIT 1;"
    print sql
    cursor.execute(sql)
    data=cursor.fetchall()
    #print data
    if  len(data)>=1:
        code = data[0][0]
    else:
        code = "null"
    cursor.close()
    db.close()
    return code


    
#print Mysql_notify_ga('top_notifica_ga',"SELECT Params FROM sms_messages WHERE Phone = '15157163734' ORDER BY SentDate DESC LIMIT 1")