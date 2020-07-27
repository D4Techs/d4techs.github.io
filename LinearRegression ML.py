import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
"""
LR: build regression model
train_test_split: split training & test data in dataset
mean_squared_error: find error in model

COLs in dataset: n1,n2,n1_sq,n1_cube,2*n1,3*n1,2*n1+5,n1*n2+10
@save below as "regTest.csv "
n1,n2,n1_sq,n1_cube,2*n1,3*n1,2*n1+5,n1*n2+10
1,1,1,1,2,3,7,11
2,6,4,8,4,6,9,22
3,6,9,27,6,9,11,27
4,4,16,64,8,12,13,26
5,1,25,125,10,15,15,13
"""
dataset = pd.read_csv("regTest.csv")

dataset.head()
x = dataset[["n1"]]
y = dataset[["2*n1+5"]]

#split train & test data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

#create LinerReg model;train; predict
lr = LinearRegression()
lr.fit(x_train , y_train)
y_predict = lr.predict(x_test)

#Calc error in model [test_data - predicted_data
print("Error : " + str( mean_squared_error(y_test, y_predict) ) )

#predict output for given input
lr.predict(8.31)
