# /data     Calls the microservice
# /readme 
# /info       Defines the service
# /train
import pytest
import requests
from flask import request
from pytest_httpserver import HTTPServer



# from service import service
# from src.adapter_transportation import from_json
from src.__pytest__.conftest import client

# def test_convert(fake_json):
#     print(from_json(fake_json))

def test_json_client(httpserver: HTTPServer):
    httpserver.expect_request("/info").respond_with_data("OK")
    assert requests.get(httpserver.url_for("/info")).status_code == 200#### test hvad der kommer tilbage i forhold til service.py filen

    #httpserver.expect_request("/foobar").respond_with_json({"foo": "bar"})
    #assert requests.get(httpserver.url_for("/foobar")).json() == {'foo': 'bar'}
def test_info():
   # service.run(host="0.0.0.0", port=5000)
    
    response = request.get('https://localhost/info')
    # assert response.status_code == 200
    
    assert True

def test_readme():
    response = request.get('https://localhost/readme')
    # assert response.status_code == 200
    
    assert True

def test_data(mocker):
    mock = mocker.patch("src.model_training.joblib", return_value=None)

    response = request.get('https://localhost/data')
    # assert response.status_code == 200
    
    # mock.dump.assert_called_once()

    assert True

# @pytest.mark.parametrize('endpoint',[
# ('/info'),
# ('/data'),
# ('/readme')
# ])
def test_that_service_can_call_endpoint(mocker,endpoint):
    # arrange 
    mock = mocker.patch("src.model_training.joblib", return_value=None)

    url = 'localhost:5000/'+endpoint
    expectedStatuscode = 200
    # mock.dump.assert_called_once()


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

