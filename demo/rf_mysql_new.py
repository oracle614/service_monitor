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
import re
import records


def Mysql_msg_test(phone):

    db = records.Database('mysql+pymysql://msg_dba:aPAYQR4ziboYLYspZovT@dev.mysql.apitops.com:4307/tops_message?charset=utf8')
    sql = "SELECT content FROM notify_sms_log WHERE target_phone LIKE '%{phone}%' ORDER BY create_time DESC ".format(phone=phone)
    print sql
    rows = db.query(sql)
    print rows
    try :
        re_str = re.findall( u'(验证码).+?' + '(\d+).+', rows[0]['content'] )
        code=re_str[0][1]
        return code
    except IndexError:
        return 'Null'
#print Mysql_msg_test('17800000010')

def Mysql_db_all(db1,sql):
    db = records.Database( 'mysql+pymysql://lvjunjie2757:bMCk64Ja4tQdRYqikMgcertrxhL7YY@cat.in.apitops.com:8066/%s?charset=utf8' %db1)
    rows = db.query( sql )
    print sql
    try:
        rows[0]
        return rows
    except IndexError:
        return 'Null'


def Mysql_test_new(db1, sql):
    db = records.Database( 'mysql+pymysql://root:root12qw!@QW@test.mysql.apitops.com:4310/%s?charset=utf8' %db1)
    rows = db.query( sql )
    print sql
    try:
        rows[0]
        return rows
    except IndexError:
        return 'Null'

def Mysql_dev_notify(sql):
    db = records.Database( 'mysql+pymysql://top_notifica:ZB5OFe3Fz2XsA1Gwd1WNVQWS3QdE83@dev.mysql.apitops.com:4307/top_notifica?charset=utf8')
    rows = db.query( sql )
    print sql
    try:
        rows[0]
        return rows
    except IndexError:
        return 'Null'

def Mysql_notify_ga(db1, sql):
    db = records.Database( 'mysql+pymysql://qa_team:A7kmZwSYGc2EEEEAiXPNfudeEH5Vyi@cat.in.apitops.com:8066/%s?charset=utf8' % db1 )
    rows = db.query( sql )
    print sql
    try:
        rows[0]
        return rows
    except IndexError:
        return 'Null'

def Mysql_jf(db1,sql,host1,user1,passwd1,port1):

    db = records.Database(
        'mysql+pymysql://{user1}:{passwd1}@{host1}:{port1}/{db1}?charset=utf8'.format(db1=db1,user1=user1,host1=host1,passwd1=passwd1,port1=port1) )
    rows = db.query( sql )
    return rows


def Mysql_release_new(db1, sql):
    db = records.Database(
        'mysql+pymysql://wusong161:N6YjYkiruKwGz9rfjWrU5js6nfzrXQ@cat.in.apitops.com:8066/%s?charset=utf8' % db1 )
    rows = db.query( sql )
    print sql
    try:
        rows[0]
        return rows
    except IndexError:
        return 'Null'


def Mysql_dev_active(sql):
    db = records.Database(
        'mysql+pymysql://admin:7fmyfCv4UUhU7Vd8ehLN9rdN7EMm7p@dev.mysql.apitops.com:4308/tops_activity_operation?charset=utf8')
    rows = db.query( sql )
    print sql
    try:
        rows[0]
        return rows
    except IndexError:
        return 'Null'
print Mysql_dev_active('SELECT * FROM tact_cd_subject WHERE subject_id = 3')[0]['subject_answer']
#print Mysql_test_new("tops_club","SELECT * FROM tc_pt_topic_post WHERE topic_post_id=222 GROUP BY topic_post_id DESC")[0]['content']
#print Mysql_notify_ga('top_notifica_ga',"SELECT Params FROM sms_messages WHERE Phone = '15157163734' ORDER BY SentDate DESC LIMIT 1")