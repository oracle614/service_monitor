from flask import Flask
from flask_restful import Api
from api.service_mock_result import PassResult, FailResult
app = Flask(__name__)
api = Api(app)



api.add_resource(PassResult, '/monitor/passresult')
api.add_resource(FailResult, '/monitor/failresult')
