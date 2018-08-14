import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import time


class Alarm:
    def send_email(self, receivers, subject, message):
        mail_host = "smtp.exmail.qq.com"  # 设置服务器
        mail_user = "lvjj@xinguangnet.com"  # 用户名
        mail_pass = "VjoiFw9ZHmCLjHnE"  # 口令
        message_to = '<'
        sender = 'lvjj@xinguangnet.com'
        receivers = receivers  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        message = MIMEText(message, 'plain', 'utf-8')
        message['From'] = Header("lvjj@xinguangnet.com", 'utf-8')
        for i in receivers:
            message['To'] = Header(i, 'utf-8')
        subject = subject
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            return "Email sent successfully"
        except smtplib.SMTPException:
            return "Error: Email sent failed"

    def call_phone(self, phone_num):

        d = os.popen("adb devices")
        print(d.read())
        if len(d.read().split('\n')) > 3:
            d = os.popen("adb shell am start -a android.intent.action.CALL tel:{}".format(phone_num))
            print(d.read())
            time.sleep(8)
            d = os.popen("adb  shell  input  keyevent  KEYCODE_ENDCALL")
            print(d.read())
        else:
            return "no deveice"


if __name__ == '__main__':
    alarm = Alarm()
    alarm.send_email(['188556051@qq.com', 'lvjj@xinguangnet.com', 'lvjunjie84@hotmail.com'], '测试主题', '测试内容\n测试内容2')