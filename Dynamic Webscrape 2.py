# -*- coding: utf-8 -*-
"""
Created on Sun May 23 09:44:38 2021

@author: kavin
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://ourworldindata.org/grapher/deaths-and-new-cases-of-hiv?country=~OWID_WRL")

button = driver.find_element_by_xpath("//li[@class='tab clickable']")
button.click()

end = driver.find_element_by_xpath("//div[@class='handle endMarker']")

move = ActionChains(driver)
#move.click_and_hold(end).move_by_offset(-675, 0).release().perform()

Full = {}
Info = {}

Deaths = []
New = []
Living = []

start = driver.find_element_by_xpath("//div[@class='handle startMarker']")
end = driver.find_element_by_xpath("//div[@class='handle endMarker']")

for x in range(28):
    print(x + 1990)
    if x < 27:
        Deaths.append(driver.find_element_by_xpath("//tr[218]/td[2]").text)
        New.append(driver.find_element_by_xpath("//tr[218]/td[6]").text)
        Living.append(driver.find_element_by_xpath("//tr[218]/td[10]").text)
    else:
        Deaths.append(driver.find_element_by_xpath("//tr[218]/td[2]").text)
        New.append(driver.find_element_by_xpath("//tr[218]/td[3]").text)
        Living.append(driver.find_element_by_xpath("//tr[218]/td[4]").text)
    print([Deaths[x], New[x], Living[x]])
    Full[x + 1990] = [Deaths[x], New[x], Living[x]]
    Info[x + 1990] = Living[x]
    time.sleep(0.5)
    if x < 27:
        ActionChains(driver).click_and_hold(start).move_by_offset(25, 0).release().perform()
        time.sleep(0.5)
time.sleep(3)

driver.close()