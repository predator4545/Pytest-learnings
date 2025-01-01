from os.path import splitdrive

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)


driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
lista=(driver.find_element(By.XPATH, "//p[@class='im-para red']").text).strip().split(" ")
print(lista)
email=""
for i in lista:
    if ".com" in i:
        email=i
        break
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("qwertyuio")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver,10)
assert wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//strong[normalize-space()='Incorrect']")))