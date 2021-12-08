import pytest

import pandas as pd
from src.adapter_transportation import MIAdapter
from src.model_training import TrainModel

def test_that_trainer_dont_crash_when_reading_tnm_as_dataframe (mocker, fake_dataframe):
    mock = mocker.patch("src.model_training.joblib", return_value=None)
    # arrange
    model = TrainModel(fake_dataframe)
    # act
    model.train_model()
    #assert
    mock.dump.assert_called_once()
    
  

def test_that_trainer_produces_a_model(fake_dataframe):
    # arrange 
    
    # act

    # assert
    assert True


