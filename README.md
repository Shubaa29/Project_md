# COVID Risk Prediction App

A Streamlit web application to predict the risk of diseases related to COVID-19 using a trained Random Forest model.

## 🔧 Features

- User-friendly form interface
- Embedded pre-trained machine learning model (no separate `.pkl` needed)
- Predicts risk based on user-input health and demographic data

## 🚀 How to Run Locally

1. Clone the repository or download the files.
2. Make sure you have Python 3.7+ installed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run frontend_streamlit.py
```

## 📁 File Structure

```
.
├── frontend_streamlit.py      # Streamlit app (model embedded)
├── requirements.txt           # List of Python dependencies
└── README.md                  # This file
```

## 📦 Deployment

You can deploy this directly to [Streamlit Cloud](https://streamlit.io/cloud). Just upload the files from this project, and it will run without needing the .pkl model separately.

