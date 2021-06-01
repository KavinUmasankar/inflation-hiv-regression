# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:47:04 2021

@author: kavin
"""
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.macrotrends.net/countries/USA/united-states/inflation-rate-cpi")
table = driver.find_element_by_xpath("//div[@class='col-xs-6']")
data = table.text
driver.close()
data = data.split("\n")
for x in range(len(data)):
    data[x] = [data[x].split(" ")[0], data[x].split(" ")[1]]
data = pd.DataFrame(data)
data = data.drop([x for x in range(4)], axis = 0)
data.index = [num - 4 for num in data.index]
data = data.drop([x for x in range(28, 58)], axis = 0)
print(data)

data.to_csv("Inflation_Data.csv")
