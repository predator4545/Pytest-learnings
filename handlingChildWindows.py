from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()   #Whenever there is a link tag(a), then we could use LINK_TEXT as a locator

windowsopened = driver.window_handles    #will get window names of all the windows currently opened by automation, not an already existing windows
# windows names are stored in a list format
driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() # closing the xcurrent child windows
#switching back to parent window
driver.switch_to.window(windowsopened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)