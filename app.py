import streamlit as st
from black_formula import black_scholes_price
from utilities.plots import black_scholes_heatmap


st.set_page_config(
    page_title="Black-Scholes Calculator",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
/* Add CSS styles here */
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(3)

with col1:
    S0 = st.number_input("Current Stock Price (S0)", 0.0, 1000.0, 100.0)
    K = st.number_input("Strike Price (K)", 0.0, 1000.0, 100.0)
    T = st.number_input("Time to Maturity (Years)", 0.01, 10.0, 1.0)

with col2:
    r = st.number_input("Risk-Free Interest Rate (r)", 0.0, 1.0, 0.05)
    sigma = st.number_input("Volatility (sigma)", 0.0, 1.0, 0.2)

if st.button("Calculate Option Prices"):
    call_price, put_price = black_scholes_price(S0, K, T, r, sigma)
    st.markdown("### Option Prices")
    st.write(f"Call Option Price: {call_price:.2f}")
    st.write(f"Put Option Price: {put_price:.2f}")
    
st.markdown("------------")

#heatmap
st.subheader("interacticve Heatmap Controls")
heat_col1,heat_col2=st.columns(2)

with heat_col1:
    spot_min=st.number_input("Min Spot Price",value=50.0)
    spont_max=st.numer_input("Max Spot Price",value=150.0)
with heat_col2:
    vol_min=st.number_input("Min Volitility",value=0.01)
    vol_max=st.number_input("Max Volitility",value=1.0)

fig=black_scholes_heatmap(K,T,r,spot_min,spot_max,vol_min,vol_max)
st.plotly_chart(fig,use_container_width=True)