import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#if the chrome is latest/or not too old version, we can use this following method
"""driver= webdriver.Chrome()
#chrome driver service
driver.get("https://rahulshettyacademy.com")
time.sleep(2)
"""
#if the chrome version is too old, we need to download the chrome driver from online then paste the file path as below
service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#driver.get("https://rahulshettyacademy.com")
#time.sleep(2)
#driver.maximize_window()
print(driver.title)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("madmax")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("selfmade@ghmail.com")
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("password")
driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()

#static Dropdown
"""Whenever there is a select tag in a webpage for a dropdown,then that dropdown is a static and we can use select class as below """
dropdown=Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_visible_text("Female")
"""If value attribute is added in the dropdown tag, then we could us e select_by_value to select the text """
#dropdown.select_by_value()
#dropdown.select_by_index(1)

#Auto suggestive dynamic drop down
"""no select tag"""

time.sleep(2)
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text   #text will be returned for.eg: "Success! The Form has been submitted successfully!."
#text method used above will work only when the browser loads that string element. If the string is script generated, then text method won;t use,refer dropdown.py
#we could download "Selectorshub "plugin to inspect loccators
print(message)
assert "Success" in message   #will consider as PASS of it find Success in the message

driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()

driver.find_element(By.LINK_TEXT, "Shop").click()


mobiles=driver.find_elements(By.XPATH, "//body//app-root//app-card")

for mobile in range(1,len(mobiles)+1):
    print(driver.find_element(By.XPATH, f"//body//app-root//app-card[{mobile}]//h4/a").text)
    if driver.find_element(By.XPATH, f"//body//app-root//app-card[{mobile}]//h4/a").text == "Blackberry":
        driver.find_element(By.XPATH, f"//body//app-root//app-card[{mobile}]//button").click()
        break
print(driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").text)
assert "Checkout ( 1 )" in driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").text.strip()
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@id='country']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("India")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.close()


'''service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("qwertyuiop")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("qwertyuiop")
driver.find_element(By.XPATH, "//button[text()='Save New Password']" ).click()'''
