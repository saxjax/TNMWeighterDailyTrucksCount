import json
from types import TracebackType
from flask import Flask, request,jsonify, render_template, redirect, abort, url_for
from src.__pytest__.conftest import fake_json
from src.heavy_weighter import predict_heavy_traffic, train_model_on_TNM, translate
from src.main import main
from src.adapter_transportation import MIAdapter

service = Flask(__name__)

@service.route('/')
def hello():
    tnm = {'text':'heavy weighter'}
    return tnm

@service.route("/readme")
def readme():
    return "readme file"


@service.route('/info')
def info():
    return 'heavyweighter /info'

@service.route('/render')
def render():
    return 'heavyweighter /render'

@service.route("/test", methods=['GET', 'POST'])
def test():
    data = request.data
    if not data:
        return json.dumps("The url was called with no arguments")
    return train_model_on_TNM(data)

@service.route("/train", methods=['GET', 'POST'])
def train():
    data = request.data
    if not data:
        return json.dumps("The url was called with no arguments")
    return train_model_on_TNM(data)

@service.route("/predict", methods=['GET', 'POST'])
def predict():
    data = request.data
    if not data:
        return json.dumps("The url was called with no arguments")
    return predict_heavy_traffic(data)
    

@service.route("/data", methods=['GET', 'POST'])
def master():
    data = request.data
    if not data:
        return json.dumps("The url was called with no arguments")
    return main(data)

@service.route("/translate", methods=['GET', 'POST'])
def transl():
    data = request.data
    if not data:
        return json.dumps("The url was called with no arguments")
    return MIAdapter.from_json(fake_json)
    # return translate(data)

@service.errorhandler(500)
def internal_error(exception):
    print("500 Error caught")
    TracebackType.format_exc()    

if __name__=="__main__":
    service.run(host="0.0.0.0", port=5000)
