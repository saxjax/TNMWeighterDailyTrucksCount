# /data     Calls the microservice
# /readme 
# /info       Defines the service
# /train
import json
import pytest
import requests
from flask import request
from pytest_httpserver import HTTPServer



# from service import service
# from src.adapter_transportation import from_json
from src.__pytest__.conftest import client



def test_info(httpserver: HTTPServer):# tester om /info statuscode == 200 hvis den får strengen heavyweighter /info
    httpserver.expect_request("/info").respond_with_data("heavyweighter /info")
    assert requests.get(httpserver.url_for("/info")).status_code == 200#### test hvad der kommer tilbage i forhold til service.py filen

def test_readme(httpserver: HTTPServer):#tester om /readme status code == 200 hvis den får strengen readme file
    httpserver.expect_request("/readme").respond_with_data("readme file")
    assert requests.get(httpserver.url_for("/readme")).status_code == 200#### test hvad der kommer tilbage i forhold til service.py filen

def test_data(httpserver: HTTPServer):#tester om json er identiske 
    httpserver.expect_request("/data").respond_with_json({"foo": "bar"})
    assert requests.get(httpserver.url_for("/data")).json() == {'foo': 'bar'}

def test_data_with_fake_json(httpserver: HTTPServer, fake_json):#tester om json er identiske 
    httpserver.expect_request("/data").respond_with_json(fake_json)
    assert requests.get(httpserver.url_for("/data")).json() == fake_json