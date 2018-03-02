#!/usr/bin/python
# encoding: utf-8
'''
Created on 2016年5月30日
@author: Lvjj
v1.0.0.1
'''
import re
import sys
from hashlib import md5

import random
import base64
from urllib import urlencode

import json
import time
import datetime
import urllib
import md5

import requests
reload(sys)
sys.setdefaultencoding('utf-8')


# 将data的keys和values拼接为字符串QueryString


def xf(x, y=26):
    l = []
    while 1:
        if x == 0:
            break
        else:
            z, h = divmod(x - 1, y)
            x = z
            l.insert(0, chr(65 + h))
    return ''.join(map(str, l))


def get_MD5_Value(string):
    mString = md5.new()
    mString.update(string)
    return mString.hexdigest()



def base64_Image(Image_path):
    f = open(Image_path, 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()
    return 'data:image/png;base64,' + ls_f



def _utf8_urlencode(data):
    if type(data) is unicode:
        return data.encode('utf-8')

    if not type(data) is dict:
        return data
    utf8_data = {}
    for k, v in data.iteritems():
        utf8_data[k] = unicode(v).encode('utf-8')
    return urlencode(utf8_data)


def time_gmt():
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    time_gmt = datetime.datetime.now().strftime(GMT_FORMAT) + '+0800'
    # print time_gmt
    return time_gmt


def sign_v4(host, query, Body='', Date=time_gmt()):
    AppKeySecret = '7LKeOCgnDBoS7HztMxLFrNUopUCozE6G'
    if 'http://' in host or 'https://' in host:
        host = re.findall('^http(s)?://(.+)$', host)[0][1]
        print 'host==============' + host
    if 'apikber' in query:
        if 'test' in host or 'beta' in host:
            AppKeySecret = 'xZhhmL181KY9W6IHabYcRTdGbL0KnyAq'
        else:
            AppKeySecret = 'UD2nNigzNzaR0nOHcld9zL7uSjO5JOTD'
    if Body == '':
        Body_md5 = '00000000000000000000000000000000'
    else:
        print 'Body==============' + Body
        Body = md5.new(Body)
        Body_md5 = Body.hexdigest()

    str1 = host + query
    # print str1.lower()

    si = str1.lower() + Body_md5 + Date + AppKeySecret
    print 'si==================' + si
    sign_v4 = md5.new()
    sign_v4.update(si)
    return 'v4:' + sign_v4.hexdigest(), Date


# print sign_v4('http://gateway.test.apitops.com','/oauth/Authorization/Login','{\"agent\":android,\"appcode\":app_broker,\"loginName\":15157163734,\"password\":\"83b4ef5ae4bb360c96628aecda974200\"}','Sun, 19 Feb 2017 11:49:40 GMT+0800')

def dictionary_to_json(dictionary=None):
    if dictionary is None:
        dictionary = {}
    str_json = json.dumps(dictionary)
    return str_json


def dictionary_to_form(dictionary=None):
    if dictionary is None:
        dictionary = {}
    str_form = urlencode(dictionary)
    return str_form

def dict_to_json(dictionary=None):
    if dictionary is None:
        dictionary = {}
    str_json = json.dumps(dictionary)
    return str_json


def dict_to_form(dictionary=None):
    if dictionary is None:
        dictionary = {}
    str_form = urlencode(dictionary)
    return str_form

def rf_count(a, b):
    return a.count(b)


def rf_replace(str, old_word, new_word):
    return str.replace(old_word, new_word)


def rf_re(str, re1, id=1):
    re_str = re.findall(re1, str)
    if id == 1:
        return re_str[0]
    return re_str[0][id - 1]


# str='/index.html?uk=90abf029-3f9a-47b3-89ff-4964c4bf2054&#/zone'
# print rf_re(str,'(.+)uk=(.+)&.+',2)
def time_nor():
    time_FORMAT = '%Y-%m-%d %H:%M:%S'
    time = datetime.datetime.now().strftime(time_FORMAT)
    # print time_gmt
    return time


def jsp_json(json):
    content_jsp = '<%@ page language="java" contentType="text/html; charset=ISO-8859-1"\n' + 'pageEncoding="ISO-8859-1"%>' + json + '<%\n' + 'try {\n' + '        java.util.Enumeration<String> e = request.getParameterNames();\n' + '        while (e.hasMoreElements()) {\n' + '            String key = e.nextElement();\n' + '            String value = request.getParameter(key);' + '        }\n' + '    } catch (Exception e) {\n' + '}\n%>'
    return content_jsp


def update_file(content, file1):
    f = open(file1, 'w')  # 打开文件。若文件不存在，则创建文件，打开方式为'w'
    f.write(content)  # 把字符串写入文件
    # f.colse()                  #关闭文件


def Http_Upload_File(head):
    resp = requests.post('http://gateway.test.apitops.com/clubapi/upload/attachments',
                         files={"file": open('C:/Users/Administrator/Desktop/Picture/temp0_750_1000.jpeg', 'rb')},
                         headers=head)
    print resp


def distance(x1, y1, x2, y2):
    return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 10)


def random_str(randomlength=8):
    from random import Random
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


# print random_str()

def random_name():  # 随机姓名
    import random as r
    a1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕',
          '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛',
          '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉',
          '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康',
          '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝',
          '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    a2 = ['玉', '明', '龙', '芳', '军', '玲', '俊', '赫', '梦', '天', '人', '阿', '加', '来', '顺']
    a3 = ['', '立', '玲', '杰', '国']

    name = r.choice(a1) + r.choice(a2) + r.choice(a3)
    return (name)

def random_familyname():  # 随机生成姓
    import random as r
    a1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕',
          '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛',
          '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉',
          '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康',
          '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝',
          '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    familyname = r.choice(a1)
    return (familyname)


# print random.randrange(0, 2, 1)
print random_familyname()


# 获取message
def get_message(self, string):
    ret_dict = json.loads(string)
    message = ret_dict.get('Message')
    return message


def random_phone():  # 随机手机号码
    phoneno = random.choice(
        ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '147', '151', '153', '155', '157', '170',
         '177', '180', '181', '183', '185', '186', '187', '189']) + "".join(
        random.choice("0123456789") for i in range(8))
    return phoneno


#print random_phone()
# print random_name()
# print distance(120.1839752,29.232065,120.1839752,30.2220650)
# str='{"Code":0,"Message":"","Data":{"list":{"Items":[{"ValidStartDate":"2017-03-30","ValidEndDate":"2017-04-09","TotalBalance":13000.0000,"capitalpool_id":5,"AccountCodeSigned":"3F9D92C723711459DF7A502284D1EC0D","condominium":true,"total_outamount":0.0000,"total_inamount":13000.0000,"total_balance_usable":13000.0000,"total_bill":13000.0000,"total_frozenamount":0.0000,"service_charge":0.0000,"had_profit_and_loss":true,"id":7184,"sys_groupguid":"","group_guid":"","account_code":"CP00000005","account_name":"金光闪闪","company":"","project_name":"金光闪闪","store_code":"","account_type":4,"city_id":112,"city_name":"杭州市","source_id":3125,"parent_id":0,"note":"","is_enable":true,"enable_time":"2017-04-04 21:17:23","stop_time":"2000-01-01","rel_time":"2000-01-01","total_amount":0.0000,"total_balance":0.0000,"contacts_name":"","phone":"","addr_name":"超级管理员","postcode":"","create_time":"2017-04-04 21:17:23","is_deleted":false,"sys_time":"2017-04-04 21:19:03","is_notcheck":false},{"ValidStartDate":"2017-03-30","ValidEndDate":"2017-04-09","TotalBalance":0.0000,"capitalpool_id":4,"AccountCodeSigned":"EBE933177943542B90BF63FC3A9C83E0","condominium":false,"total_outamount":0.0000,"total_inamount":0.0000,"total_balance_usable":0.0000,"total_bill":0.0000,"total_frozenamount":0.0000,"service_charge":0.0000,"had_profit_and_loss":false,"id":7183,"sys_groupguid":"","group_guid":"","account_code":"CP00000004","account_name":"旅游地产1","company":"","project_name":"旅游地产1","store_code":"","account_type":4,"city_id":112,"city_name":"杭州市","source_id":3130,"parent_id":0,"note":"","is_enable":true,"enable_time":"2017-04-04 21:16:06","stop_time":"2000-01-01","rel_time":"2000-01-01","total_amount":0.0000,"total_balance":0.0000,"contacts_name":"","phone":"","addr_name":"超级管理员","postcode":"","create_time":"2017-04-04 21:16:06","is_deleted":false,"sys_time":"2017-04-04 21:16:08","is_notcheck":false},{"ValidStartDate":"2017-03-30","ValidEndDate":"2017-04-09","TotalBalance":19306.9600,"capitalpool_id":3,"AccountCodeSigned":"E1B2FA16E695F3F7ED34340A7525AD24","condominium":true,"total_outamount":693.0400,"total_inamount":20000.0000,"total_balance_usable":-1693.0400,"total_bill":9306.9600,"total_frozenamount":0.0000,"service_charge":0.0000,"had_profit_and_loss":true,"id":7182,"sys_groupguid":"","group_guid":"","account_code":"CP00000003","account_name":"kk测试","company":"","project_name":"kk测试","store_code":"","account_type":4,"city_id":112,"city_name":"杭州市","source_id":395,"parent_id":0,"note":"","is_enable":true,"enable_time":"2017-04-04 21:09:38","stop_time":"2000-01-01","rel_time":"2000-01-01","total_amount":0.0000,"total_balance":9306.9600,"contacts_name":"","phone":"","addr_name":"超级管理员","postcode":"","create_time":"2017-04-04 21:09:38","is_deleted":false,"sys_time":"2017-04-11 14:54:03","is_notcheck":true},{"ValidStartDate":"2017-03-30","ValidEndDate":"2017-04-09","TotalBalance":61000.0000,"capitalpool_id":2,"AccountCodeSigned":"EFEE3EDC0F7692E82E6017C664F85373","condominium":true,"total_outamount":0.0000,"total_inamount":61000.0000,"total_balance_usable":45000.0000,"total_bill":45000.0000,"total_frozenamount":0.0000,"service_charge":0.0000,"had_profit_and_loss":true,"id":7181,"sys_groupguid":"","group_guid":"","account_code":"CP00000002","account_name":"测试315","company":"","project_name":"测试315","store_code":"","account_type":4,"city_id":112,"city_name":"杭州市","source_id":3152,"parent_id":0,"note":"","is_enable":true,"enable_time":"2017-04-04 21:09:06","stop_time":"2000-01-01","rel_time":"2000-01-01","total_amount":0.0000,"total_balance":45000.0000,"contacts_name":"","phone":"","addr_name":"超级管理员","postcode":"","create_time":"2017-04-04 21:09:06","is_deleted":false,"sys_time":"2017-04-12 16:08:35","is_notcheck":false},{"ValidStartDate":"2017-03-29","ValidEndDate":"2017-04-01","TotalBalance":29999.0000,"capitalpool_id":1,"AccountCodeSigned":"0F5DE86549175EF4EBB6DF27D2823E0E","condominium":true,"total_outamount":10000.0000,"total_inamount":39999.0000,"total_balance_usable":10000.0000,"total_bill":10000.0000,"total_frozenamount":0.0000,"service_charge":1.0000,"had_profit_and_loss":true,"id":7180,"sys_groupguid":"","group_guid":"","account_code":"CP00000001","account_name":"代理商的开发商","company":"","project_name":"代理商的开发商","store_code":"","account_type":4,"city_id":112,"city_name":"杭州市","source_id":3170,"parent_id":0,"note":"","is_enable":true,"enable_time":"2017-04-01 20:56:29","stop_time":"2000-01-01","rel_time":"2000-01-01","total_amount":0.0000,"total_balance":0.0000,"contacts_name":"","phone":"","addr_name":"超级管理员","postcode":"","create_time":"2017-04-01 20:56:29","is_deleted":false,"sys_time":"2017-04-04 21:06:52","is_notcheck":false}],"Count":5},"info":{"Outamount":10693.0400,"Inamount":133999.0000,"Balance":123305.9600,"BalanceUsable":66306.9600,"Bill":77306.9600}},"ServerTime":"2017-04-13 10:44:24"}'
# print rf_re(str,'^(.+)AccountCodeSigned\":\"(.+)\",\"condominium(.+)CP00000005.+',2)
# d = {'first':'O,n e','second':'2'}
# print dictionary_to_form(d)
# p = rf_re('https://gateway.test.apitops.com','^(.+)s(.+)$',1)
# print p
# a='{"Code":0,"Message":"","Data":{"list":{"Items":[{"AccountCode":"AP00004829","AccountCodeSigned":"D56C376825D3CE7C5311CAAA897252D6","AccountName":"AP00004829","AccountType":2,"Company":"测试门店：门店代码延迟出现","ProjectName":"门店代码延迟出现","StoreCode":"HZ00000161","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-31 16:39:36","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004828","AccountCodeSigned":"B27E08E0462342D9137714D6AF7A8963","AccountName":"AP00004828","AccountType":2,"Company":"万宁代理3","ProjectName":"万宁代理3","StoreCode":"WN00000003","city_id":295,"CityName":"万宁市","EnableTime":"2017-03-31 16:00:17","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004827","AccountCodeSigned":"6CAD5628471E0064B5D207FEFD52E6CF","AccountName":"AP00004827","AccountType":2,"Company":"万宁代理商2","ProjectName":"万宁代理商2","StoreCode":"WN00000002","city_id":295,"CityName":"万宁市","EnableTime":"2017-03-31 15:58:55","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004826","AccountCodeSigned":"9CAA089CDA90B59B080D6F8443A16D29","AccountName":"AP00004826","AccountType":2,"Company":"万宁代理店","ProjectName":"万宁代理店","StoreCode":"WN00000001","city_id":295,"CityName":"万宁市","EnableTime":"2017-03-31 15:27:11","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004825","AccountCodeSigned":"10C582ED23943F64652C89118242F765","AccountName":"AP00004825","AccountType":2,"Company":"绍兴代理商","ProjectName":"绍兴代理商","StoreCode":"SXG0000003","city_id":116,"CityName":"绍兴市","EnableTime":"2017-03-31 14:51:37","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004824","AccountCodeSigned":"D642F4A9C738F1ED890766AACCDC4A27","AccountName":"AP00004824","AccountType":2,"Company":"测试代理商测试门店","ProjectName":"测试代理商","StoreCode":"SXG0000002","city_id":116,"CityName":"绍兴市","EnableTime":"2017-03-30 16:01:19","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004823","AccountCodeSigned":"FFB34DDE6BAA5132AB8DD50A5BE47AA2","AccountName":"AP00004823","AccountType":2,"Company":"绍兴测试代理商经纪公司","ProjectName":"代理商公司","StoreCode":"SXG0000001","city_id":116,"CityName":"绍兴市","EnableTime":"2017-03-30 15:18:40","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004822","AccountCodeSigned":"73BB4ED74AE57A35AADC0C1DE9B4D290","AccountName":"AP00004822","AccountType":2,"Company":"ttt","ProjectName":"tttt","StoreCode":"CC00000001","city_id":75,"CityName":"长春市","EnableTime":"2017-03-29 09:59:25","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004821","AccountCodeSigned":"7A967A2BC9C5E43E38996D1CBFBFC81F","AccountName":"AP00004821","AccountType":2,"Company":"测试门店327","ProjectName":"测试门店327","StoreCode":"HZ00000160","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-27 17:41:49","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004820","AccountCodeSigned":"252E1CB3FB9325B2E58CD0548382EA32","AccountName":"AP00004820","AccountType":2,"Company":"千层层经纪门店","ProjectName":"qcc","StoreCode":"HZ00000159","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-24 15:35:20","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004819","AccountCodeSigned":"B486EEB26852B3677BB59DB1E5574BF3","AccountName":"AP00004819","AccountType":2,"Company":"测试对的对的","ProjectName":"对的","StoreCode":"HZ00000158","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-21 15:11:20","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004818","AccountCodeSigned":"25BC890D6ACC895C6AE64A5DFE997332","AccountName":"AP00004818","AccountType":2,"Company":"溜溜对的","ProjectName":"溜溜","StoreCode":"NJ00000006","city_id":97,"CityName":"南京市","EnableTime":"2017-03-21 10:41:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004817","AccountCodeSigned":"78C24D796C1390B4CF5779D04298E736","AccountName":"AP00004817","AccountType":2,"Company":"测试门店","ProjectName":"1111","StoreCode":"HZ00000154","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-21 10:41:14","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004816","AccountCodeSigned":"D57008BC8A28A533D5F2396C86FB56C7","AccountName":"AP00004816","AccountType":2,"Company":"涂涂321","ProjectName":"321","StoreCode":"NJ00000007","city_id":97,"CityName":"南京市","EnableTime":"2017-03-21 10:41:13","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004815","AccountCodeSigned":"327D3AD330A1D4B30B29A60779A4A5B2","AccountName":"AP00004815","AccountType":2,"Company":"溜溜梅321","ProjectName":"321","StoreCode":"NJ00000005","city_id":97,"CityName":"南京市","EnableTime":"2017-03-21 10:41:11","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004814","AccountCodeSigned":"A9419F24EA60E5900EA2AB2591324D74","AccountName":"AP00004814","AccountType":2,"Company":"厉害了","ProjectName":"厉害","StoreCode":"NJ00000004","city_id":97,"CityName":"南京市","EnableTime":"2017-03-17 10:34:16","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004813","AccountCodeSigned":"0C76D3173F0EB53AC7F295B7AF1B37C7","AccountName":"AP00004813","AccountType":2,"Company":"测试对接老系统315","ProjectName":"老系统315","StoreCode":"NJ00000003","city_id":97,"CityName":"南京市","EnableTime":"2017-03-15 17:02:04","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004812","AccountCodeSigned":"4C5DEFA519343CFCBE1008DFC0B2D057","AccountName":"AP00004812","AccountType":2,"Company":"宁波新新房产有限公司赞成店","ProjectName":"宁波新新房产赞成店","StoreCode":"NB00000002","city_id":115,"CityName":"宁波市","EnableTime":"2017-03-15 10:19:00","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004811","AccountCodeSigned":"6FAE5B8CEE463DBFCB8892F7A7690194","AccountName":"AP00004811","AccountType":2,"Company":"测试315","ProjectName":"315","StoreCode":"HZ00000153","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-15 10:07:29","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004810","AccountCodeSigned":"55EA1C77541EF6AB32B52DF7BBE3FBBF","AccountName":"AP00004810","AccountType":2,"Company":"测试跨城市都结算","ProjectName":"都结算","StoreCode":"NJ00000002","city_id":97,"CityName":"南京市","EnableTime":"2017-03-14 14:42:38","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004809","AccountCodeSigned":"52D0FFB50108AE8045885A40A84E2AD7","AccountName":"AP00004809","AccountType":2,"Company":"测试314","ProjectName":"314","StoreCode":"HZ00000152","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-14 11:26:31","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004808","AccountCodeSigned":"6C979DFF0864990FF26ACE505910E415","AccountName":"AP00004808","AccountType":2,"Company":"测试城","ProjectName":"城","StoreCode":"HZ00000151","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-13 16:02:52","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004807","AccountCodeSigned":"DB185853BFAF8DECD33C23850112066C","AccountName":"AP00004807","AccountType":2,"Company":"销冠测试门店","ProjectName":"xgcs","StoreCode":"HK00000001","city_id":289,"CityName":"海口市","EnableTime":"2017-03-13 15:39:41","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004806","AccountCodeSigned":"2C9C2CA021F071158D80730B06374FD6","AccountName":"AP00004806","AccountType":2,"Company":"测试对接bops313","ProjectName":"对接bops313","StoreCode":"HZ00000150","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-13 15:39:40","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004805","AccountCodeSigned":"AA43D37D0D3C5CEE02F312DD21BB4D24","AccountName":"AP00004805","AccountType":2,"Company":"测试进应付313","ProjectName":"应付313","StoreCode":"HZ00000149","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-13 15:39:39","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004804","AccountCodeSigned":"1BC292791FF73F6FF5A141C35BFE6A57","AccountName":"AP00004804","AccountType":2,"Company":"销冠测试分公司","ProjectName":"xgcefgs","StoreCode":"HZ00000148","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-13 15:39:38","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004803","AccountCodeSigned":"D77B9C1C3671E904DE0963A84CCDA0D9","AccountName":"AP00004803","AccountType":2,"Company":"测试跨城市","ProjectName":"跨城市","StoreCode":"NJ00000001","city_id":97,"CityName":"南京市","EnableTime":"2017-03-10 12:01:03","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004802","AccountCodeSigned":"E266358FF0F1717AB2AEBC0640601785","AccountName":"AP00004802","AccountType":2,"Company":"测试bops对接","ProjectName":"bops","StoreCode":"HZ00000147","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-10 10:12:16","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004801","AccountCodeSigned":"C923F03F472419B92BACB1EE98BF8E4C","AccountName":"AP00004801","AccountType":2,"Company":"宗厚上单真坑","ProjectName":"宗厚坑","StoreCode":"HZ00000146","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 19:01:42","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004800","AccountCodeSigned":"2185FE517A34D10D33CA264229832DCB","AccountName":"AP00004800","AccountType":2,"Company":"201739同步测试1","ProjectName":"201739同步测试1","StoreCode":"HZ00000144","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004799","AccountCodeSigned":"8FA555D83971749EFF24377A52605C5F","AccountName":"AP00004799","AccountType":2,"Company":"同步什么情况1","ProjectName":"情况1","StoreCode":"CQ00000002","city_id":38,"CityName":"重庆市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004798","AccountCodeSigned":"211EA2AE8B60D31A2E72EFBB5EBE4378","AccountName":"AP00004798","AccountType":2,"Company":"weoifwoef","ProjectName":"131231","StoreCode":"TJ00000008","city_id":36,"CityName":"天津市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004797","AccountCodeSigned":"1494E53174535A44B0D9E586C180E34C","AccountName":"AP00004797","AccountType":2,"Company":"test201737","ProjectName":"同步呀","StoreCode":"TJ00000005","city_id":36,"CityName":"天津市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004796","AccountCodeSigned":"F6BEB182A8358EACDC39929164F281BF","AccountName":"AP00004796","AccountType":2,"Company":"同步呀同步呀2","ProjectName":"同步呀","StoreCode":"TJ00000004","city_id":36,"CityName":"天津市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004795","AccountCodeSigned":"A4DFA37B7767C651A3AEFD266658519D","AccountName":"AP00004795","AccountType":2,"Company":"测试门店名称","ProjectName":"csmdmc","StoreCode":"HZ00000142","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004794","AccountCodeSigned":"183557509F3A141F401A7E36721519EB","AccountName":"AP00004794","AccountType":2,"Company":"测试20173602","ProjectName":"测试","StoreCode":"HZ00000133","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004793","AccountCodeSigned":"EDC92B34EEA5594A2A19B7538972B549","AccountName":"AP00004793","AccountType":2,"Company":"小棍","ProjectName":"xx","StoreCode":"NB00000001","city_id":115,"CityName":"宁波市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004792","AccountCodeSigned":"B44BAB981AFE4A428F3F84D6B843F2D1","AccountName":"AP00004792","AccountType":2,"Company":"新新门店同步测试1","ProjectName":"11","StoreCode":"TJ00000002","city_id":36,"CityName":"天津市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004791","AccountCodeSigned":"32D4C0C9860439053A125E013F23A3DD","AccountName":"AP00004791","AccountType":2,"Company":"测试一下同步eventId","ProjectName":"同步eventId","StoreCode":"hz12345704","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004790","AccountCodeSigned":"7CDF2C8873B72C3908E1EDF0F27B9B5B","AccountName":"AP00004790","AccountType":2,"Company":"test20170224","ProjectName":"test20170224","StoreCode":"HZ1047001","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004789","AccountCodeSigned":"45589D592760920A807F991EAFAF47E4","AccountName":"AP00004789","AccountType":2,"Company":"test分店乱了?","ProjectName":"tst","StoreCode":"HZ1002002","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004788","AccountCodeSigned":"161B1247D327B63E841484D747FF4BBC","AccountName":"AP00004788","AccountType":2,"Company":"门店完整性校验5","ProjectName":"校验1","StoreCode":"HZ011004","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004787","AccountCodeSigned":"FC4863CFD800EDEC446484FE4C95766F","AccountName":"AP00004787","AccountType":2,"Company":"门店完整性校验4","ProjectName":"校验1","StoreCode":"HZ011003","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004786","AccountCodeSigned":"8296478692EBFA4C84421E66EB706E41","AccountName":"AP00004786","AccountType":2,"Company":"门店完整性校验2","ProjectName":"校验1","StoreCode":"HZ011002","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004785","AccountCodeSigned":"EF8E98C73F2FD463C3C51100355AD020","AccountName":"AP00004785","AccountType":2,"Company":"测试1111","ProjectName":"测试1111","StoreCode":"hz12345703","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004784","AccountCodeSigned":"C6022DA1EDC5A7C716304034F55409F9","AccountName":"AP00004784","AccountType":2,"Company":"同步测试门店123","ProjectName":"123","StoreCode":"hz12345701","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004783","AccountCodeSigned":"85343015933E92942200F97FE30C970E","AccountName":"AP00004783","AccountType":2,"Company":"经纪人账号","ProjectName":"验证","StoreCode":"hz12345698","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004782","AccountCodeSigned":"145934ACADD007675D49F8775B77F189","AccountName":"AP00004782","AccountType":2,"Company":"广东省发个梵蒂冈梵蒂冈","ProjectName":"gfdfr","StoreCode":"hz12345702","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004781","AccountCodeSigned":"F8487AD037316E60E82CB6240A4E44E7","AccountName":"AP00004781","AccountType":2,"Company":"财务测试","ProjectName":"财务账号","StoreCode":"hz12345695","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""},{"AccountCode":"AP00004780","AccountCodeSigned":"346946E7716EE3BE6A1E04ECBDEE7A13","AccountName":"AP00004780","AccountType":2,"Company":"财务账号注册验证","ProjectName":"财务","StoreCode":"hz12345696","city_id":112,"CityName":"杭州市","EnableTime":"2017-03-09 11:32:15","IsEnable":true,"TotalBill":0,"TotalAmount":0,"TotalCount":0,"TotalBalance":0,"Note":""}],"Count":4677},"info":{"TotalBillSum":0.0000,"TotalAmountSum":0.0000,"TotalBalanceSum":0.0000,"TotalCountSum":0}},"ServerTime":"2017-03-31 16:57:59"}'
# p = rf_re(a,'^.+"AccountCode":"AP00004825","AccountCodeSigned":"(.+)","AccountName":"AP00004825"',1)
# print p
