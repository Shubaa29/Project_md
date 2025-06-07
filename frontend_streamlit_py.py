import streamlit as st
import pickle
import base64
import io

# =======================
# Embedded model (base64)
# =======================
model_base64 = """<ISI_STRING_BASE64_DI_SINI>"""

# Decode model
model_bytes = base64.b64decode(model_base64)
model = pickle.load(io.BytesIO(model_bytes))

# =======================
# Streamlit App
# =======================
st.title("COVID Risk Prediction App")

st.markdown("Masukkan data pasien di bawah ini untuk memprediksi risiko penyakit terkait COVID.")

# Form input user
age = st.slider("Usia", 0, 100, 25)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.5)
gender = st.selectbox("Jenis Kelamin", ["Male", "Female", "Other"])
region = st.selectbox("Region", ["Asia", "Europe", "Africa", "America", "Oceania"])
smoking_status = st.selectbox("Status Merokok", ["Never", "Former", "Current"])
preexisting_condition = st.selectbox("Penyakit Penyerta", ["Yes", "No"])
vaccination_status = st.selectbox("Status Vaksinasi", ["Not Vaccinated", "Partially", "Fully"])
symptoms = st.selectbox("Memiliki Gejala?", ["Yes", "No"])
severity = st.selectbox("Tingkat Keparahan", ["Mild", "Moderate", "Severe"])
icu_admission = st.selectbox("Masuk ICU?", ["Yes", "No"])
ventilator_support = st.selectbox("Butuh Ventilator?", ["Yes", "No"])
recovered = st.selectbox("Sudah Sembuh?", ["Yes", "No"])

# Saat tombol ditekan
if st.button("Prediksi Risiko"):
    # Susun input sesuai urutan fitur model
    input_data = [[
        age, gender, region, bmi, smoking_status, preexisting_condition,
        vaccination_status, symptoms, severity, icu_admission,
        ventilator_support, recovered
    ]]
    
    # Prediksi
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Hasil Prediksi: {prediction}")
    except Exception as e:
        st.error(f"Gagal prediksi: {e}")
