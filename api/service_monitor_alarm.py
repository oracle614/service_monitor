from flask import request
from flask_restful import Resource
from db.db_result import DBResult
from common.utils import DateFormat
from common.alarm import Alarm
date_format = DateFormat()
db_result = DBResult()
alram = Alarm()


class Alarm(Resource):

    def post(self):
        try:
            failed_count = request.json['failed_count']
            time = request.json['time']
            alarm_level = int(request.json['alarm_level'])
            product_id = request.json['product_id']
            data = request.json['data']

            if alarm_level == 1:
                # 发送邮件
                receivers = data['receivers']
                subject = data['subject']
                message = data['message']
                return alram.send_email(receivers, subject, message)

            elif alarm_level == 2:
                # 打电话
                pass

            else:
                return {"code":1, "msg": "error alarm_level"}




        except:
            pass

