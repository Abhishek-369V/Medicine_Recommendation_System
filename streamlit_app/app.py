import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
) # Getting the System Path


import streamlit as st # Web App Framework
import pandas as pd # Dataframe Library
import matplotlib.pyplot as plt # Plotting Library
import seaborn as sns # Plotting Library
from sklearn.metrics import confusion_matrix # Confusion Matrix
import joblib # Model Saving and Loading

from src.data_loader import load_training # Load Training Data
from src.predict import predict_disease # Predict Disease
from src.recommendation import * # Get Medicine Recommendation
from src.severity import calculate_severity # Calculate Severity




st.set_page_config(

    page_title="AI Medicine Recommendation",

    layout="wide",

    page_icon="🏥"

)

# Header

st.title(" AI Medicine Recommendation Dashboard")

st.markdown(
"### Machine Learning Based Healthcare Assistant"
)

st.divider()


# Load Dataset

train_df = load_training() # Load Training Data

symptoms = list(
    train_df.drop("prognosis",axis=1).columns # Drop Diease Columns and Get Symptoms
)

# load Models

model = joblib.load("models/disease_model.pkl")

le = joblib.load("models/label_encoder.pkl")

# Sidebar

st.sidebar.header("Patient Symptoms") # Sidebar Header

selected = st.sidebar.multiselect(

    "Select Symptoms",

    symptoms

) # Select Symptoms

predict_button = st.sidebar.button(

    "Predict Disease",

    use_container_width=True

) # Predict Button

st.sidebar.divider() # Divider

st.sidebar.caption("AI Healthcare ML System") # Caption

# ---------------- MODEL INFO METRICS ----------------

col1,col2,col3 = st.columns(3)

with col1:

    st.metric(

        "Total Symptoms",

        len(symptoms)

    ) # Total Symptoms in datasets

with col2:

    st.metric(

        "Diseases",

        train_df["prognosis"].nunique()

    ) # Total Diseases in datasets

with col3:

    st.metric(

        "Model",

        "Random Forest"

    ) # Model Used

st.divider()


# predict disease

if predict_button:

    if not selected:

        st.warning("Please select symptoms") # Warning if no symptoms selected

        st.stop() # stop execution

    disease = predict_disease(selected) # Predict Disease

    st.success(

        f" Predicted Disease : {disease}"

    ) # Displaying the diease

    # Description

    with st.expander(  # Expander

        " Disease Description",

        expanded=True

    ):

        st.info(

            get_description(disease) # Get Description

        )

    # severity

    score = calculate_severity(selected) # Calculate Severity

    c1,c2 = st.columns(2)

    with c1:

        st.metric(

            "Risk Score",

            score

        ) # Risk Score

    with c2:

        if score>20:

            st.error(

                " High Risk Symptoms — Consult Doctor"

            ) # Showing message when above 20

        else:

            st.success(

                "Normal Risk Level"

            ) # Showing message when below 20

    st.divider()

    # Medicines

    st.subheader(" Recommended Medicines")

    meds = get_medicine(disease) # Get Medicine

    cols = st.columns(3) # 3 Columns

    for i,med in enumerate(meds): # Looping through medicines

        with cols[i%3]:

            st.success(med) # Displaying Medicine

    # Recommendation Diet

    st.subheader(" Recommended Diet")

    diets = get_diet(disease) # Get Diet

    cols = st.columns(3)

    for i,d in enumerate(diets):

        with cols[i%3]:

            st.info(d) # Displaying Diet

    # Precautions

    st.subheader(" Precautions")

    for p in get_precautions(disease):

        st.write("--> ",p) # Displaying Precautions

    # life Style

    st.subheader(" Lifestyle Advice")

    for w in get_workout(disease):

        st.write("--> ",w) # Displaying Workout

    st.divider()

    
    # MODEL PERFORMANCE
   

    st.header(" Model Performance")

    X = train_df.drop("prognosis",axis=1) # Drop Diease Columns

    y = train_df["prognosis"] # Get Diease Columns

    y_encoded = le.transform(y) # Encode Diease Columns

    pred = model.predict(X) # Predict Diease

    # Confusion Matrix

    st.subheader("Confusion Matrix")

    cm = confusion_matrix(

        y_encoded,

        pred

    ) # Confusion Matrix values getting

    fig,ax = plt.subplots(

        figsize=(12,10)

    ) # Plotting Confusion Matrix

    sns.heatmap( # Heatmap

        cm, # Confusion Matrix values

        cmap="Blues", # Color Map

        square=True, # Square

        linewidths=.2, # Line Widths

        xticklabels=False, # X Tick Labels

        yticklabels=False, # Y Tick Labels

        cbar=True, # Color Bar

        ax=ax # Axes

    )

    ax.set_title(

        "Disease Prediction Confusion Matrix"

    ) # Title

    ax.set_xlabel("Predicted") # X Label

    ax.set_ylabel("Actual") # Y Label

    st.pyplot(fig) # Displaying Confusion Matrix

    # Feature importance

    st.subheader("Top Feature Importance")

    importance = model.feature_importances_ # Feature Importance

    feature_names = X.columns # Feature Names

    imp_df = pd.DataFrame({

        "feature":feature_names,

        "importance":importance

    }) # Feature Importance DataFrame

    imp_df = imp_df.sort_values(

        by="importance",

        ascending=False

    ).head(15) # Top 15 Features

    fig2,ax2 = plt.subplots(

        figsize=(10,6)

    ) # Plotting Feature Importance

    ax2.barh(

        imp_df["feature"],

        imp_df["importance"]

    ) # Bar Plot

    ax2.invert_yaxis() # Invert Y Axis

    ax2.set_title(

        "Top Important Symptoms"

    )

    st.pyplot(fig2) # Displaying Feature Importance


# Footer

st.divider()

st.caption(

"AI Medicine Recommendation System | Machine Learning Dashboard"

)