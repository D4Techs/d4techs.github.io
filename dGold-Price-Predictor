# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:06:04 2020
@author: durgesh.vishwakarma
"""
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#https://in.finance.yahoo.com/quote/GLD/history?p=GLD
Df = pd.read_excel("D:\Gold Price Yahoo.xlsx")
Df.index = Df["Date"]
# Only keep close columns
Df = Df[['Close']]
print( Df.head() )

# Drop rows with missing values
Df = Df.dropna()

# Plot the closing price of GLD
Df.Close.plot(figsize=(10, 7),color='r')
#plt.ylabel("Gold ETF Prices")
#plt.title("Gold ETF Price Series")
plt.show()

# Define explanatory variables
Df['S_3'] = Df['Close'].rolling(window=3).mean()
Df['S_9'] = Df['Close'].rolling(window=9).mean()
Df['next_day_price'] = Df['Close'].shift(-1)

Df = Df.dropna()
X = Df[['S_3', 'S_9']]

# Define dependent variable
y = Df['next_day_price']
# Split the data into train and test dataset
t = .8
t = int(t*len(Df))

# Train dataset
X_train, y_train = X[:t], y[:t]
# Test dataset
X_test, y_test = X[t:], y[t:]

# Create a linear regression model
linear = LinearRegression().fit(X_train, y_train)
print("Linear Regression model")
print("Gold ETF Price (y) = %.2f * 3 Days Moving Average (x1) \
+ %.2f * 9 Days Moving Average (x2) \
+ %.2f (constant)" % (linear.coef_[0], linear.coef_[1], linear.intercept_))

# Predicting the Gold ETF prices
predicted_price = linear.predict(X_test)
predicted_price = pd.DataFrame(
    predicted_price, index=y_test.index, columns=['price'])
predicted_price.plot(figsize=(10, 7))
y_test.plot()
plt.legend(['predicted_price', 'actual_price'])
#plt.ylabel("Gold ETF Price")
plt.show()

# R square
r2_score = linear.score(X[t:], y[t:])*100
print( float("{0:.2f}".format(r2_score)) )

gold = pd.DataFrame()

gold['price'] = Df[t:]['Close']
gold['predicted_price_next_day'] = predicted_price
gold['actual_price_next_day'] = y_test
gold['gold_returns'] = gold['price'].pct_change().shift(-1)

gold['signal'] = np.where(gold.predicted_price_next_day.shift(1) < gold.predicted_price_next_day,1,0)

gold['strategy_returns'] = gold.signal * gold['gold_returns']
((gold['strategy_returns']+1).cumprod()).plot(figsize=(10,7),color='g')
#plt.ylabel('Cumulative Returns')
plt.show()

print('Sharpe Ratio %.2f' % (gold['strategy_returns'].mean()/gold['strategy_returns'].std()*(252**0.5)) )

Df["predicted"] = linear.predict(Df[ ['S_3', 'S_9'] ] )
Df["Diff"] = Df["predicted"] - Df["Close"]

plt.plot(Df.index, Df["next_day_price"])
plt.plot(Df.index, Df["predicted"])
plt.legend( ['Actual Price', 'Predicted Price'] )
plt.show()
