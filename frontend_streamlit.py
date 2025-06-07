import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Prediksi Hospitalisasi COVID", layout="centered")

# Load model pipeline
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🩺 Prediksi Hospitalisasi Pasien COVID-Related Disease")

def user_input():
    age = st.slider('Umur', 0, 100, 30)
    doses = st.slider('Jumlah Dosis Vaksin yang Diterima', 0, 4, 2)
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=22.0)

    gender = st.selectbox('Jenis Kelamin', ['Male', 'Female', 'Other'])
    region = st.selectbox('Wilayah', ['Asia', 'Europe', 'America', 'Africa', 'Oceania'])
    preexisting = st.selectbox('Penyakit Penyerta', ['Yes', 'No'])
    strain = st.selectbox('Varian COVID', ['Alpha', 'Beta', 'Delta', 'Omicron', 'Original'])
    symptoms = st.selectbox('Gejala', ['Mild', 'Moderate', 'Severe'])
    severity = st.selectbox('Tingkat Keparahan', ['Low', 'Medium', 'High'])
    icu = st.selectbox('Dirawat di ICU', ['Yes', 'No'])
    ventilator = st.selectbox('Dibantu Ventilator', ['Yes', 'No'])
    recovered = st.selectbox('Sudah Sembuh', ['Yes', 'No'])
    reinfection = st.selectbox('Pernah Terinfeksi Ulang', ['Yes', 'No'])
    vax_status = st.selectbox('Status Vaksinasi', ['Unvaccinated', 'Partial', 'Full'])
    occupation = st.selectbox('Pekerjaan', ['Healthcare', 'Essential', 'Non-Essential'])
    smoking = st.selectbox('Perokok', ['Yes', 'No'])

    data = {
        'Age': [age],
        'Doses_Received': [doses],
        'BMI': [bmi],
        'Gender': [gender],
        'Region': [region],
        'Preexisting_Condition': [preexisting],
        'COVID_Strain': [strain],
        'Symptoms': [symptoms],
        'Severity': [severity],
        'ICU_Admission': [icu],
        'Ventilator_Support': [ventilator],
        'Recovered': [recovered],
        'Reinfection': [reinfection],
        'Vaccination_Status': [vax_status],
        'Occupation': [occupation],
        'Smoking_Status': [smoking]
    }

    return pd.DataFrame(data)

input_df = user_input()

if st.button('Prediksi'):
    try:
        prediction = model.predict(input_df)
        result = '🛏️ Dirawat (Hospitalized)' if prediction[0] == 1 else '🏠 Tidak Dirawat'
        st.success(f'Hasil Prediksi: {result}')
    except Exception as e:
        st.error(f'Error saat memproses prediksi: {e}')
