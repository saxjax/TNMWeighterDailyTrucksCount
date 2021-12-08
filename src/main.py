#!/usr/bin/env python3:
from src.heavy_weighter import predict_heavy_traffic, train_model_on_TNM
from src.adapter_transportation import MIAdapter

def main(input):
    annotatedTNM = {}
    try:
      annotatedTNM = predict_heavy_traffic(input)
    except:
    #   print( 'you must train a model first by calling /train {TNM}')
      annotatedTNM = train_model_on_TNM(input)
    
    return annotatedTNM


if __name__ == "__main__":
    main()