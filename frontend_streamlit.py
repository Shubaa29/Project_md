import streamlit as st
import pickle
import pandas as pd
import joblib

# Load model
model = joblib.load("random_forest_model.pkl")

st.title("Prediksi Keparahan COVID-19")

# Input form
age = st.slider("Umur", 0, 100, 25)
gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
region = st.selectbox("Wilayah", ["Region A", "Region B", "Region C"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
smoking = st.selectbox("Status Merokok", ["Smoker", "Non-Smoker"])
preexist = st.selectbox("Penyakit Penyerta", ["Yes", "No"])
symptoms = st.selectbox("Gejala?", ["Yes", "No"])
vaccine = st.selectbox("Status Vaksin", ["Fully Vaccinated", "Partially Vaccinated", "Not Vaccinated"])
doses = st.slider("Jumlah Dosis", 0, 3, 2)
reinfection = st.selectbox("Reinfeksi?", ["Yes", "No"])
icu = st.selectbox("ICU?", ["Yes", "No"])
ventilator = st.selectbox("Ventilator?", ["Yes", "No"])

# Prediksi
if st.button("Prediksi"):
    input_df = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Region": region,
        "BMI": bmi,
        "Smoking_Status": smoking,
        "Preexisting_Condition": preexist,
        "Symptoms": symptoms,
        "Vaccination_Status": vaccine,
        "Doses_Received": doses,
        "Reinfection": reinfection,
        "ICU_Admission": icu,
        "Ventilator_Support": ventilator
    }])
    
    prediction = model.predict(input_df)[0]
    st.success(f"Hasil Prediksi: **{prediction}**")
