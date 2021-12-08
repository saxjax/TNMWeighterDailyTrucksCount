import json
import joblib
import pandas as pd
import pytest
from src.enhancer_microservice import Enhancer
from src.heavy_weighter import predict_heavy_traffic, train_model_on_TNM
from src.__pytest__.conftest import fake_json

def test_that_predicter_predicts_dailyTrucks (fake_json,fake_dataframe):
    #arrange
    pre_dataframe = pd.DataFrame(fake_dataframe)
    
    before_predictions_on_daily_trucks = pre_dataframe['daily_trucks'].tolist()
    
    #prepare for predicter, by removing theese columns
    pre_dataframe_dropped_columns = pre_dataframe.drop(columns=['max_axle_load', 'max_height','max_weight', 'max_length', 'recommended_speed', 'mean_speed','daily_trucks'])

    #the trained model found in the filesystem
    model = joblib.load('decision_tree_model.joblib')
    

    #act
    predicted_dataframe = model.predict(pre_dataframe_dropped_columns)
    after_predictions_on_daily_trucks = predicted_dataframe.tolist()
    with pd.option_context('display.max_rows', None, 'display.max_columns', pre_dataframe.shape[1]):
        print("dataframe used for predictions:\n",pre_dataframe)
        print("the  daily_trucks before predictions:\n",before_predictions_on_daily_trucks)
        print("the predicted daily_trucks after predictions:\n",predicted_dataframe)
    #assert
    assert after_predictions_on_daily_trucks != before_predictions_on_daily_trucks
    assert False

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