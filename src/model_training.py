
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

class TrainModel():
    def __init__(self):
        pass

    def train_model_fake_data(self, df):
        X_input = df.drop(columns=['daily_trucks'])
        y_output = df['daily_trucks']

        X_train, X_test, y_train, y_test = train_test_split(X_input, y_output, test_size=0.2)

        model = DecisionTreeClassifier()
        model.fit(X_train,y_train)

        # Stores our trained model in a file
        joblib.dump(model, 'decision_tree_model_fake.joblib')

        print("------------- MODEL SUCCESSFULLY TRAINED ON FAKE DATA -------------")

        return TrainModel.predict_on_data(self, X_test, y_test, model)

    def train_model_real_data(self, df):
        X_input = df.drop(columns=['daily_trucks'])
        y_output = df['daily_trucks']

        X_train, X_test, y_train, y_test = train_test_split(X_input, y_output, test_size=0.2)

        model = DecisionTreeClassifier()
        model.fit(X_train,y_train)

        # Stores our trained model in a file
        joblib.dump(model, 'decision_tree_model_real.joblib')

        print("------------- MODEL SUCCESSFULLY TRAINED ON REAL DATA -------------")

        return TrainModel.predict_on_data(self, X_test, y_test, model)

    def train_and_predict(self, df_fake, df_real):
        fake_data_score = TrainModel.train_model_fake_data(self, df_fake)
        real_data_score = TrainModel.train_model_real_data(self, df_real)
        return fake_data_score, real_data_score
    
    def predict_on_data(self, X_test, y_test, model):
        predictions = model.predict(X_test)
        score = accuracy_score(y_test, predictions)
        return score
