# import json
# from src.adapter_transportation import MIAdapter
# import pytest

#TODO: Combine with data_processer

# def test_adapter_transportation_from_json_deserializes_input_to_dictionary(fake_json):
#     # fake_json is a fixture imported from the conftest.py file
#     adapter = MIAdapter(fake_json)
#     expected = json.loads(fake_json)
    
#     # actual = adapter.from_json(fake_json)
    
#     # assert actual == expected
#     # try:
#     #     adapter.from_json(fake_json)
#     # except:
#     assert True 

# def test_adapter_transportation_to_json_serializes_input_to_json(fake_json):
#     adapter = MIAdapter(fake_json)
#     badvalue = {"Expected": "Value"}
#     value = fake_json
#     badexpected = json.dumps(badvalue)
#     goodexpected = json.dumps(value)
    
#     #actual = adapter.to_json(default=badvalue)
    
#     #assert actual == expected
#     # try:
#     #     adapter.to_json(value)
#     # except:
#     #     assert False
#     assert True
    

