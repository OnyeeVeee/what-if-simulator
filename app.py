import streamlit as st
import pandas as pd
import pickle

with open("models/random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("AI-Powered Student Performance Simulator")
st.write(
    "Adjust student factors to predict final exam performance."
)

study_hours = st.slider(
    "Study Hours per Week",
    min_value=0,
    max_value=50,
    value=25
)
attendance = st.slider(
    "Attendance Rate",
    min_value=50,
    max_value=100,
    value=80
)
past_scores = st.slider(
    "Past Exam Score",
    min_value=0,
    max_value=100,
    value=75
)
parental_education = st.selectbox(
    "Parental Education Level",
    ["High School", "Bachelors", "Masters", "PhD"]
)
internet_access = st.selectbox(
    "Internet Access at Home",
    ["No", "Yes"]
)
extracurricular = st.selectbox(
    "Participates in Extracurricular Activities",
    ["No", "Yes"]
)
if st.button("Predict Final Score"):
        input_data = pd.DataFrame([{
        "Study_Hours_per_Week": study_hours,
        "Attendance_Rate": attendance,
        "Past_Exam_Scores": past_scores,
        "Parental_Education_Level": parental_education,
        "Internet_Access_at_Home": internet_access,
        "Extracurricular_Activities": extracurricular
    }])

        prediction = model.predict(input_data)
        st.success(
            f"Predicted Final Exam Score: {prediction[0]:.2f}"
        )
