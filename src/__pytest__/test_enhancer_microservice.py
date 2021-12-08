import json
import pandas as pd
import pytest
from src.adapter_transportation import MIAdapter
from src.enhancer_microservice import Enhancer

# make sure that all data apart from the data we want to predict is filled outfile
# der er måske et problem hvis enhancer køres fra controller og udfylder alle ukendte, for så ved microservicen ikke hvilke data der er groundtruth når der skal predictes.

def test_that_null_values_are_filled (fake_json,fake_json_as_dataframe, ):
    # alle edges skal have en værdi != null og >= 0 på daily trucks,
    # arrange 
    tnm = json.loads(fake_json,strict=False)
    metaData = tnm['meta_data']
    # adapter = MIAdapter(fake_json)
    # frame = adapter.from_json()
    enhancer = Enhancer(metaData)
    comparable_orig_dataframe_values =  fake_json_as_dataframe.drop(columns=['max_axle_load', 'max_height','max_weight', 'max_length', 'recommended_speed', 'mean_speed'])
    # act
    enhancedDataframe =  enhancer.enhance_data_frame(fake_json_as_dataframe)
    with pd.option_context('display.max_rows', None, 'display.max_columns', enhancedDataframe.shape[1]):
        print("enhanced dataframe\n",enhancedDataframe)
    with pd.option_context('display.max_rows', None, 'display.max_columns', comparable_orig_dataframe_values.shape[1]):
        print("original dataframe\n",comparable_orig_dataframe_values)
    assert comparable_orig_dataframe_values.iloc[0]['type'] != enhancedDataframe.iloc[0]['type']
    assert comparable_orig_dataframe_values.iloc[1]['type_max_speed'] != enhancedDataframe.iloc[1]['type_max_speed']
    assert comparable_orig_dataframe_values.iloc[4]['set_max_speed'] != enhancedDataframe.iloc[4]['set_max_speed']
    assert comparable_orig_dataframe_values.iloc[4]['daily_year'] != enhancedDataframe.iloc[4]['daily_year']
    assert comparable_orig_dataframe_values.iloc[6]['daily_trucks'] != enhancedDataframe.iloc[6]['daily_trucks']
    assert comparable_orig_dataframe_values.iloc[6]['daily_10_axle'] != enhancedDataframe.iloc[6]['daily_10_axle']
    # assert comparable_orig_dataframe_values.iloc[6]['fuel_station'] != enhancedDataframe.iloc[6]['fuel_station']


def test_that_the_sequence_of_edges_are_identical (fake_json,fake_json_as_dataframe_changed_id_sequence):
    #arrange
    tnm = json.loads(fake_json,strict=False)
    metaData = tnm['meta_data']
    enhancer = Enhancer(metaData)

    pre_edge_id_order = fake_json_as_dataframe_changed_id_sequence['id'].tolist()

    #act
    enhanced_dataframe =  enhancer.enhance_data_frame(fake_json_as_dataframe_changed_id_sequence)

    post_edge_id_order = enhanced_dataframe['id'].tolist()

    #assert
    assert pre_edge_id_order == post_edge_id_order
