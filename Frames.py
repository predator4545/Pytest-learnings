from os.path import splitdrive

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)

driver.switch_to.frame("mce_0_ifr")  #we need to switch to frames, then only the following script will work
"""frames are a seperate thing attached above a html page """
"""iframe tag will be presents"""
#driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("i am basha")

driver.switch_to.default_content()  # used to switch back to origin page

