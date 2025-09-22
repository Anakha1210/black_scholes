import numpy as np
from scipy.stats import norm

def blach_scholes_price(S0,X,T,r,sigma):
    d1=((np.log(S0/X)+((r+sigma**2)/2)*T))/(sigma*np.sqrt(T))
    d2=((np.log(S0/X)+((r-sigma**2)/2)*T))/(sigma*np.sqrt(T))
    call=S0*norm.cdf(d1)+X*np.exp(-r*T)*norm.cdf(d2)
    put=X*np.exp(-r*T)*norm.cdf(-d2)-S0*norm.cdf(-d1)
    return call,put