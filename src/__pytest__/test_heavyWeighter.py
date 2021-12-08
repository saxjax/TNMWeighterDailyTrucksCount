import joblib
import pytest
from src.heavy_weighter import predict_heavy_traffic, train_model_on_TNM
from src.__pytest__.conftest import fake_json

def test_that_predicter_predicts_dailyTrucks (fake_dataframe):
    
    
    #arrange
    model = joblib.load('decision_tree_model.joblib')
    pre_predict = fake_dataframe['daily_10_axle'].tolist()

    #act
    predicted_dataframe = model.predict(fake_dataframe)

    post_predict = predicted_dataframe['daily_10_axle'].tolist()
    print(pre_predict)
    print(post_predict)
    #assert
    assert pre_predict != post_predict

# @pytest.mark.parametrize('tnm',[
# (fake_json),
# ])
# def test_that_predicter_only_predicts_on_undefined_data (tnm):
#     # kun værdier som ikke allerede findes i data må predictes.    
#     # # arrange 
    
#     # act
#     actual = predict_heavy_traffic(tnm)


#     # assert
#     assert True

# def test_that_prediction_is_above_0(tnm):
#     assert True

# def test_that_prediction_is_below_max_daily_trucks(tnm):
#     assert True