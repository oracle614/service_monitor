from flask import request
from flask_restful import Resource
from db.db_result import DBResult
from common.utils import DateFormat
date_format = DateFormat()
db_result = DBResult()


class PassResult(Resource):
    def post(self):
        try:
            product_id = request.json['product_id']
            tc_name = request.json['tc_name']
            date = date_format.date_now()
            print(product_id, tc_name, date)
            res = db_result.pass_update(product_id=product_id, tc_name=tc_name, date=date)
            return {"code": 0, "msg": res}
        except:
            return {"code": 1, "msg": "error operation"}

    def get(self):
        try:
            product_id = request.args['product_id']
            tc_name = request.args['tc_name']
            date = date_format.date_now()
            res = db_result.get_pass_count(product_id=product_id,tc_name=tc_name, date=date)
            return {"code": 0, "msg": res}
        except:
            return {"code": 1, "msg": "error operation"}


class FailResult(Resource):
    def post(self):
        try:
            product_id = request.json['product_id']
            tc_name = request.json['tc_name']
            date = date_format.date_now()
            res = db_result.fail_update(product_id=product_id, tc_name=tc_name, date=date)
            return {"code": 0, "msg": res}
        except:
            return {"code": 1, "msg": "error operation"}

    def get(self):
        try:
            product_id = request.args['product_id']
            tc_name = request.args['tc_name']
            date = date_format.date_now()
            res = db_result.get_fail_count(product_id=product_id, tc_name=tc_name, date=date)
            return {"code": 0, "msg": res}
        except:
            return {"code": 1, "msg": "error operation"}