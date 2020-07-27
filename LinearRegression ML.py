import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

iris = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

x = iris.iloc[0]
y = iris.iloc[1]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
lr = LinearRegression()
lr.fit(x_train , y_train)
y_predict = lr.predict(x_test)

print( mean_squared_error(y_test, y_predict) )
