from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("max")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert=driver.switch_to.alert
 #to get the text
print(alert.text)
assert "max" in alert.text
alert.accept()
#alert.dismiss()