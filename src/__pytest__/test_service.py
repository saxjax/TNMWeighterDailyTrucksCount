# /data     Calls the microservice
# /readme 
# /info       Defines the service
# /train
import pytest
# from src.adapter_transportation import from_json

from src.__pytest__.conftest import client

# def test_convert(fake_json):
#     print(from_json(fake_json))


@pytest.mark.parametrize('endpoint',[
('/info'),
('/data'),
('/readme')
])
def test_that_service_can_call_endpoint(endpoint):
    # arrange 
    url = 'localhost:5000/'+endpoint
    expectedStatuscode = 200

    # https://stackoverflow.com/questions/57663308/how-to-mock-requests-using-pytest
    # https://www.freecodecamp.org/news/end-to-end-api-testing-with-docker/
    

    # act

    # assert 
    assert True

@pytest.mark.parametrize('endpoint',[
('/info'),
('/data'),
('/readme')
])
def test_status_code(endpoint,client):
    rv = client.get(endpoint)

    assert rv

#response.status_code == status
@pytest.mark.parametrize('endpoint',[
('/info'),
('/data'),
('/readme')
])
def test_endpoint_calls_predict(endpoint):
    assert True

