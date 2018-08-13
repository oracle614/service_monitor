#!/usr/bin/python
#encoding: utf-8
'''
Created on 2016年5月30日
@author: Lvjj
'''
import re
import sys
import md5
import base64
from urllib import urlencode
import json
import time
import datetime
import urllib
from urllib import quote
from urllib import unquote
from urllib import urlencode
import MySQLdb
import scpclient
import paramiko
import xlwt
import xlrd
import xlsxwriter
import linecache
import smtplib
from email.MIMEText import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.header import Header
reload(sys)
sys.setdefaultencoding('utf-8')
def xf(x,y=26):
    l=[]
    while 1:
        if x==0:
            break
        else:
            z,h=divmod(x-1,y)
            x=z
            l.insert(0,chr(65+h))
    return ''.join(map(str,l))
def get_MD5_Value(string):
    mString = md5.new()
    mString.update(string)
    return mString.hexdigest()
def changge(c):
    c= str(c)
    #print quote(c)
    return quote(c)
def timenow():
    timeStr = datetime.now()
    times = str(timeStr)
    times = times.replace(" ", "").replace(":", "").replace("-", "").replace(".","")[:-3]
    return times
#print timenow()
def base64_Image(Image_path):
    f=open(Image_path,'rb') #二进制方式打开图文件     
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码    
    return 'data:image/png;base64,'+ls_f
    f.close() 
def Image_binary(Image_path):
    f=open(Image_path,'rb') #二进制方式打开图文件     
    return f.read()
    f.close() 
def _utf8_urlencode(data):
    if type(data) is unicode:
        return data.encode('utf-8')

    if not type(data) is dict:
        return data
    utf8_data = {}
    for k, v in data.iteritems():
        utf8_data[k] = unicode(v).encode('utf-8')
    return urlencode(utf8_data)
def sign_new(host, uri, data={}, headers=None, params={},files={}):
    '''
    session = self._cache.switch(alias)
    print 'host' + '=' + session.url
    host = session.url
    '''
    # * * * 适配APP需要签名的场景 * * *
    if "gateway" in host or "100.28" in host:
        #* * * gateway签名 * * *
        print 'gateway'
        if ("test" in host) or ("beta" in host) or ("demo" in host) or ("integrate" in host) or ( "100.28" in host) :
            ConsumerKey = "ae80b757c66741ccace3169a0d223acd"
        else :
            ConsumerKey = "0af9944d954343c3a5a8d7a989512d12"
        #print 'ConsumerKey' + '=' + ConsumerKey
        #设置AppKey
        broker = "374fa3ab6b1fae595db5382afe415bce"
        admin = "374fa3ab6b1fae595db5382afe415bce"
        test = "11021d8cfed50c14eeb3cca9aeb654f0"
        #判断AppKey
        if "User-Agent" in headers :
            headValue = headers.get("User-Agent")
            if "com.kakao.topsales" in headValue:
                Appkey = admin
            elif "com.kakao.topbroker" in headValue:
                Appkey = broker
            else :
                Appkey = test
            print 'Appkey' + '=' + Appkey
        #将Consumer-Key插入header头
        headers['Consumer-Key'] = ConsumerKey
        #获取GMT时间插入header头
        GMT = '%a, %d %b %Y %H:%M:%S GMT+0800'
        headers['Date'] = datetime.now().strftime(GMT)
        #获取data里面的ak信息，插入到header头
        if len(data)>1:
            if "ak" in data :
                headers['Authorization'] = data['ak']
            else :
                headers['Authorization'] = ''
            #取出Key并且忽略大小写进行排序
            keys = data.keys()
            keys.sort(cmp=lambda x,y: cmp(x.lower(), y.lower()))
            #将data的keys和values拼接为字符串QueryString
            QueryString = keys[0].lower() + '=' + quote(str(data.get(keys[0])))
            for i_p in keys:
                print i_p + '=' + str(data[i_p])
                if i_p.lower() != keys[0].lower():
                    QueryString = QueryString +  '&' + i_p.lower() + '=' + quote(str(data.get(i_p)))
            data = QueryString
            print 'data' + '=' + data
            #md5Body值
            md5Body = md5.new()
            md5Body.update(QueryString)
            md5Body = md5Body.hexdigest()
            #print 'MD5(Body)' + '=' + md5Body
        else :
            if "ak" in params :
                headers['Authorization'] = params['ak']
            else :
                headers['Authorization'] = ''
            md5Body = '00000000000000000000000000000000'
        #获取url
        url = host + uri
        if url.find('?') > 0:
            url = url.split('?')[0]
        url = url[7:]
        #print 'url'+ '=' + url
        print md5Body
        #md5需要签名的值
        md5last = url.lower() + md5Body + headers['Date'] + Appkey
        #print 'Lower(url) + MD5(Body) + Header[Date] + AppKeySecret' + '=' + md5last
        md5lasted = md5.new()
        md5lasted.update(md5last)
        print 'The sign' + '=' + md5lasted.hexdigest()
        #将Signature插入header头
        headers['Signature'] = 'v3:'+ md5lasted.hexdigest()
        #print url
        #print headers
        #print data, headers , uri
        return data, headers , uri
    elif  "192.168.255.96" in host:
        print uri
        print headers
        return data, headers , uri
    else :
        #非gateway签名
        broker = "374fa3ab6b1fae595db5382afe415bce"
        admin = "80b131d757c90282b802e3f9840bfd71"
        test = "11021d8cfed50c14eeb3cca9aeb654f0"
        #判断AppKey
        if "User-Agent" in headers :
            headValue = headers.get("User-Agent")
            if "com.kakao.topsales" in headValue:
                Appkey = admin
            elif "com.kakao.topbroker" in headValue:
                Appkey = broker
            else :
                Appkey = test
            print 'Appkey' + '=' + Appkey
            if len(Appkey)>0:
                #获取ApiName
                urlStr = uri
                if urlStr.find('?') > 0:
                    urlStr = urlStr.split('?')[0]
                strTmp = urlStr.split('/')
                ApiName = urlStr.split('/')[len(strTmp)-1]
                ApiName = ApiName.lower()
                print 'ApiName' + '=' + ApiName

                #生成time参数并将time参数插入data
                timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                timeStr = timeStr.replace(" ","").replace(":","").replace("-","")+"179"
                data.setdefault('time',timeStr)

                #取出Key并且忽略大小写进行排序
                keys = data.keys()
                keys.sort(cmp=lambda x,y: cmp(x.lower(), y.lower()))

                #将data的keys和values拼接为字符串QueryString
                QueryString = keys[0].lower() + '=' + quote(str(data.get(keys[0])))
                for i_p in keys:
                    print i_p + '=' + str(data[i_p])
                    if i_p.lower() != keys[0].lower():
                        QueryString = QueryString +  '&' + i_p.lower() + '=' + quote(str(data.get(i_p)))
                data = QueryString
                print 'data' + '=' + data
                #生成PlainText
                PlainText = ApiName + QueryString + Appkey
                print 'PlainText' + '=' + PlainText
                #生成MD5
                sign = md5.new()
                sign.update(PlainText)
                print 'The sign' + '=' + sign.hexdigest()

                #在url后插入sign值
                if uri.find('?') != -1:
                    uri = uri + '&' + "sign=" + sign.hexdigest()
                else:
                    uri = uri + '?' + "sign=" + sign.hexdigest()
            print uri
            print headers
            #return data, headers , uri
            return sign.hexdigest()


def sign(string, data, time, sig):
    broker = "374fa3ab6b1fae595db5382afe415bce"
    admin = "80b131d757c90282b802e3f9840bfd71"
    test = "11021d8cfed50c14eeb3cca9aeb654f0"
    #print data
    if sig == "app_sales":
        sig = admin
    elif sig == "app_broker":
        sig = broker
    elif sig == "test":
        sig = test

    urlStr = str(string)
    if urlStr.find('?') > 0:
        urlStr = urlStr.split('?')[0]
    strTmp = urlStr.split('/')
    ApiName = urlStr.split('/')[len(strTmp) - 1]
    ApiName = ApiName.lower()
    #print ApiName
    # time = timenow()
    # print time
    paras = data.keys()
    #print ("paras:= {0}".format(paras))
    #dataTmp = "app=" + data.get("app") + "&" + "time=" + time + "&" + "agent=" + data.get("agent")
    dataTmp = "time=" + time
    #print dataTmp
    for i_p in paras:

        dataTmp = dataTmp + '&' +i_p.lower() + '=' + changge(data.get(i_p))

    dataTmp = dataTmp.split('&')
    #print("dataTmp:= {0}".format(dataTmp))
    dataList = sorted(dataTmp)
    #print("dataList:= {0}".format(dataList))
    QueryString = ""
    for i in dataList:
        if QueryString == "":
            QueryString = i
        else:
            QueryString = QueryString + '&' + i
    #print QueryString

    # 生成PlainText
    PlainText = ApiName + QueryString + sig
    #print PlainText

    # 生成MD5
    sign = md5.new()
    sign.update(PlainText)
    #print "the sign value is "
    #print sign.hexdigest()
    return sign.hexdigest()


def Mysql_db_all(db1,sql):
    db=MySQLdb.connect(host='cat.in.apitops.com', user='lvjunjie2757',passwd='bMCk64Ja4tQdRYqikMgcertrxhL7YY',db=db1,port=8066,charset='utf8')
    cursor = db.cursor()
    sql=sql
    cursor.execute(sql)
    data=cursor.fetchall()
    db.commit()
    return data
    cursor.close()
    db.close()


def Mysql_db_chandao(db1,sql):
    db=MySQLdb.connect(host='rdsej341u9483k397ae5.mysql.rds.aliyuncs.com', user='admin_ljj',passwd='a1478520B',db=db1,port=3306,charset='utf8')
    cursor = db.cursor()
    sql=sql
    cursor.execute(sql)
    data=cursor.fetchall()
    db.commit()
    return data
    cursor.close()
    db.close()

def split_str(str,Separator):
    return str.split(Separator)

def chandao_burn_down_chart():#生成bug燃尽图，保存到'D:/chandao/chandao_burn_down_chart.xls'
    COUNT=30#获取近30天数据
    #从MySQL中获取历史bug数据
    
    bug_num=Mysql_db_chandao('tops001','SELECT bug_num FROM changdao_bug_statistics WHERE is_delete=0 ORDER BY date DESC LIMIT 0,'+str(COUNT)+';')
    COUNT1= Mysql_db_chandao('tops001','SELECT COUNT(*) FROM changdao_bug_statistics WHERE is_delete=0; ')[0][0]
    #print COUNT
    if COUNT1<30 :
        COUNT=COUNT1
        
    date_chandao=Mysql_db_chandao('tops001','SELECT date FROM changdao_bug_statistics WHERE is_delete=0 ORDER BY date  LIMIT '+str(COUNT1-COUNT)+','+str(COUNT1)+';')
    
    workbook = xlsxwriter.Workbook('D:/chandao/chandao_burn_down_chart.xls')    #创建一个Excel文件
    worksheet = workbook.add_worksheet()    #创建一个工作表对象
    chart = workbook.add_chart({'type': 'line'})    #创建一个图表对象
    #定义数据表头列表
    title = [0]*(COUNT+1)
    title[0]='日期'
    for i in range(1,COUNT+1):
        title[i]=date_chandao[i-1][0]
    #print title
    buname= [u'当天未解决bug数']    #定义频道名称
    data = []
    for i in range(1):
        tmp = []
        for j in range(COUNT):
            tmp.append(int(bug_num[COUNT-j-1][0]))
        data.append(tmp)
    #print data 
    format=workbook.add_format()    #定义format格式对象
    format.set_border(1)    #定义format对象单元格边框加粗(1像素)的格式
    format_title=workbook.add_format()    #定义format_title格式对象
    format_title.set_border(1)   #定义format_title对象单元格边框加粗(1像素)的格式
    format_title.set_bg_color('#cccccc')   #定义format_title对象单元格背景颜色为#cccccc'的格式
    format_title.set_align('center')    #定义format_title对象单元格居中对齐的格式
    format_title.set_bold()    #定义format_title对象单元格内容加粗的格式
    
    format_ave=workbook.add_format()    #定义format_ave格式对象
    format_ave.set_border(1)    #定义format_ave对象单元格边框加粗(1像素)的格式
    format_ave.set_num_format('0.00')   #定义format_ave对象单元格数字类别显示格式
    #下面分别以行或列写入方式将标题、业务名称、流量数据写入起初单元格，同时引用不同格式对象
    worksheet.write_row('A1',title,format_title)  
    worksheet.write_column('A2', buname,format)
    worksheet.write_row('B2', data[0],format)
    worksheet.set_column('A:A', 20)#设置列宽
    worksheet.set_column('B:'+xf(COUNT+1), 10)#设置列宽
    '''
    worksheet.write_row('B3', data[1],format)
    worksheet.write_row('B4', data[2],format)
    worksheet.write_row('B5', data[3],format)
    worksheet.write_row('B6', data[4],format)
    '''
    #定义图表数据系列函数
    #print xf(COUNT+1)
    def chart_series(cur_row):
        '''
        worksheet.write_formula('I'+cur_row, \
         '=AVERAGE(B'+cur_row+':H'+cur_row+')',format_ave)    #计算（AVERAGE函数）频#道周平均流量
        '''
        chart.add_series({
            
            'categories': '=Sheet1!$B$1:$'+xf(COUNT+1)+'$1',    #(X轴)
            'values':     '=Sheet1!$B$'+cur_row+':$'+xf(COUNT+1)+'$'+cur_row,    #频道一周所有数据作
                                                                   #为数据区域
            'line':       {'color': '#4A4AFF'},    #线条颜色定义为black(黑色)
            #'line':       {'color': 'black'},    #线条颜色定义为black(黑色)
            'name': '=Sheet1!$A$'+cur_row,    #引用业务名称为图例项
        })
    
    for row in range(2, 3):    #数据域以第2～3行进行图表数据系列函数调用
        chart_series(str(row))
    
    chart.set_size({'width': (COUNT+1)*70, 'height': 287})    #设置图表大小
    chart.set_title ({'name': u'销冠bug燃尽图'})    #设置图表（上方）大标题
    chart.set_y_axis({'name': '未解决bug数'})    #设置y轴（左侧）小标题
     
    worksheet.insert_chart('A8', chart)    #在A8单元格插入图表
    workbook.close()    #关闭Excel文档
    return 'OK'

def chandao_email(Addressee,to_list,file1,file2,Subject,text):
    #创建一个带附件的实例
    msg = MIMEMultipart('')
    #构造附件1
    att1 = MIMEText(open(file1, 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="chandao_burn_down_chart.xls"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)
    #构造附件2
    att2 = MIMEText(open(file2, 'rb').read(), 'base64', 'gb2312')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="changdao_'+timenow()[:8]+'.xls"'
    msg.attach(att2)
    #加邮件头
    msg['to'] = Addressee
    #msg['cc']='lvjunjie2757@tops001.com,lvjunjie84@163.com'
    #to_list=['lvjunjie2757@tops001.com''lvjunjie84@163.com']
    to_list=to_list
    msg['from'] = 'lvjunjie2757@tops001.com'
    msg['Subject'] = Header(Subject, 'utf-8')
    #part = MIMEText(TEXT, 'plain', 'utf-8')
    text=text
    msg.attach(MIMEText(text,'html', 'utf-8')) 
    #发送邮件
    try:
        server = smtplib.SMTP()
        server.connect('smtp.exmail.qq.com')
        server.login('lvjunjie2757@tops001.com','Larh7oOz8g74bJ9O')#XXX为用户名，XXXXX为密码
        server.sendmail(msg['from'], to_list,msg.as_string())
        server.quit()
        return 'Send success'
    except Exception, e:  
        return str(e)
def text_email(a1,a2):
    text_email='<html><body><h1>Hi all!<br>         截止当前，禅道剩余bug未解决数量共：<span style="font-family:verdana;color:red">'+str(a1)+'个，</span></h1>其中<br><table border=1>'+str(a2)+'</table><h4>具体详情及每日bug燃尽图见附件，请知悉，谢谢！</h4><br><br>      (数据来源：http://chandao.apitops.com/product-all-34.html，请各位将发现bug提到禅道上，并且及时关闭已解决bug)'
    return text_email
def chandao_today():
    return 'D:/chandao/changdao_'+timenow()[:8]+'.xls','Tops001_禅道bug 统计'+timenow()[:8]
def chandao_find(str1,Separator1,Separator2):
    Separator3='全部产品'
    #print str1
    
    #print len(str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines())#项目总数
    projectinfo=['']*(len(str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines())-1)
    #print projectinfo
    bugnum=['']*(len(str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines())-1)
    #print str1.find(Separator)
    #print str1.rfind(Separator)
    #return str1[str1.find(Separator):str1.rfind(Separator)]
    #print str1.splitlines()[2]
    #workbook = xlrd.open_workbook('F:11111.xls')
    #sheet1 = workbook.sheet_by_name('禅道今日bug数量统计')
    file1 = xlwt.Workbook()
    sheet_1 = file1.add_sheet(u'禅道今日bug数量统计', cell_overwrite_ok=True) #创建sheet
    sheet_2 = file1.add_sheet(u'历史bug统计', cell_overwrite_ok=True) #创建sheet

    for i in range(1, len(str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines())):
        line= str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines()[i]
        #line=str1[str1.find(Separator3,0)+len(Separator3)+1:].splitlines()[i]
        sheet_1.write(i, 0, str(line.split(' ')[0]))
        print "line=    "+line
        sheet_1.write(i, 1, str(line.split(' ')[1]))
        projectinfo[i-1]=str(line.split(' ')[1])
        bugnum[i-1]=str(line.split(' ')[9])
        #print bugnum[i-1]
        #print projectinfo[i-1]
    #写入excel第一行（标题）
    title=['ID','产品名称','激活需求','已变更需求','草稿需求','已关闭需求','计划数','发布数','相关BUG','未解决','未指派']
    for j in range(0,len(title)):
        
        line=str1[str1.find(Separator3,0)+len(Separator3)+1:].splitlines()[0]
        #print str(line.split(' ')[j])
        #sheet_1.write(0, j, str(line.split(' ')[j]))
        sheet_1.write(0, j, title[j])

        
    sum=0#统计未解决bug总数
    for ii in range(1,len(str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines())):
        line= str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines()[ii]
        #print line
        for jj in range(2,len(line.split(' '))):
            #print line.split(' ')[jj]
            if jj == len(line.split(' '))-2 :
                #print jj
                #print 'aaaaaa='+str(int(line.split(' ')[jj]))
                sum=sum+(int(line.split(' ')[jj]))
            sheet_1.write(ii, jj, int(line.split(' ')[jj])) 
            sheet_1.write(len(str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines()),jj,xlwt.Formula('SUM('+xf(jj+1)+'2:'+xf(jj+1)+str(len(str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines()))+')'))
        #print 'sum='+str(sum)
        sheet_1.write(len(str1[str1.find(Separator1):str1.rfind(Separator2)].splitlines()),len(line.split(' ')),sum)
    file1.save('D:/chandao/changdao_'+timenow()[:8]+'.xls') 
    Mysql_db_chandao('tops001','UPDATE  changdao_bug_statistics set is_delete=1 WHERE date='+timenow()[:8])
    Mysql_db_chandao('tops001','INSERT INTO changdao_bug_statistics (bug_num,date,createtime,systime,is_delete) VALUES ('+str(sum)+','+timenow()[:8]+',SYSDATE(),SYSDATE(),0)')
    project_info=''
    project_info1=''
    project_info2=''
    #print projectinfo[1]
    for i in range(0,len(projectinfo)):
        if bugnum[i] != '0':#过滤bug数量为0的项目，不写入邮件正文中
            project_info1=project_info1+'<td>'+projectinfo[i]+'</td>'
            project_info2=project_info2+'<td>'+bugnum[i]+'</td>'
            
            #print projectinfo[i]+':'+bugnum[i]+','
            project_info=project_info+projectinfo[i]+' : '+bugnum[i]+'个，  '
        
    project_info1='<tr>'+project_info1+'</tr>'
    project_info2='<tr>'+project_info2+'</tr>'
    project_info=project_info1+project_info2
    #project_info=project_info[:-5]+'。'
    return sum,project_info

def sign_v4(host,query,Body,Date):
    AppKeySecret = '374fa3ab6b1fae595db5382afe415bce'
    
    if Body == '':
        Body_md5 = '00000000000000000000000000000000'

    else:
        #print Body
        Body = md5.new(Body)
        Body_md5 = Body.hexdigest()
    
    str1 = host + query
    #print str1.lower()
    
    si = str1.lower() + Body_md5 + Date + AppKeySecret
    #print 'si=================='+si
    sign_v4 = md5.new()
    sign_v4.update(si)
    return 'v4:'+sign_v4.hexdigest(),Date
#print sign_v4('gateway.test.apitops.com','/oauth/Authorization/Login','{\"agent\":android,\"appcode\":app_broker,\"loginName\":15157163734,\"password\":\"83b4ef5ae4bb360c96628aecda974200\"}','Sun, 19 Feb 2017 11:49:40 GMT+0800')

def time_gmt():
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    time_gmt = datetime.datetime.now().strftime(GMT_FORMAT)+'+0800'
    #print time_gmt
    return time_gmt
print time_gmt()
def dictionary_to_jsonstr(str_dictionary={}):
    #print str(str_dictionary)
    #print str_dictionary.keys()
    str_json='{'
    for i in range(0,len(str_dictionary)):
        if type(str_dictionary[str_dictionary.keys()[i]]) is str:   
            str_json = str_json+'\"'+str_dictionary.keys()[i]+'\":'+'\"'+str(str_dictionary[str_dictionary.keys()[i]])+'\",'
        else:
            str_json = str_json+'\"'+str_dictionary.keys()[i]+'\":'+str(str_dictionary[str_dictionary.keys()[i]])+','
        
    str_json=str_json[:-1]+'}'
    return str_json

def dictionary_to_form(str_dictionary={}):
    #print str(str_dictionary)
    #print str_dictionary.keys()
    str_json=''
    for i in range(0,len(str_dictionary)):
  
        str_json = str_json+str_dictionary.keys()[i]+'='+str(str_dictionary[str_dictionary.keys()[i]])+'&'

        
    str_json=str_json[:-1]+''
    return str_json

def rf_re(str,re1,id=1):
    re_str = re.findall(re1, str)  
    return re_str[0][id-1]
    
d = {'first':'One','second':2}
print dictionary_to_form(d)
p = rf_re('https://gateway.test.apitops.com','^http(s)?://(.+)$',2)
print p
#print dictionary_to_jsonstr(d)
    
#a="更多\n未关闭的产品\n日结 0 0 0 0 0 50 5\n用户中心 0 0 0 0 0 0 0\n数据修改通道 0 0 0 0 0 14 1\n房产销冠4.0 1 0 0 0 0 217 87\n新组织架构 0 0 0 0 0 74 2\n有序结佣 0 0 0 0 0 55 3\n钱包 0 0 1 0 0 1 0\n财务oa 0 0 0 0 0 2 0\n保理回款产品 0 0 0 0 0 198 3\nKber 3 0 0 0 0 339 6\n装修贷 0 0 0 0 0 5 0\n装修撮合 0 0 0 0 0 21 2\n楼盘合同管理 0 0 0 0 0 52 3\n交易管理系统 0 0 1 0 0 132 5\n销冠经纪4.0 2 0 0 0 0 228 41\n产品名称 激活 已变更 草稿 计划数 发布数 相关BUG 未解决\n更多\n指派给我的需求\nID P 需求名称 预计 状态 阶段\n20161004 13:06:35.036 :  INFO : Slept 500 milliseconds\nEnding test:   Club New Test.禅道Bug统计.禅道bug统计"


#a="a=新增产品\n未关闭\n结束\n全部产品\nID\n产品名称\n激活需求 已变更需求 草稿需求 已关闭需求 计划数 发布数 相关BUG 未解决 未指派\n排序\n053 销冠经纪重构 0 0 0 0 0 0 0 0 0\n052 快速结佣 0 0 0 0 0 0 15 0 0\n051 数据中心 0 0 0 0 0 0 31 1 0\n050 自动化项目管理及发布 0 0 0 0 0 0 1 0 0\n049 日结 0 0 0 0 0 0 56 2 0\n048 用户中心 0 0 0 0 0 0 0 0 0\n047 数据修改通道 0 0 0 0 0 0 14 1 0\n046 房产销冠4.0 1 0 0 0 0 0 1116 70 0\n045 新组织架构 0 0 0 0 0 0 82 6 0\n044 有序结佣 0 0 0 0 0 0 55 2 0\n043 钱包 0 0 1 0 0 0 1 0 0\n042 财务oa 0 0 0 0 0 0 2 0 0\n041 保理回款产品 0 0 0 0 0 0 244 0 0\n040 Kber 3 0 0 0 0 0 339 6 0\n039 装修贷 0 0 0 0 0 0 5 0 0\n038 装修撮合 0 0 0 0 0 0 21 2 0\n037 楼盘合同管理 0 0 0 0 0 0 51 1 0\n035 交易管理系统 0 0 1 0 0 0 130 3 0\n034 销冠经纪4.0 2 0 0 0 0 0 282 32 1\n002 卡考OA 9 0 10 191 0 0 155 5 1\n013 积分商城 0 0 0 13 0 0 54 0 0\n001 销冠经纪(android) 41 0 7 82 0 0 346 17 1\n026 销冠经纪(ios) 8 0 33 18 0 0 137 22 0\n008 经纪公司CRM 8 0 5 9 0 0 28 4 0\n004 销冠Club 0 0 0 30 0 0 1384 24 0\n009 理财产品 6 0 39 5 0 1 268 7 0\n024 销冠管家 0 0 0 1 0 0 677 9 0\n017 Oauth 1 0 0 0 0 0 41 4 2\n028 组织架构与权限 0 0 0 0 0 2 487 25 0\n011 卡考中国数据 1 0 0 0 0 0 5 0 0\n015 安全测试 0 0 0 0 0 0 472 181 1\n014 app_TC_基线 0 0 0 0 0 0 0 0 0\n030 首付贷 0 0 0 0 0 0 113 9 0\n选择\n批量编辑\n共 33 条记录，每页 100 条\n1/1  "
#print a
#print chandao_find(a,'排序','选择')
#print text_email(chandao_find(a,' 未解决 未指派','共 ')[0],chandao_find(a,' 未解决 未指派','共 ')[1])
#print chandao_burn_down_chart()
#print chandao_email('188556051@qq.com',['lvjunjie84@163.com','lvjunjie2757@tops001.com'],'D:/chandao/chandao_burn_down_chart.xls','D:/chandao/changdao_20161007.xls','Tops001_bug燃尽图',text_email(chandao_find(a,' 未解决 未指派','共 ')[0],chandao_find(a,' 未解决 未指派','共 ')[1]))

#print a[26:532]
 
#print rf_linux('121.41.5.216',22,'root','a1478520B','ls /home')
#print timenow()

#GMT = '%a, %d %b %Y %H:%M:%S GMT+0800'
#print base64_Image('E:/Image/1.jpg')

#print Keywords_get('添加话题接口','/club/api/v4/topic/add','brokerId,postGid')
#print chandao_today()
#D:/chandao/changdao_20161009.xls
#a='agent=android&appcode=app_broker&loginName=15157163734&password=83b4ef5ae4bb360c96628aecda974200'

