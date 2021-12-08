import json
from src.adapter_transportation import MIAdapter
import pytest

#TODO: Combine with adaptertest


def test_adapter_transportation_from_json_deserializes_input_to_pandas_dataframe(fake_json, fake_dataframe):
    # fake_json is a fixture imported from the conftest.py file
     adapter = MIAdapter(fake_json)
     fakedf = fake_dataframe
    
     actualdf = adapter.from_json()

     expected = list(fakedf.columns.values)

     actual = list(actualdf.columns.values)

     assert actual == expected
     #assert True
     #try:
      #   adapter.from_json(fake_json)
     #except:
    # assert True 

def test_adapter_transportation_to_json_serializes_input_to_json(fake_json):
    adapter = MIAdapter(fake_json)
    fake_json = json.loads(fake_json,strict=False)
#     adapter.meta_data = fake_json['meta_data']
#     adapter.nodes_data = fake_json['nodes']
#     adapter.vehicle_data = fake_json['vehicle']
    pre_to_json = fake_json
    #TODO: erstat med et mock
    adapter.from_json()

    pre_to_json_weights=[]
    pre_to_json_ids = []
    for node in pre_to_json["nodes"]:
        for edge in pre_to_json["nodes"][node]["edges"]:
            pre_to_json_weights.append(pre_to_json["nodes"][node]["edges"][edge]["weight"])
            pre_to_json_ids.append(pre_to_json["nodes"][node]["edges"][edge]["id"])

    expected = pre_to_json_weights
    fake_prediction={}
    for x in range(len(pre_to_json_weights)):
        edgeid=pre_to_json_ids[x]
        fake_prediction[str(edgeid)]= x+1
    post_to_json = adapter.to_json(fake_prediction)
    
    
    post_to_json_weights=[]
    for node in post_to_json["nodes"]:
        for edge in post_to_json["nodes"][node]["edges"]:
            post_to_json_weights.append(post_to_json["nodes"][node]["edges"][edge]["weight"])
    
    actual = post_to_json_weights

    assert actual != expected
    # assert True
    