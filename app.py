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
.option-cards {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
}
.option-card {
  background: linear-gradient(180deg, #ffffff 0%, #f7f9fb 100%);
  border-radius: 12px;
  padding: 14px;
  box-shadow: 0 6px 18px rgba(12,34,56,0.08);
  width: 220px;
  text-align: left;
  border: 1px solid #e6eef8;
}
.option-label {
  font-size: 13px;
  color: #6b7280;
  margin-bottom: 6px;
}
.option-value {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: 0.2px;
}
.call-accent { color: #0b875b; }   /* green */
.put-accent  { color: #c53030; }  /* red */
</style>

<div class="option-cards">
  <div class="option-card">
    <div class="option-label">📈 CALL Value</div>
    <div class="option-value call-accent">${call_price:.2f}</div>
  </div>

  <div class="option-card">
    <div class="option-label">📉 PUT Value</div>
    <div class="option-value put-accent">${put_price:.2f}</div>
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