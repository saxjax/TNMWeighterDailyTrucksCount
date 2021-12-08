from numpy import False_
import pytest
import json
import pandas as pd


@pytest.fixture
def fake_json():
    python_dict = {
    "meta_data": {
        "max_length": 3778,
        "min_length": 1,
        "max_slope": 24.527,
        "min_slope": -2.407,
        "max_legal_speed": 80,
        "min_recommended_speed": 0,
        "max_mean_speed": 0,
        "min_mean_speed": 0,
        "max_daily_year": 16138.0,
        "min_daily_year": 57.5,
        "max_daily_july": 14813.0,
        "min_daily_july": 51.5,
        "max_daily_trucks": 2472.0,
        "min_daily_trucks": 87.0
    },
    "vehicle": {
        "id": 1,
        "name": "Fiat multipla",
        "data": {
            "top_speed": 150,
            "mileage": 13204.03,
            "max_fuel": 4.3
        }
    },
    "nodes": {
        "1": {
            "id": 1,
            "weight": 0.0,
            "data": {
                "longitude": 15.9550166585396,
                "latitude": 57.1940874759639,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "null",
                "signal_control": True
            },
            "edges": {
                "1": {
                    "id": 1,
                    "from_node_id": 1,
                    "to_node_id": 3,
                    "weight": 0.0,
                    "data": {
                        "length": 162,
                        "slope": "null",
                        "type": "null",
                        "type_max_speed": "null",
                        "set_max_speed": "null",
                        "recommended_speed": "null",
                        "mean_speed": "null",
                        "daily_year": "null",
                        "daily_july": "null",
                        "daily_trucks": "null",
                        "daily_10_axle": "null",
                        "fuel_station": False,
                        "max_axle_load": "null",
                        "max_height": "null",
                        "max_length": "null",
                        "max_weight": "null"
                    }
                },
                "2": {
                    "id": 2,
                    "from_node_id": 1,
                    "to_node_id": 3,
                    "weight": 0.0,
                    "data": {
                        "length": 151,
                        "slope": "null",
                        "type": "null",
                        "type_max_speed": "null",
                        "set_max_speed": "null",
                        "recommended_speed": "null",
                        "mean_speed": "null",
                        "daily_year": "null",
                        "daily_july": "null",
                        "daily_trucks": "null",
                        "daily_10_axle": "null",
                        "fuel_station": False,
                        "max_axle_load": "null",
                        "max_height": "null",
                        "max_length": "null",
                        "max_weight": "null"
                    }
                }
            }
        },
        "2": {
            "id": 2,
            "weight": 0.0,
            "data": {
                "longitude": 16.2145174943897,
                "latitude": 56.9771748846184,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": False
            },
            "edges": {}
        },
        "3": {
            "id": 3,
            "weight": 0.0,
            "data": {
                "longitude": 15.5891433415976,
                "latitude": 56.9609130669128,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "null",
                "signal_control": "null"
            },
            "edges": {
                "3": {
                    "id": 3,
                    "from_node_id": 3,
                    "to_node_id": 1,
                    "weight": 0.0,
                    "data": {
                        "length": 302,
                        "slope": "-0.23899999999999988",
                        "type": "null",
                        "type_max_speed": "null",
                        "set_max_speed": "null",
                        "recommended_speed": "null",
                        "mean_speed": "null",
                        "daily_year": "null",
                        "daily_july": "null",
                        "daily_trucks": "null",
                        "daily_10_axle": "null",
                        "fuel_station": False,
                        "max_axle_load": "null",
                        "max_height": "null",
                        "max_length": "null",
                        "max_weight": "null"
                    }
                },
                "4": {
                    "id": 4,
                    "from_node_id": 3,
                    "to_node_id": 1,
                    "weight": 0.0,
                    "data": {
                        "length": 39,
                        "slope": "null",
                        "type": "null",
                        "type_max_speed": "null",
                        "set_max_speed": "null",
                        "recommended_speed": "null",
                        "mean_speed": "null",
                        "daily_year": "null",
                        "daily_july": "null",
                        "daily_trucks": "null",
                        "daily_10_axle": "null",
                        "fuel_station": False,
                        "max_axle_load": "null",
                        "max_height": "null",
                        "max_length": "null",
                        "max_weight": "null"
                    }
                }
            }
        },
        "4": {
            "id": 4,
            "weight": 0.0,
            "data": {
                "longitude": 15.7367147390899,
                "latitude": 57.0368169072154,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": False
            },
            "edges": {
                "5": {
                    "id": 5,
                    "from_node_id": 4,
                    "to_node_id": 3,
                    "weight": 0.0,
                    "data": {
                        "length": 168,
                        "slope": "null",
                        "type": "null",
                        "type_max_speed": "null",
                        "set_max_speed": "null",
                        "recommended_speed": "null",
                        "mean_speed": "null",
                        "daily_year": "null",
                        "daily_july": "null",
                        "daily_trucks": "null",
                        "daily_10_axle": "null",
                        "fuel_station": False,
                        "max_axle_load": "null",
                        "max_height": "null",
                        "max_length": "null",
                        "max_weight": "null"
                    }
                },
                "6": {
                    "id": 6,
                    "from_node_id": 4,
                    "to_node_id": 1,
                    "weight": 0.0,
                    "data": {
                        "length": 55,
                        "slope": "null",
                        "type": "null",
                        "type_max_speed": "null",
                        "set_max_speed": "null",
                        "recommended_speed": "null",
                        "mean_speed": "null",
                        "daily_year": "null",
                        "daily_july": "null",
                        "daily_trucks": "null",
                        "daily_10_axle": "null",
                        "fuel_station": False,
                        "max_axle_load": "null",
                        "max_height": "null",
                        "max_length": "null",
                        "max_weight": "null"
                    }
                },
                "7": {
                    "id": 7,
                    "from_node_id": 7,
                    "to_node_id": 4,
                    "weight": 0.0,
                    "data": {
                        "length": 40,
                        "slope": "null",
                        "type": "null",
                        "type_max_speed": "null",
                        "set_max_speed": "null",
                        "recommended_speed": "null",
                        "mean_speed": "null",
                        "daily_year": "null",
                        "daily_july": "null",
                        "daily_trucks": "null",
                        "daily_10_axle": "null",
                        "fuel_station": False,
                        "max_axle_load": "null",
                        "max_height": "null",
                        "max_length": "null",
                        "max_weight": "null"
                    }
                }
            }
        }
    }
}
    tnm = json.dumps(python_dict)
    return tnm

@pytest.fixture  
def enhanced_fake_json():
    python_dict = {
    "meta_data": {
        "max_length": 3778,
        "min_length": 1,
        "max_slope": 24.527,
        "min_slope": -2.407,
        "max_legal_speed": 80,
        "min_recommended_speed": 0,
        "max_mean_speed": 0,
        "min_mean_speed": 0,
        "max_daily_year": 16138.0,
        "min_daily_year": 57.5,
        "max_daily_july": 14813.0,
        "min_daily_july": 51.5,
        "max_daily_trucks": 10,
        "min_daily_trucks": 1
    },
    "vehicle": {
        "id": 1,
        "name": "Fiat multipla",
        "data": {
            "top_speed": 150,
            "mileage": 13204.03,
            "max_fuel": 4.3
        }
    },
    "nodes": {
        "1": {
            "id": 1,
            "weight": 0.0,
            "data": {
                "longitude": 15.9550166585396,
                "latitude": 57.1940874759639,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": True
            },
            "edges": {
                "1": {
                    "id": 1,
                    "from_node_id": 1,
                    "to_node_id": 3,
                    "weight": 0.0,
                    "data": {
                        "length": 96,
                        "slope": 0,
                        "type": "Trafikvej, prim\u00e6r by",
                        "type_max_speed": 80,
                        "set_max_speed": 80,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 2189.0,
                        "daily_july": 2252.5,
                        "daily_trucks": 10,
                        "daily_10_axle": 188.0,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                },
                "2": {
                    "id": 2,
                    "from_node_id": 1,
                    "to_node_id": 3,
                    "weight": 0.0,
                    "data": {
                        "length": 208,
                        "slope": 0,
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 80,
                        "set_max_speed": 80,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 3876.0,
                        "daily_july": 4703.0,
                        "daily_trucks": 10,
                        "daily_10_axle": 281.5,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                }
            }
        },
        "2": {
            "id": 2,
            "weight": 0.0,
            "data": {
                "longitude": 16.2145174943897,
                "latitude": 56.9771748846184,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": False
            },
            "edges": {}
        },
        "3": {
            "id": 3,
            "weight": 0.0,
            "data": {
                "longitude": 15.5891433415976,
                "latitude": 56.9609130669128,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": False
            },
            "edges": {
                "3": {
                    "id": 3,
                    "from_node_id": 3,
                    "to_node_id": 1,
                    "weight": 0.0,
                    "data": {
                        "length": 302,
                        "slope": "-0.23899999999999988",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                },
                "4": {
                    "id": 4,
                    "from_node_id": 3,
                    "to_node_id": 1,
                    "weight": 0.0,
                    "data": {
                        "length": 39,
                        "slope": "null",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                }
            }
        },
        "4": {
            "id": 4,
            "weight": 0.0,
            "data": {
                "longitude": 15.7367147390899,
                "latitude": 57.0368169072154,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": False
            },
            "edges": {
                "5": {
                    "id": 5,
                    "from_node_id": 4,
                    "to_node_id": 3,
                    "weight": 0.0,
                    "data": {
                        "length": 168,
                        "slope": "null",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                },
                "6": {
                    "id": 6,
                    "from_node_id": 5,
                    "to_node_id": 1,
                    "weight": 0.0,
                    "data": {
                        "length": 55,
                        "slope": "null",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                },
                "7": {
                    "id": 7,
                    "from_node_id": 6,
                    "to_node_id": 7,
                    "weight": 0.0,
                    "data": {
                        "length": 40,
                        "slope": "null",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                }
            }
        }
    }
}
    tnm = json.dumps(python_dict)
    return tnm

@pytest.fixture  
def annotated_fake_json():
    python_dict = {
    "meta_data": {
        "max_length": 3778,
        "min_length": 1,
        "max_slope": 24.527,
        "min_slope": -2.407,
        "max_legal_speed": 80,
        "min_recommended_speed": 0,
        "max_mean_speed": 0,
        "min_mean_speed": 0,
        "max_daily_year": 16138.0,
        "min_daily_year": 57.5,
        "max_daily_july": 14813.0,
        "min_daily_july": 51.5,
        "max_daily_trucks": 10,
        "min_daily_trucks": 1
    },
    "vehicle": {
        "id": 1,
        "name": "Fiat multipla",
        "data": {
            "top_speed": 150,
            "mileage": 13204.03,
            "max_fuel": 4.3
        }
    },
    "nodes": {
        "1": {
            "id": 1,
            "weight": 0.0,
            "data": {
                "longitude": 15.9550166585396,
                "latitude": 57.1940874759639,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": True
            },
            "edges": {
                "1": {
                    "id": 1,
                    "from_node_id": 1,
                    "to_node_id": 3,
                    "weight": 1.0,
                    "data": {
                        "length": 96,
                        "slope": 0,
                        "type": "Trafikvej, prim\u00e6r by",
                        "type_max_speed": 80,
                        "set_max_speed": 80,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 2189.0,
                        "daily_july": 2252.5,
                        "daily_trucks": 10,
                        "daily_10_axle": 188.0,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                },
                "2": {
                    "id": 2,
                    "from_node_id": 1,
                    "to_node_id": 3,
                    "weight": 1.0,
                    "data": {
                        "length": 208,
                        "slope": 0,
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 80,
                        "set_max_speed": 80,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 3876.0,
                        "daily_july": 4703.0,
                        "daily_trucks": 10,
                        "daily_10_axle": 281.5,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                }
            }
        },
        "2": {
            "id": 2,
            "weight": 0.0,
            "data": {
                "longitude": 16.2145174943897,
                "latitude": 56.9771748846184,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": False
            },
            "edges": {}
        },
        "3": {
            "id": 3,
            "weight": 0.0,
            "data": {
                "longitude": 15.5891433415976,
                "latitude": 56.9609130669128,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": False
            },
            "edges": {
                "3": {
                    "id": 3,
                    "from_node_id": 3,
                    "to_node_id": 1,
                    "weight": 1.0,
                    "data": {
                        "length": 302,
                        "slope": "-0.23899999999999988",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                },
                "4": {
                    "id": 4,
                    "from_node_id": 3,
                    "to_node_id": 1,
                    "weight": 1.0,
                    "data": {
                        "length": 39,
                        "slope": "null",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                }
            }
        },
        "4": {
            "id": 4,
            "weight": 0.0,
            "data": {
                "longitude": 15.7367147390899,
                "latitude": 57.0368169072154,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "regular",
                "signal_control": False
            },
            "edges": {
                "5": {
                    "id": 5,
                    "from_node_id": 4,
                    "to_node_id": 3,
                    "weight": 1.0,
                    "data": {
                        "length": 168,
                        "slope": "null",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                },
                "6": {
                    "id": 6,
                    "from_node_id": 5,
                    "to_node_id": 1,
                    "weight": 1.0,
                    "data": {
                        "length": 55,
                        "slope": "null",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                },
                "7": {
                    "id": 7,
                    "from_node_id": 6,
                    "to_node_id": 7,
                    "weight": 1.0,
                    "data": {
                        "length": 40,
                        "slope": "null",
                        "type": "Trafikvej,\n    prim\u00e6r by",
                        "type_max_speed": 0,
                        "set_max_speed": 0,
                        "recommended_speed": 0,
                        "mean_speed": 0,
                        "daily_year": 200,
                        "daily_july": 100,
                        "daily_trucks": 10,
                        "daily_10_axle": 20,
                        "fuel_station": False,
                        "max_axle_load": 0,
                        "max_height": 0,
                        "max_length": 0,
                        "max_weight": 0
                    }
                }
            }
        }
    }
}
    tnm = json.dumps(python_dict)
    return tnm

@pytest.fixture
def fake_json_as_dataframe():

    complete_dict = { 'id' : [1,2,3,4,5,6,7], 'from_node_id' : [1,1,3,3,4,4,7], 'to_node_id': [3,3,1,1,3,1,4], 'length' : [162,151,302,39,168,55,40], 'slope' : [0,0,-0.23899999999999988,0,0,0,0], 'type' : [None,None,None,None,None,None,None], 
    'type_max_speed' : [None,None,None,None,None,None,None], 'set_max_speed' : [None,None,None,None,None,None,None], 'recommended_speed' : [None,None,None,None,None,None,None], 'mean_speed' : [None,None,None,None,None,None,None], 'daily_year' : [None,None,None,None,None,None,None], 
    'daily_july' : [None,None,None,None,None,None,None], 'daily_trucks' : [None,None,None,None,None,None,None], 'daily_10_axle' : [None,None,None,None,None,None,None], 'fuel_station' : [False,False,False,False,False,False,False], 'max_axle_load' : [None,None,None,None,None,None,None],
    'max_height' : [None,None,None,None,None,None,None], 'max_length' : [None,None,None,None,None,None,None], 'max_weight' : [None,None,None,None,None,None,None]}
    
    dataFrame = pd.DataFrame(complete_dict)
    return dataFrame

@pytest.fixture
def fake_json_as_dataframe_changed_id_sequence():

    complete_dict = { 'id' : [4,2,3,1,5,6,7], 'from_node_id' : [1,1,3,3,4,4,7], 'to_node_id': [3,3,1,1,3,1,4], 'length' : [162,151,302,39,168,55,40], 'slope' : [0,0,-0.23899999999999988,0,0,0,0], 'type' : [None,None,None,None,None,None,None], 
    'type_max_speed' : [None,None,None,None,None,None,None], 'set_max_speed' : [None,None,None,None,None,None,None], 'recommended_speed' : [None,None,None,None,None,None,None], 'mean_speed' : [None,None,None,None,None,None,None], 'daily_year' : [None,None,None,None,None,None,None], 
    'daily_july' : [None,None,None,None,None,None,None], 'daily_trucks' : [None,None,None,None,None,None,None], 'daily_10_axle' : [None,None,None,None,None,None,None], 'fuel_station' : [False,False,False,False,False,False,False], 'max_axle_load' : [None,None,None,None,None,None,None],
    'max_height' : [None,None,None,None,None,None,None], 'max_length' : [None,None,None,None,None,None,None], 'max_weight' : [None,None,None,None,None,None,None]}
    
    dataFrame = pd.DataFrame(complete_dict)
    return dataFrame


# @pytest.fixture
# def fake_json_as_dataframe_with_dropped_columns():

#     complete_dict = { 'id' : [1,2,3,4,5,6,7], 'from_node_id' : [1,1,3,3,4,4,7], 'to_node_id': [3,3,1,1,3,1,4], 'length' : [162,151,302,39,168,55,40], 'slope' : [0,0,-0.23899999999999988,0,0,0,0], 'type' : [None,None,None,None,None,None,None], 
#     'type_max_speed' : [None,None,None,None,None,None,None], 'set_max_speed' : [None,None,None,None,None,None,None], 'recommended_speed' : [None,None,None,None,None,None,None], 'mean_speed' : [None,None,None,None,None,None,None], 'daily_year' : [None,None,None,None,None,None,None], 
#     'daily_july' : [None,None,None,None,None,None,None], 'daily_trucks' : [None,None,None,None,None,None,None], 'daily_10_axle' : [None,None,None,None,None,None,None], 'fuel_station' : [False,False,False,False,False,False,False], 'max_axle_load' : [None,None,None,None,None,None,None],
#     'max_height' : [None,None,None,None,None,None,None], 'max_length' : [None,None,None,None,None,None,None], 'max_weight' : [None,None,None,None,None,None,None]}
    
#     dataFrame = pd.DataFrame(complete_dict)
#     return dataFrame

@pytest.fixture
def fake_dataframe():

    complete_dict = { 'id' : [4,1,2,3,0,5,6,7,8,9], 'from_node_id' : [0,1,2,3,4,5,6,7,8,9], 'to_node_id': [0,1,2,3,4,5,6,7,8,9], 'length' : [0,1,2,3,4,5,6,7,8,9], 'slope' : [0,1,2,3,4,5,6,7,8,9], 'type' : [0,1,2,3,4,5,6,7,8,9], 
    'type_max_speed' : [0,1,2,3,4,5,6,7,8,9], 'set_max_speed' : [0,1,2,3,4,5,6,7,8,9], 'recommended_speed' : [0,1,2,3,4,5,6,7,8,9], 'mean_speed' : [0,1,2,3,4,5,6,7,8,9], 'daily_year' : [0,1,2,3,4,5,6,7,8,9], 
    'daily_july' : [0,1,2,3,4,5,6,7,8,9], 'daily_trucks' : [0,1,2,3,4,5,6,7,8,9], 'daily_10_axle' : [0,1,2,3,4,5,6,7,8,9], 'fuel_station' : [0,1,2,3,4,5,6,7,8,9], 'max_axle_load' : [0,1,2,3,4,5,6,7,8,9],
    'max_height' : [0,1,2,3,4,5,6,7,8,9], 'max_length' : [0,1,2,3,4,5,6,7,8,9], 'max_weight' : [0,1,2,3,4,5,6,7,8,9]}

    return pd.DataFrame(complete_dict)

@pytest.fixture
def client():
    print("client")
    # app = service
    # with app.test_client() as client:
    #     with app.app_context():
    #         yield client

