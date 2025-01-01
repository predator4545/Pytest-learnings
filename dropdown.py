import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://rahulshettyacademy.com/angularpractice/")
#static Dropdown
"""Whenever there is a select tag in a webpage for a dropdown,then that dropdown is a static and we can use select class as below """
#dropdown=Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
#dropdown.select_by_visible_text("Female")
"""If value attribute is added in the dropdown tag, then we could us e selcct_by_value to select the text """
#dropdown.select_by_value()
#dropdown.select_by_index(1)

#Auto suggestive dynamic drop down
"""no select tag"""
service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com/")
driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").is_displayed()
driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").send_keys("lufthansa")
time.sleep(2)
options=driver.find_elements(By.CSS_SELECTOR, "li[class='sbct PZPZlf']") #value used here is not unique one, this value is representing multipe li tags, take note(we used elements)
for correctOne in options:
    if correctOne.text == "lufthansa careers":   #for checkboxes, If correctOne.getAttribute("value") == "xxxx":
        correctOne.click()
        break
"""we could use same method as above for checkboxes.etc too """



"""when we add a dynamic value using a automation script, then we can't use text method to retrieve the visible value"""
#print(driver.find_element(By.XPATH, "xxxxxxxxxxx").text)
"""in such case , we need to use as below"""
#print(driver.find_element(By.XPATH, "xxxxxxxx").get_attribute("value"))
