import pandas as pd
import ast

DATA_PATH="data/"


def load_training(): # load training data

    df=pd.read_csv(DATA_PATH+"Training.csv")

    df=df.loc[:,~df.columns.duplicated()] # remove duplicate columns

    df.columns=df.columns.str.strip() # remove leading/trailing whitespaces like "  venky" --> "venky"

    df["prognosis"]=df["prognosis"].str.strip() # remove leading/trailing whitespaces like "  diabetes" --> "diabetes"

    return df


def load_description(): # load description data

    df=pd.read_csv(DATA_PATH+"description.csv")

    df["Disease"]=df["Disease"].str.strip() # remove leading/trailing whitespaces like "  diabetes" --> "diabetes"

    return df


def load_diets():

    df=pd.read_csv(DATA_PATH+"diets.csv") # load diet data

    df["Disease"]=df["Disease"].str.strip() # remove leading/trailing whitespaces like "  diabetes" --> "diabetes"

    df["Diet"]=df["Diet"].apply(ast.literal_eval) # convert diet column to list of strings
    # eg. "['eat fruits','eat vegetables']" --> ['eat fruits','eat vegetables']

    return df


def load_medications(): # load medication data

    df=pd.read_csv(DATA_PATH+"medications.csv")

    df["Disease"]=df["Disease"].str.strip() # remove leading/trailing whitespaces like "  diabetes" --> "diabetes"

    df["Medication"]=df["Medication"].apply(ast.literal_eval) # convert medication column to list of strings
    # eg. "['eat fruits','eat vegetables']" --> ['eat fruits','eat vegetables']

    return df


def load_precautions(): # load precautions data

    df=pd.read_csv("data/precautions_df.csv",index_col=0) # load precautions data

    df["Disease"]=df["Disease"].str.strip() # remove leading/trailing whitespaces like "  diabetes" --> "diabetes"

    return df


def load_workout(): # load workout data

    df=pd.read_csv(DATA_PATH+"workout_df.csv")

    if "Unnamed: 0" in df.columns: # remove unnamed column if present

        df.drop(columns=["Unnamed: 0"],inplace=True)

    df.rename(columns={"disease":"Disease"},inplace=True) # rename column name

    df["Disease"]=df["Disease"].str.strip() # remove leading/trailing whitespaces like "  diabetes" --> "diabetes"

    return df


def load_severity(): # load severity data

    df=pd.read_csv(DATA_PATH+"Symptom-severity.csv")

    df["Symptom"]=df["Symptom"].str.strip() # remove leading/trailing whitespaces like "  diabetes" --> "diabetes"

    return dict(zip(df["Symptom"],df["weight"])) # convert to dictionary

    # { rash : 6, tyy : 7}