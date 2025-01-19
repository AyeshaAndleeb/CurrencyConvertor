import streamlit as st

# Set page configuration
st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

# Title of the app
st.title("💱 Currency Conversion App")

# Hardcoded exchange rates (example values)
exchange_rates = {
    "USD": {"EUR": 0.92, "GBP": 0.78, "INR": 82.5},
    "EUR": {"USD": 1.09, "GBP": 0.85, "INR": 89.8},
    "GBP": {"USD": 1.28, "EUR": 1.18, "INR": 104.2},
    "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0096},
}

# Input fields
st.sidebar.header("Conversion Details")
from_currency = st.sidebar.selectbox("From Currency:", list(exchange_rates.keys()))
to_currency = st.sidebar.selectbox("To Currency:", list(exchange_rates.keys()))
amount = st.sidebar.number_input("Amount to Convert:", min_value=0.0, format="%.2f")

# Conversion logic
convert_button = st.sidebar.button("Convert Currency")

if convert_button:
    if from_currency == to_currency:
        st.warning("From Currency and To Currency are the same. No conversion needed.")
    else:
        try:
            # Retrieve the conversion rate
            conversion_rate = exchange_rates[from_currency][to_currency]
            converted_amount = amount * conversion_rate
            st.success(
                f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
            )
        except KeyError:
            st.error("Conversion rate not available for the selected currencies.")
