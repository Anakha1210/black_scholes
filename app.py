import streamlit as st
from black_scholes import black_scholes_price

st.title("Black-Scholes Option Pricing Calculator")

S0 = st.number_input("Current Stock Price (S0)", min_value=0.0, value=100.0, step=0.1)
K = st.number_input("Strike Price (K)", min_value=0.0, value=100.0, step=0.1)
T = st.number_input("Time to Maturity (Years)", min_value=0.01, value=1.0, step=0.01)
r = st.number_input("Risk-Free Interest Rate (r)", min_value=0.0, value=0.05, step=0.001)
sigma = st.number_input("Volatility (sigma)", min_value=0.0, value=0.2, step=0.01)

if st.button("Calculate Option Prices"):
    call_price, put_price = black_scholes_price(S0, K, T, r, sigma)
    st.write(f"Call Option Price: {call_price:.2f}")
    st.write(f"Put Option Price: {put_price:.2f}")
