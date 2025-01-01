from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
action = ActionChains(driver)
#action.click_and_hold()  #used to grab something
#action.double_click()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()   #.perform() is a must, to execute the actions
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()  #context_click means Right click
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()