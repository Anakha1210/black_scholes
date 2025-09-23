import numpy as np
import plotly.graph_objects as go
from black_formula import black_scholes_price 


def black_scholes_heatmap(K,T,r,spot_min, spot_max, vol_min, vol_max, steps=10,option="call"):
    spot_range=np.linspace(spot_min,spot_max,steps)
    vol_range=np.linspace(vol_min,vol_max,steps)
    z=np.zeros((steps,steps))
    for i,S0 in enumerate(spot_range):
        for j,sigma in enumerate(vol_range):
            call_price,put_price=black_scholes_price(S0,K,T,r,sigma)
            z[i,j]=call_price if option_type=="call" else put_price
    fig=go.Figure(data=go.Heatmap(
        z=z,
        x=spot_range,
        y=vol_range,
        colorscale='Viridis',
        colorbar=dict(title="Call Price")
    ))
    
    fig.update_layout(
        xaxis_title="Spot Price",
        yaxis_title="Volatility",
        title=f"{option_type} option Price Heatmap"
    )
    return fig