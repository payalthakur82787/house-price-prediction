import streamlit as st
import pickle
import numpy as np

# Load model & encoder
model = pickle.load(open("house_model.pkl", "rb"))
le = pickle.load(open("location_encoder.pkl", "rb"))

st.title("🏠 House Price Prediction App")

# Inputs
area = st.number_input("Area (sq ft)", 500, 5000)
bedrooms = st.slider("Bedrooms", 1, 6)
bathrooms = st.slider("Bathrooms", 1, 5)

location = st.selectbox("Location", le.classes_)

# Encode location
loc_encoded = le.transform([location])[0]

# Predict
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms, loc_encoded]])
    prediction = model.predict(input_data)

    st.success(f"💰 Estimated Price: ₹{int(prediction[0])}")