import json
from src.adapter_transportation import MIAdapter
from src.enhancer_microservice import Enhancer
from src.model_training import TrainModel
import joblib

# When opening the file - make sure to adjust the path to your own location of the tnm.json file
# f = open('/Users/rasmushenriksen/Desktop/BACHELOR-SOFTWARE/femte_og_sjette/femte_semester/Project/Python/src/Data_set/tnm.json')
def train_model_on_TNM(tnm):
    a = MIAdapter(tnm)

    # Convert TNM to Pandas dataframe
    print(" -------------------- CONVERTING TO DATA FRAME --------------------\n")
    df = a.from_json()
    

    # Enhance the DataFrame
    print(" -------------------- ENHANCING DATA FRAME --------------------\n")
    e = Enhancer(a.meta_data)
    enhanced_df = e.enhance_data_frame(df)
    print(enhanced_df)

    # Train the model
    print(" -------------------- TRAINING THE MODEL --------------------\n")
    tm = TrainModel(enhanced_df)
    tm.train_model()

    return predict_heavy_traffic(tnm)

def predict_heavy_traffic(tnm):
    model = None
    try:
        model = joblib.load('decision_tree_model.joblib')
    except:
        print(" -------------------- NO TRAINED MODEL --------------------\n")
        # return "You must call /train to create a model first"

    a = MIAdapter(tnm)

    # Convert TNM to Pandas dataframe
    print(" -------------------- CONVERTING TO DATA FRAME --------------------\n")
    df = a.from_json()

    # Enhance the DataFrame
    print(" -------------------- ENHANCING DATA FRAME --------------------\n")
    e = Enhancer(a.meta_data)
    df = e.remove_column(df,"daily_trucks")
    # Load the model
    

    print(" -------------------- PREDICTING --------------------\n")


    # Make predictions
    predicted_weights = model.predict(df)
    print(" -------------------- DONE PREDICTING --------------------\n")
    if len(predicted_weights) != df.shape[0]:
        print("ERROR!!!!")
        exit(0)

    numbers = {}
    for (index, row), weight in zip(df.iterrows(), predicted_weights): 
        numbers[str(row['id'])] = weight

    # Add weights to TNM
    print(" -------------------- ADDING WEIGHTS TO TNM --------------------\n")
    updated_tnm = a.to_json(numbers)

    # Creates an updated TNM file with edge weights
    print(" -------------------- CREATING UPDATED TNM FILE --------------------\n")
    with open("updated_tnm.json", "w") as outfile:
        json.dump(updated_tnm, outfile, indent=4, sort_keys=False)

    return updated_tnm

def translate(tnm):
    parsed = json.loads(tnm,strict = False)
    with open("new_tnm.json", "w") as outfile:
        json.dump(parsed, outfile, indent=4, sort_keys=False)
    return "json file created"