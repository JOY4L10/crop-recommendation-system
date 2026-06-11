import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("crop_model.pkl")

st.title("🌱 Crop Recommendation System")

N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)
temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
ph = st.number_input("pH")
rainfall = st.number_input("Rainfall")

if st.button("Recommend Crop"):
    sample = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(sample)
    st.success(f"Recommended Crop: {prediction[0]}")