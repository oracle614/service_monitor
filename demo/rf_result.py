#!/usr/bin/python
#encoding: utf-8
'''
Created on 2016年5月30日
@author: Lvjj
v1.0.0.1
'''
import re
import sys
import md5
import MySQLdb
import random
import base64
from urllib import urlencode
import json
import time
import datetime
import urllib

from email import encoders
import smtplib
from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr

reload(sys)
sys.setdefaultencoding('utf-8')
# 将data的keys和values拼接为字符串QueryString
def mysql_rf_monitor(sql):
    db=MySQLdb.connect(host='test.mysql.apitops.com', user='root',passwd='root12qw!@QW',db='topsqa_rf_monitor',port=4310,charset='utf8')
    cursor = db.cursor()
    sql=sql
    #print sql
    cursor.execute(sql)
    data=cursor.fetchall()
    if 'UPDATE' in sql or 'DELETE' or 'INSERT' in sql:   
        db.commit()
    return data
    cursor.close()
    db.close()

def time_now():
    GMT_FORMAT = '%Y-%m-%d %H:%M:%S'
    time_now = datetime.datetime.now().strftime(GMT_FORMAT)
    #print time_gmt
    return time_now
def date_now():
    GMT_FORMAT = '%Y-%m-%d 00:00:00'
    date_now = datetime.datetime.now().strftime(GMT_FORMAT)
    #print time_gmt
    return date_now
print time_now() 

#获取当天成功或者失败用例的次数和失败内容
def get_failed_count(tc_id,result_id,Interval_time):
    if tc_id==0:
        sql_get_failed='SELECT tc_name,failed_content,sys_time FROM rf_product_failed_log WHERE result_id='+str(result_id)+' AND sys_time < NOW() and sys_time > (select DATE_SUB(SYSDATE(),INTERVAL '+str(Interval_time)+' MINUTE) from dual); '
    else:
        sql_get_failed='SELECT tc_name,failed_content,sys_time FROM rf_product_failed_log WHERE tc_id = '+str(tc_id)+' AND result_id='+str(result_id)+' AND sys_time < NOW() and sys_time > (select DATE_SUB(SYSDATE(),INTERVAL '+str(Interval_time)+' MINUTE) from dual); '
    #print sql_get_failed
    get_failed=mysql_rf_monitor(sql_get_failed)
    #print get_failed
    count=len(get_failed)
    tc_name=['']*count
    tc_content=['']*count
    failed_content=['']*count
    sys_time=['']*count
    failed_contents=''
    for i in range(0,count):
        tc_name[i] = get_failed[i][0]
        tc_content[i] = get_failed[i][1]
        sys_time[i] = get_failed[i][2]
        failed_content[i]='测试用例：【'+tc_name[i]+'】 ，出现异常: 【'+tc_content[i]+'】，异常时间为 : '+str(sys_time[i])
        failed_contents=failed_contents+failed_content[i]+'<br>'
    return count,failed_content,failed_contents
#print get_failed_count(1,40,1)
def get_count(tc_id,product_id,date,result):
    if 'pass' in result:
        #print 'pass'
        sql_getcount='select passed_count from rf_product_result where product_id='+str(product_id)+' and date="'+str(date) +'" and tc_id='+ str(tc_id)
    else:
        #print 'failed'
        sql_getcount='select failed_count from rf_product_result where product_id='+str(product_id)+' and date="'+str(date)+'"' 
    count=mysql_rf_monitor(sql_getcount)
    if len(count)==0:
        count=-1
    else:
        count=count[0][0]
    return count

#获取result_id
def get_resultid(tc_id,product_id,date,result):
    sql_getcount='select result_id from rf_product_result where product_id='+str(product_id)+' and date="'+str(date) +'" and tc_id='+ str(tc_id)
    resultid=mysql_rf_monitor(sql_getcount)
    if len(resultid)==0:
        resultid=-1
    else:
        resultid=resultid[0][0]
    return resultid
#print get_resultid(1,1,date_now(),'failed')

#用例成功后执行
def rf_passed(tc_id,tc_name,product_id):
    print tc_name+'：pass'
    count=get_count(tc_id,product_id,date_now(),'pass')
    #print count
    if count==-1:
        sql_pass='INSERT INTO rf_product_result (tc_id,product_id,passed_count,failed_count,date) VALUES('+str(tc_id)+','+str(product_id)+',1,0,CURDATE())'
        #print sql_pass
    else:
        count=count+1
        sql_pass='UPDATE rf_product_result set passed_count= '+str(count)+' WHERE product_id= '+str(product_id)+' AND tc_id = '+str(tc_id)+' AND date = "'+date_now()+'"'
    mysql_rf_monitor(sql_pass)
    #print sql_pass
    return count

#用例失败后执行
def rf_failed(tc_id,tc_name,product_id,content):
    #print tc_name+'：failed'
    count=get_count(tc_id,product_id,date_now(),'failed')
    #print count
    #判断数据是否存在，存在更新，不存在插入
    if count==-1:
        sql_failed='INSERT INTO rf_product_result (tc_id,product_id,passed_count,failed_count,date) VALUES('+str(tc_id)+','+str(product_id)+',0,1,CURDATE())'
    else:
        count=count+1
        sql_failed='UPDATE rf_product_result set failed_count= '+str(count)+' WHERE product_id= '+str(product_id)+' AND tc_id = '+str(tc_id)+' AND date = "'+date_now()+'"'
    print sql_failed
    mysql_rf_monitor(sql_failed)
    time.sleep(1)
    result_id=get_resultid(tc_id,product_id,date_now(),'failed')
    print result_id
    sql_failed_log='INSERT INTO rf_product_failed_log (tc_id,tc_name,result_id,failed_content) VALUES('+str(tc_id)+',"'+tc_name+'",'+str(result_id)+',"'+content+'")'
    print 'sql_failed_log = ' + sql_failed_log
    mysql_rf_monitor(sql_failed_log)
    return result_id
#print rf_failed(1,'测试一下失败的',1,'"xxxx用例失败啦"')

#邮件模块

def rf_result_email(Addressee,to_list,file1,Subject,text):
    print( '发送邮件')
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr) else addr))
    #详细邮件模块：http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000
    msg = MIMEMultipart('')
    #构造附件1
    att1 = MIMEText(open(file1, 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="setup.log"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)
    
    '''
    #构造附件2
    att2 = MIMEText(open(file2, 'rb').read(), 'base64', 'gb2312')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="setup.log"'
    msg.attach(att2)
    '''
    #加邮件头
    msg['To'] = _format_addr(u'收件人 <%s>' % to_list[0]+u'收件人 <%s>' % to_list[1])
    #msg['cc']='lvjunjie2757@tops001.com,lvjunjie84@163.com'
    #to_list=['lvjunjie2757@tops001.com''lvjunjie84@163.com']
    to_list=to_list
    msg['from'] = _format_addr(u'rf管理员 <%s>' % Addressee)
    msg['Subject'] = Header(Subject, 'utf-8')
    #part = MIMEText(TEXT, 'plain', 'utf-8')
    text=text
    msg.attach(MIMEText(text,'html', 'utf-8')) 
    #发送邮件
    try:
        server = smtplib.SMTP()
        server.connect('smtp.exmail.qq.com')
        server.login('lvjunjie2757@tops001.com','Larh7oOz8g74bJ9O')#用户名，密码
        server.sendmail(msg['from'], to_list,msg.as_string())
        server.quit()
        return 'Send success'
    except:
        return 'Send fail'

#用例失败告警通知
def rf_failed_notice(max_count,count,content,email_parameter=['','','','','']):
    if count >= max_count and email_parameter[0] != '':
        #需要告警
        print '准备发送邮件'
        return rf_result_email(email_parameter[0],email_parameter[1],email_parameter[2],email_parameter[3],content)
    else: 
        print '未达到发送邮件标准'
        return 'Do not email'

#rf_failed = get_failed_count(0,14,10000)
#rf_failed_notice(1,rf_failed[0],rf_failed[2],['lvjunjie2757@tops001.com',['188556051@qq.com','lvjunjie2757@tops001.com'],'c:\setup.log','销冠经纪告警'])