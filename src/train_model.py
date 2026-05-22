from sklearn.preprocessing import LabelEncoder # Conberts strings to numbers
from sklearn.ensemble import RandomForestClassifier # random forest classifier
from sklearn.model_selection import train_test_split # split data into train and test
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    r2_score
) # metrics
import joblib
import numpy as np

from src.data_loader import load_training # load training data


def train():

    print("Loading dataset...")

    df = load_training() # load training data


    X = df.drop("prognosis", axis=1) # features or Symptoms x= itching, fever, vomiting

    y = df["prognosis"] # target or Disease y= Dengue, Malaria, Typhoid


    le = LabelEncoder() # converts strings to numbers

    y_encoded = le.fit_transform(y) # converts disease names to numbers

   

    X_train, X_test, y_train, y_test = train_test_split(
        X,  # features
        y_encoded, # target
        test_size=0.2, # 20% of data for testing
        random_state=42 # random seed
    )



    model = RandomForestClassifier(
        n_estimators=200, # number of trees
        random_state=42 # random seed
    )

    print("Training model...")

    model.fit(X_train, y_train) # train the model

    

    y_pred = model.predict(X_test) # predict the target

    

    accuracy = accuracy_score(y_test, y_pred) # accuracy of the model Correctly classified / Total samples

    precision = precision_score(
        y_test,
        y_pred,
        average='weighted'
    ) # precision of the model 
    # How many of the predicted values are correct

    recall = recall_score(
        y_test,
        y_pred,
        average='weighted'
    ) # recall of the model
    # How many of the actual values are predicted correctly

    f1 = f1_score(
        y_test,
        y_pred,
        average='weighted'
    ) # Balance between precision and recall

    r2 = r2_score(y_test, y_pred) # R2 score of the model

    cm = confusion_matrix(y_test, y_pred) # confusion matrix of the model

    

    print("\n <---------- MODEL PERFORMANCE ---------->")
    print(f"Accuracy      : {accuracy:.4f}")
    print(f"Precision     : {precision:.4f}")
    print(f"Recall        : {recall:.4f}")
    print(f"F1 Score      : {f1:.4f}")
    print(f"R2 Score      : {r2:.4f}")

    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred)) # classification report of the model

    print("\nConfusion Matrix:\n")
    print(cm)

    

    joblib.dump(model, "models/disease_model.pkl") # save the model
    joblib.dump(le, "models/label_encoder.pkl") # save the label encoder

    print("\n Model Saved Successfully")


if __name__ == "__main__":
    train()