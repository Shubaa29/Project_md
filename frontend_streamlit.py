import streamlit as st
import pandas as pd
import pickle

# Load model pipeline
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Prediksi Rawat Inap (Hospitalized) Pasien COVID-19")

st.markdown("Masukkan data pasien di bawah ini untuk memprediksi apakah perlu rawat inap:")

# Input form
def user_input():
    Age = st.slider("Umur", 0, 100, 30)
    Gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    Occupation = st.selectbox("Pekerjaan", ["Healthcare Worker", "Unemployed", "Other", "Essential Services"])
    Region = st.selectbox("Wilayah", ["Region A", "Region B", "Region C"])
    Smoking_Status = st.selectbox("Status Merokok", ["Smoker", "Non-Smoker"])
    BMI = st.number_input("BMI", 10.0, 50.0, 22.0)
    Preexisting_Condition = st.selectbox("Penyakit Bawaan", ["Yes", "No"])
    Vaccination_Status = st.selectbox("Status Vaksinasi", ["Not Vaccinated", "Partially Vaccinated", "Fully Vaccinated"])
    Doses_Received = st.slider("Jumlah Dosis Vaksin", 0, 4, 2)
    Reinfection = st.selectbox("Reinfeksi?", ["Yes", "No"])
    COVID_Strain = st.selectbox("Varian COVID", ["Alpha", "Delta", "Omicron", "Other"])
    Symptoms = st.selectbox("Ada Gejala?", ["Yes", "No"])
    ICU_Admission = st.selectbox("Rawat ICU?", ["Yes", "No"])
    Ventilator_Support = st.selectbox("Pakai Ventilator?", ["Yes", "No"])
    Recovered = st.selectbox("Sudah Sembuh?", ["Yes", "No"])
    Severity = st.selectbox("Tingkat Keparahan", ["Mild", "Moderate", "Severe"])

    data = {
        "Age": Age,
        "Gender": Gender,
        "Occupation": Occupation,
        "Region": Region,
        "Smoking_Status": Smoking_Status,
        "BMI": BMI,
        "Preexisting_Condition": Preexisting_Condition,
        "Vaccination_Status": Vaccination_Status,
        "Doses_Received": Doses_Received,
        "Reinfection": Reinfection,
        "COVID_Strain": COVID_Strain,
        "Symptoms": Symptoms,
        "ICU_Admission": ICU_Admission,
        "Ventilator_Support": Ventilator_Support,
        "Recovered": Recovered,
        "Severity": Severity
    }

    return pd.DataFrame([data])

input_df = user_input()

# Tombol prediksi
if st.button("Prediksi"):
    prediction = model.predict(input_df)[0]
    label = "Yes" if prediction == 1 else "No"
    st.subheader("Hasil Prediksi:")
    st.write(f"Pasien perlu dirawat inap: **{label}** (label numerik: {prediction})")
