# /data     Calls the microservice
# /readme 
# /info       Defines the service
# /train
import json
import pytest
import requests
from flask import request
from service import service


# from service import service
# from src.adapter_transportation import from_json
from src.__pytest__.conftest import client


def test_readme_flask():        
    response = service.test_client().get('/readme')

    assert response.status_code == 200

def test_info_flask():        
    response = service.test_client().get('/info')

    assert response.status_code == 200

def test_data_flask():        
    response = service.test_client().get('/data')

    assert response.status_code == 200