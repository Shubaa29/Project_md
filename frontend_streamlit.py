# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Prediksi Hospitalisasi COVID-Related Disease")

st.title("Aplikasi Prediksi Hospitalisasi")
st.write("Masukkan data pasien untuk memprediksi kemungkinan dirawat di rumah sakit.")

# Contoh fitur dari dataset (harus disesuaikan dengan fitur yang digunakan model)
# Misalnya: Age, Gender, Fever, Cough, etc.
# Ubah sesuai dengan input sebenarnya dari dataset Anda

def user_input_features():
    age = st.slider('Umur', 0, 100, 30)
    gender = st.selectbox('Jenis Kelamin', ['Male', 'Female'])
    fever = st.selectbox('Demam', ['Yes', 'No'])
    cough = st.selectbox('Batuk', ['Yes', 'No'])
    sore_throat = st.selectbox('Sakit Tenggorokan', ['Yes', 'No'])
    breathing_problem = st.selectbox('Masalah Pernapasan', ['Yes', 'No'])
    fatigue = st.selectbox('Kelelahan', ['Yes', 'No'])

    # Buat DataFrame input user
    data = {
        'Age': [age],
        'Gender': [gender],
        'Fever': [fever],
        'Cough': [cough],
        'Sore_Throat': [sore_throat],
        'Breathing_Problem': [breathing_problem],
        'Fatigue': [fatigue]
    }

    return pd.DataFrame(data)

input_df = user_input_features()

# Prediksi
if st.button('Prediksi'):
    prediction = model.predict(input_df)
    prediction_label = 'Dirawat (Hospitalized)' if prediction[0] == 1 else 'Tidak Dirawat'
    st.subheader('Hasil Prediksi:')
    st.success(f'Pasien kemungkinan: {prediction_label}')
