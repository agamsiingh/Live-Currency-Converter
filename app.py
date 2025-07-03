import streamlit as st
import requests

st.title("💱 Live Currency Converter")

# Input: INR amount
amount = st.number_input("Enter the amount in INR", min_value=1)

# Target currency selection
target_currency = st.selectbox("Convert to:", ["USD", "EUR", "GBP", "JPY"])

# On Convert button click
if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]  # Fix: Store the rate
        converted = rate * amount
        st.success(f"{amount} INR = {converted:.2f} {target_currency}")  # Fix: lowercase f, closing quote
    else:
        st.error("❌ Failed to fetch conversion rate.")
