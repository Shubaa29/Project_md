import streamlit as st
import pickle
import pandas as pd

# Load model
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Judul Aplikasi
st.title("Prediksi Tingkat Keparahan Penyakit Terkait COVID-19")

# Form input
st.subheader("Masukkan data pasien:")
age = st.slider("Umur", 0, 100, 25)
gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
region = st.selectbox("Wilayah", ["Region A", "Region B", "Region C"])
bmi = st.number_input("BMI", 10.0, 50.0, 22.5)
smoking = st.selectbox("Status Merokok", ["Smoker", "Non-Smoker"])
preexist = st.selectbox("Penyakit Penyerta", ["Yes", "No"])
symptoms = st.selectbox("Mengalami Gejala?", ["Yes", "No"])
vaccine = st.selectbox("Status Vaksinasi", ["Fully Vaccinated", "Partially Vaccinated", "Not Vaccinated"])
doses = st.slider("Jumlah Dosis Vaksin", 0, 3, 2)
reinfection = st.selectbox("Reinfeksi?", ["Yes", "No"])
icu = st.selectbox("Perawatan ICU?", ["Yes", "No"])
ventilator = st.selectbox("Ventilator Support?", ["Yes", "No"])

# Tombol prediksi
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
    st.success(f"Prediksi tingkat keparahan: **{prediction}**")
