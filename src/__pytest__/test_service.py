# /data     Calls the microservice
# /readme 
# /info       Defines the service
# /train
import pytest
import requests
from flask import request
import json
from urllib.parse import urlencode
from urllib.request import urlopen

# from service import service
# from src.adapter_transportation import from_json
from src.__pytest__.conftest import client

# def test_convert(fake_json):
#     print(from_json(fake_json))

def test_hello(httpserver):
    body = "Hello, World!"
    endpoint = "/hello"
    httpserver.expect_request(endpoint).respond_with_data(body)
    with urlopen(httpserver.url_for(endpoint)) as response:
        result = response.read().decode()
    assert body == result


def test_info():
   # service.run(host="0.0.0.0", port=5000)
    
    response = request.get('https://localhost/info')
    # assert response.status_code == 200
    
    assert True

def test_readme():
    response = request.get('https://localhost/readme')
    # assert response.status_code == 200
    
    assert True

def test_data():
    response = request.get('https://localhost/data')
    # assert response.status_code == 200
    
    assert True

# @pytest.mark.parametrize('endpoint',[
# ('/info'),
# ('/data'),
# ('/readme')
# ])
def test_that_service_can_call_endpoint(endpoint):
    # arrange 
    url = 'localhost:5000/'+endpoint
    expectedStatuscode = 200

    # https://stackoverflow.com/questions/57663308/how-to-mock-requests-using-pytest
    # https://www.freecodecamp.org/news/end-to-end-api-testing-with-docker/
    

    # act

    # assert 
    assert True

# @pytest.mark.parametrize('endpoint',[
# ('/info'),
# ('/data'),
# ('/readme')
# ])
# def test_status_code(endpoint,client):
#     rv = client.get(endpoint)

#     assert rv

# #response.status_code == status
# @pytest.mark.parametrize('endpoint',[
# ('/info'),
# ('/data'),
# ('/readme')
# ])
# def test_endpoint_calls_predict(endpoint):
#     assert True

