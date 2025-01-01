import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)    #it's global, will wait for max 5 sec. wherever required in the script
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

listOriginal=[]
driver.find_element(By.XPATH, "//thead//th[1]/span[1]").click()
items = driver.find_elements(By.XPATH, "//tbody//td[1]")
for item in items:
    listOriginal.append(item.text)
listb = listOriginal.copy()
print(listOriginal)
listb.sort()
print(listb)
assert listb == listOriginal
"""print(set(listb) - set(listOriginal))
assert (set(listb) - set(listOriginal)) ==set()"""
