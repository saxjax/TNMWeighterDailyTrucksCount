import json
from src.main import main

def test_integration_of_whole_service(mocker,enhanced_fake_json, annotated_fake_json):
    # mock = mocker.patch("src.model_training.joblib", return_value=None)

    unannotated = json.loads(enhanced_fake_json, strict=False)
    annotated = json.loads(annotated_fake_json, strict=False)


    actual = main(enhanced_fake_json)

    assert len(actual['nodes']) == len(unannotated['nodes'])  
    assert actual['nodes']['1']['edges']['1']['weight'] != unannotated['nodes']['1']['edges']['1']['weight']
    assert actual['nodes']['1']['edges']['2']['weight'] != unannotated['nodes']['1']['edges']['2']['weight']
    assert actual['nodes']['3']['edges']['3']['weight'] != unannotated['nodes']['3']['edges']['3']['weight']
    assert actual['nodes']['3']['edges']['4']['weight'] != unannotated['nodes']['3']['edges']['4']['weight']
    assert actual['nodes']['4']['edges']['5']['weight'] != unannotated['nodes']['4']['edges']['5']['weight']
    assert actual['nodes']['4']['edges']['6']['weight'] != unannotated['nodes']['4']['edges']['6']['weight']
    assert actual['nodes']['4']['edges']['7']['weight'] != unannotated['nodes']['4']['edges']['7']['weight']

    assert actual['nodes']['1']['edges']['1']['weight'] == annotated['nodes']['1']['edges']['1']['weight']
    assert actual['nodes']['1']['edges']['2']['weight'] == annotated['nodes']['1']['edges']['2']['weight']
    assert actual['nodes']['3']['edges']['3']['weight'] == annotated['nodes']['3']['edges']['3']['weight']
    assert actual['nodes']['3']['edges']['4']['weight'] == annotated['nodes']['3']['edges']['4']['weight']
    assert actual['nodes']['4']['edges']['5']['weight'] == annotated['nodes']['4']['edges']['5']['weight']
    assert actual['nodes']['4']['edges']['6']['weight'] == annotated['nodes']['4']['edges']['6']['weight']
    assert actual['nodes']['4']['edges']['7']['weight'] == annotated['nodes']['4']['edges']['7']['weight']

    