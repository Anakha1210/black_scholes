import streamlit as st
from black_formula import black_scholes_price
from utils.plots import black_scholes_heatmap
from utils.pnl_plots import black_scholes_pnl_heatmap

st.set_page_config(
    page_title="Black-Scholes Calculator",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
    <style>
    .center-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
    .option-card {
        background: #181c23;
        border-radius: 16px;
        padding: 32px 48px;
        margin: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        text-align: center;
        color: #fff;
        min-width: 280px;
        font-family: 'Segoe UI', sans-serif;
    }
    .option-title {
        font-size: 2em;
        margin-bottom: 16px;
        font-weight: 600;
    }
    .option-label {
        font-size: 1.25em;
        margin-bottom: 8px;
        font-weight: 400;
    }
    .option-value {
        font-size: 2.5em;
        font-weight: bold;
        color: #41b883;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="center-container">
    <div class="option-card">
        <div class="option-title">Call Option Price</div>
        <div class="option-value">10.45</div>
    </div>
    <div class="option-card">
        <div class="option-title">Put Option Price</div>
        <div class="option-value">5.57</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

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
    spot_min=st.sidebar.number_input("Min Spot Price",value=50.0)
    spot_max=st.sidebar.number_input("Max Spot Price",value=150.0)
with heat_col2:
    vol_min=st.sidebar.number_input("Min Volitility",value=0.01)
    vol_max=st.sidebar.number_input("Max Volitility",value=1.0)
call_fig=black_scholes_heatmap(K,T,r,spot_min,spot_max,vol_min,vol_max,option="call")
put_fig=black_scholes_heatmap(K,T,r,spot_min,spot_max,vol_min,vol_max,option="put")

hm_col1,hm_col2=st.columns(2)

with hm_col1:
    st.plotly_chart(call_fig,use_container_width=True)
with hm_col2:
    st.plotly_chart(put_fig,use_container_width=True)

st.markdown("------------")

st.subheader("Interacticve PNL Heatmap Controls")


purchase_call = st.sidebar.number_input("Purchase Price (Call)", min_value=0.0, value=10.0, step=0.1)
purchase_put  = st.sidebar.number_input("Purchase Price (Put)",  min_value=0.0, value=5.0,  step=0.1)



st.subheader("Call Option PNL Heatmap")
st.plotly_chart(
    black_scholes_pnl_heatmap(K, T, r, spot_min, spot_max, vol_min, vol_max, purchase_call, option="call")
)

st.subheader("Put Option PNL Heatmap")
st.plotly_chart(
    black_scholes_pnl_heatmap(K, T, r, spot_min, spot_max, vol_min, vol_max, purchase_put, option="put")
)