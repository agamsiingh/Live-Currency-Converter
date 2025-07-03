Here's a clean and informative **README** file for your **Live Currency Converter** Streamlit project:

---

# 💱 Live Currency Converter

A simple web app built with **Streamlit** and **Python** that converts Indian Rupees (INR) to popular foreign currencies like **USD**, **EUR**, **GBP**, and **JPY** in real-time using data from the [ExchangeRate API](https://www.exchangerate-api.com/).

## 🚀 Features

* Input amount in INR
* Select from multiple target currencies (USD, EUR, GBP, JPY)
* Fetch live exchange rates
* Displays the converted amount
* Clean and minimal Streamlit UI

## 🖼️ Preview

![Currency Converter Screenshot](path/to/your/screenshot.png)
*(Replace with an actual image)*

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – for building the UI
* **Requests** – for making HTTP requests to the API
* **ExchangeRate API** – to get the live rates

## 📦 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/currency-converter-streamlit.git
cd currency-converter-streamlit
```

2. **Install dependencies:**

```bash
pip install streamlit requests
```

3. **Run the app:**

```bash
streamlit run app.py
```

Replace `app.py` with your actual filename if it's different.

## 📁 Project Structure

```
currency-converter-streamlit/
├── app.py
├── README.md
└── requirements.txt
```

## 📄 Sample Code

```python
import streamlit as st
import requests

st.title("💱 Live Currency Converter")

amount = st.number_input("Enter the amount in INR", min_value=1)
target_currency = st.selectbox("Convert to:", ["USD", "EUR", "GBP", "JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted = rate * amount
        st.success(f"{amount} INR = {converted:.2f} {target_currency}")
    else:
        st.error("❌ Failed to fetch conversion rate.")
```

## 📌 To-Do (Optional Enhancements)

* Add more currencies
* Include historical rate charts
* Improve UI with themes or images
* Add currency flags

## 📃 License

This project is licensed under the MIT License.

---

Let me know if you'd like help creating a `requirements.txt`, a deployment guide, or a GitHub-ready version with badges!
