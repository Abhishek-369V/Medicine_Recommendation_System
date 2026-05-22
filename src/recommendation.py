from src.data_loader import *

desc_df=load_description() # load description
diet_df=load_diets() # load diet
med_df=load_medications() # load medication
prec_df=load_precautions() # load precautions
work_df=load_workout() # load workout


def get_description(disease): # input diease name, output description

    return desc_df[
    desc_df["Disease"]==disease
    ]["Description"].values[0] # return description


def get_medicine(disease): # input diease name, output medication

    return med_df[
    med_df["Disease"]==disease
    ]["Medication"].values[0] # return medication


def get_diet(disease): # input diease name, output diet

    return diet_df[
    diet_df["Disease"]==disease
    ]["Diet"].values[0] # return diet


def get_precautions(disease): # input diease name, output precautions

    row=prec_df[
    prec_df["Disease"]==disease
    ]

    return row.iloc[0,1:].dropna().values # return list of precautions


def get_workout(disease): # input diease name, output workout

    rows=work_df[
    work_df["Disease"]==disease
    ] # return dataframe

    return rows["workout"].values # return list of workouts