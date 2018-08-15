from flask import Flask
from flask_restful import Api
from api.service_monitor_result import PassResult, FailResult
from api.service_monitor_alarm import Alarm
app = Flask(__name__)
api = Api(app)


api.add_resource(PassResult, '/monitor/passresult')
api.add_resource(FailResult, '/monitor/failresult')
api.add_resource(Alarm, '/monitor/alarm')