from flask import request
from flask_restful import Resource
from db.db_result import DBResult
from db.db_log import DBLog
from common.utils import DateFormat
from common.alarm import Alarm
date_format = DateFormat()
db_result = DBResult()
db_log = DBLog()
alram = Alarm()


class Alarm(Resource):

    def post(self):
        try:
            failed_count = request.json['failed_count']
            time = request.json['time']
            alarm_level = int(request.json['alarm_level'])
            product_id = request.json['product_id']
            data = request.json['data']
            print(failed_count,time,alarm_level,product_id,data)

            get_failed_count = db_log.get_failed_count(product_id=product_id, start_time=date_format.time_add(time), end_time=date_format.time_now())
            if get_failed_count < failed_count:
                return {'code': 0, 'msg': 'No alarm is required'}
            else:
                if alarm_level == 1:
                    # 发送邮件
                    receivers = data['receivers']
                    subject = data['subject']
                    message = data['message']
                    return {"code":0, "msg": alram.send_email(receivers, subject, message)}

                elif alarm_level == 2:
                    # 打电话
                    pass

                else:
                    return {"code":1, "msg": "error alarm_level"}
        except:
            return {"code":1,"message":"error"}

