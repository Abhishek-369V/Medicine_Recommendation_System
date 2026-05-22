import joblib

from src.data_loader import load_training
from src.utils import symptoms_to_vector # Converts user symtoms into vectors


model=joblib.load("models/disease_model.pkl")

le=joblib.load("models/label_encoder.pkl")


train_df=load_training() # load training data

symptom_columns=list(
train_df.drop("prognosis",axis=1).columns
) # load symptom columns


def predict_disease(user_symptoms): # predict disease

    vector=symptoms_to_vector(  # Converts user symtoms into vectors
        user_symptoms, # user symptoms
        symptom_columns # symptom columns
    ) 

    prediction=model.predict([vector]) # predict disease

    disease=le.inverse_transform(prediction)[0] # get disease name

    return disease