# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:24:32 2020

@author: Nicholas Sotiriou - github: @nsotiriou88 // nsotiriou88@gmail.com


Excercise: Monte Carlo Simulation on Value at Risk (1 stock)

link: https://programmingforfinance.com/2017/12/var-via-monte-carlo-simulation/

We are taking the last days price and multiplying it by 1 + a random shock
which is created by drawing a sample of the distribution given the historical
volatility of an asset.
"""

'''
As implied by the title of this post, we will be estimating Value at Risk via
a Monte Carlo approach. What we are doing here is generating future prices via
a probability simulation of future outcomes. We will generate the stock
movement based on the asset’s historical volatility. With this historical
volatility, there will be an element of randomness or a random “shock.”
Different Monte Carlo models may require different inputs. By analyzing
historical data, we can determine volatility, the average daily return, and
drift of an asset. All of these can be used within a Monte Carlo model. Let’s
take a look at the formula used to generate the next day’s price.

We are taking the last days price and multiplying it by 1 + a random shock
which is created by drawing a sample of the distribution given the historical
volatility of an asset.
'''


# Import libraries
import numpy as np
import pandas as pd
import quandl
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = "eGY3srpm6Gmzh6-K-CtS"

symbols = ["WIKI/AAPL.4"]
data = quandl.get(symbols, start_date="2015-12-31", end_date="2017-10-31",
                  collapse="daily")
rets = data.pct_change()
rets = rets[1:]

daily_vol = rets.std()
daily_ret = rets.mean()
    
simulation_df = pd.DataFrame()

num_simulations = 10000
predicted_days = 252

last_price = data.iloc[-1:,0][0]

#Create Each Simulation as a Column in df
for x in range(num_simulations):
    
    count = 0
    
    price_series = []
    price_series.append(last_price)
        
    #Series for Preditcted Days
    for i in range(predicted_days):
        if count == 251:
            break
        
        # price = price_series[count] + price_series[count] * (daily_ret + 
        #                             daily_vol * np.random.normal(0, 1))
        
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))

        price_series.append(price)
        count += 1

    simulation_df[x] = price_series

plt.plot(simulation_df)

price_array = simulation_df.iloc[-1, :]
price_array = sorted(price_array, key=int)
 
var =  np.percentile(price_array, .95)
var1 =  np.percentile(price_array, .99)
var2 =  np.percentile(price_array, .9999)

print("VaR at 95% Confidence: " + '${:,.2f}'.format(last_price - var))
print("VaR at 99% Confidence: " + '${:,.2f}'.format(last_price - var1))
print("VaR at 99.99% Confidence: " + '${:,.2f}'.format(last_price - var2))

plt.hist(price_array, normed=True)
plt.xlabel('Price')
plt.ylabel('Probability')
plt.title(r'Histogram of Simulated Stock Prices', fontsize=18,
          fontweight='bold')
plt.axvline(x=var, color='r', linestyle='--',
            label='Price at Confidence Interval: ' + str(round(var, 2)))
plt.axvline(x=last_price, color='k', linestyle='--',
            label = 'Current Stock Price: ' + str(round(last_price, 2)))
plt.legend(loc='upper right', fontsize = 'x-small')
plt.show()

'''
Analyzing the outputted histogram, the current stock price is located at the
center of the distribution. The Value at Risk would be the current stock price
subtracted from the price 5’th percentile price of the distribution. Below is
what the Value at Risk metrics would be at different confidence intervals.
'''
