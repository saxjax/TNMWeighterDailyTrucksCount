
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

class TrainModel():
    def __init__(self, df):
        self.df = df

    def train_model(self):
        X_input = self.df.drop(columns=['daily_trucks'])
        y_output = self.df['daily_trucks']

        X_train, X_test, y_train, y_test = train_test_split(X_input, y_output, test_size=0.2)

        model = DecisionTreeClassifier()
        model.fit(X_train,y_train)

        # Stores our trained model in a file
        joblib.dump(model, 'decision_tree_model.joblib')

        print("------------- MODEL SUCCESSFULLY TRAINED -------------")

