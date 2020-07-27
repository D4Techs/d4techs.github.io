import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
"""
LR: build regression model
train_test_split: split training & test data in dataset
mean_squared_error: find error in model
"""

iris = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
iris.columns = ["sepal.length", "sepal.width", "petal.length", "petal.width", "species"]

x = iris[["sepal.length"]]
y = iris[["sepal.width"]]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
lr = LinearRegression()
lr.fit(x_train , y_train)
y_predict = lr.predict(y_test)

print("Error in prediction: " + str( mean_squared_error(y_test, y_predict)  ) )
