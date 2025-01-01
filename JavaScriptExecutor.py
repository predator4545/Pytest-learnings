from os.path import splitdrive

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""TO run test in headless mode(means to run script in backend)
"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

#search as "chrome options python" for more options
"""to ignore the certificates like ssl 'eg: your connection is not private' while launching a url"""
chrome_options.add_argument("--ignore-certificate-errors")

service_obj= Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)   #need to add options to run in headless mode
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)

"""All the browsers are rendered/created using JavaScripts, so sometime we might need to execute JavaScript, eg: Scrolling the webpage, but selenium don't have any inbuilt method to do that"""
"""Selenium will only give support to execute javascript using python/java etc.,"""

"""After inspecting a page, in console tab enter the command as below
window.scrollBy(0,500)    # this JavaScript command will scroll the page till y axis is 500
window.scrollBy(0,document.body.scrollHeight)     #this command will scroll to the end of the page
"""
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")  #using execute_script, we could send javascript commands to the browser
driver.get_screenshot_as_file("demo.png")    #to take screenshots, name can be any

