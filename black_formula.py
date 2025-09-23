import numpy as np
from scipy.stats import norm

def black_scholes_price(S0,X,T,r,sigma):
    d1=((np.log(S0/X)+(r+0.5*sigma**2)*T))/(sigma*np.sqrt(T))
    d2=d1-sigma*np.sqrt(T)
    call=S0*norm.cdf(d1)-X*np.exp(-r*T)*norm.cdf(d2)
    put=X*np.exp(-r*T)*norm.cdf(-d2)-S0*norm.cdf(-d1)
    return call,put