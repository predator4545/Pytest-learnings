import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)    #it's global, will wait for max 5 sec. wherever required in the script
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

lista=["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Vegetables and Fruits']").send_keys("ber")

items=driver.find_elements(By.XPATH, "//div[@class='product']//button")
i=0
lists=[]
for item in items:
    if item.text == "ADD TO CART":
        i=i+1
        lists.append(driver.find_element(By.XPATH, f"(//div[@class='product']//h4)[{i}]").text)
        item.click()

assert lista==lists

if driver.find_element(By.XPATH, "//a[@class='cart-icon']").is_displayed():
    driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()

    driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()



TotalValue=0
for i in range(1,i+1):
    TotalValue=TotalValue+int(driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[5]").text)
print(TotalValue)
assert TotalValue == int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait=WebDriverWait(driver,10)
promoApplied=driver.find_element(By.CSS_SELECTOR, ".promoInfo")
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo"))) #explicit used when we need to target particular element

discountenance=float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
actualValue=float(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
assert discountenance < actualValue








