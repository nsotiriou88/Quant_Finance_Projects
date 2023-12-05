import pandas as pd
import pandas_datareader.data as web
import numpy as np
import datetime as dt
import math

import matplotlib.pyplot as plt


def combos(n, i):
    return math.factorial(n) / (math.factorial(n-i)*math.factorial(i))



def binom_EU1(S0, K , T, r, sigma, N, type_ = 'call'):
    dt = T/N
    u = np.exp(sigma * np.sqrt(dt))
    d = np.exp(-sigma * np.sqrt(dt))
    p = (  np.exp(r*dt) - d )  /  (  u - d )
    value = 0 
    for i in range(N+1):
        node_prob = combos(N, i)*p**i*(1-p)**(N-i)
        ST = S0*(u)**i*(d)**(N-i)
        if type_ == 'call':
            value += max(ST-K,0) * node_prob
        elif type_ == 'put':
            value += max(K-ST, 0)*node_prob
        else:
            raise ValueError("type_ must be 'call' or 'put'" )
    
    return value*np.exp(-r*T)


def get_data(symbol):
    obj = web.YahooOptions(f'{symbol}')
    
    df = obj.get_all_data()

    df.reset_index(inplace=True)

    df['mid_price'] = (df.Ask+df.Bid) / 2
    df['Time'] = (df.Expiry - dt.datetime.now()).dt.days / 255
    
    return df[(df.Bid>0) & (df.Ask >0)]


df = get_data('TSLA')

prices = [] 


for row in df.itertuples():
    price = binom_EU1(row.Underlying_Price, row.Strike, row.Time, 0.01, 0.5, 20, row.Type)
    prices.append(price)
    
    
df['Price'] = prices
    
df['error'] = df.mid_price - df.Price 
    
    
exp1 = df[(df.Expiry == df.Expiry.unique()[2]) & (df.Type=='call')]


plt.plot(exp1.Strike, exp1.mid_price,label= 'Mid Price')
plt.plot(exp1.Strike, exp1.Price, label = 'Calculated Price')
plt.xlabel('Strike')
plt.ylabel('Call Value')
plt.legend()
