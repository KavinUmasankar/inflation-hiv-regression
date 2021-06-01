# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:52:51 2021

@author: kavin
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

inflation = pd.read_csv("Inflation_Data.csv").drop("Unnamed: 0", axis = 1).drop("0", axis = 1).rename(index = lambda x: 27 - x + 1990)
hiv = pd.read_csv("HIV_Data.csv").drop("Unnamed: 0", axis = 1).drop([0, 1], axis = 0)

for x in range(1990, 2018):
    inflation["1"][x] = float(inflation["1"][x][:-1])

for x in range(1990, 2018):
    hiv[str(x)][2] = float(hiv[str(x)][2].replace(",", ""))

x = np.array(list(hiv.iloc[0, :])).reshape((-1, 1))
y = np.array(list(inflation["1"]))

model = LinearRegression().fit(x, y)

print("slope: " + str(model.coef_[0]) + ", y-intercept: " + str(model.intercept_))