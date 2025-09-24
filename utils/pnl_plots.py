import numpy as np 
import plotly.graph_objects as go
from black_formula import black_scholes_price

def black_scholes_pnl_heatmap(K,T,r,spot_min,spot_max,vol_min,vol_max,purchase_price,steps=10,option="call"):
    spot_range=np.linspace(spot_min,spot_max,steps)
    vol_range=np.linspace(vol_min,vol_max,steps)
    z=np.empty((steps,steps))
    text=np.empty((steps,steps),dtype=object)
    for i,S0 in enumerate(spot_range):
        for j,sigma in enumerate(vol_range):
            call_price,put_price=black_scholes_price(S0,K,T,r,sigma)
            model_price=call_price if option=="call" else put_price
            pnl=model_price-purchase_price
            z[i,j]=pnl
            text[i,j]=f"{pnl:.2f}"
    colorscale=[[0,"red"],[0.5,"white"],[1,"green"]]

    fig=go.Figure(data=go.Heatmap(
        z=z,
        x=spot_range,
        y=vol_range,
        colorscale=colorscale,
        text=text,
        zmid=0,
        colorbar=dict(title="PnL"),
        texttemplate="%{text}",
        textfont=dict(color="black"),
        showscale=True
    ))

    fig.update_layout(
        x_axis_title='Spot Price',
        y_axis_title='Volatility',
        title=f'{option} Option PnL Heatmap'
    )
    return fig