import streamlit as st
from model import predict_price

st.title("🏠 House Price Predictor")

st.write("Enter house details:")

area = st.slider("Area (sq ft)", 500, 5000)
bedrooms = st.slider("Bedrooms", 1, 10)
age = st.slider("House Age (years)", 0, 30)

if st.button("Predict Price"):
    price = predict_price(area, bedrooms, age)
    st.success(f"Estimated Price: ₹ {round(price, 2)}")