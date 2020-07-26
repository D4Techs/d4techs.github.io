import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
lr = LinearRegression()
lr.fit(x_train , y_train)
y_predict = lr.predict(x_test)
from sklearn.matrics import mean_squared_error
mean_squared_error(y_test, y_predict)
