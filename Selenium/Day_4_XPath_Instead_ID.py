#Why XPath?
"""
Sometimes, By.ID or By.NAME won’t be available,,,

XPath lets you locate any element by:
text
attributes
partial match
position, etc."""

# Basic XPath Syntax: driver.find_element(By.XPATH, "//tagname[@attribute='value']")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= webdriver.Chrome (service= Service(ChromeDriverManager().install()))
driver.get ("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window ()
time.sleep (2)

# ✅ Use XPath instead of ID
driver.find_element (By.XPATH, "//input[@id='username']").send_keys ("student")
driver.find_element (By.XPATH, "//input[@id='password']").send_keys ("Password123")
driver.find_element (By.XPATH, "//button[@id='submit']").click ()
time.sleep (4)
if "Logged In Successfully" in driver.title:
    print ("Loggedin success using Xpath")
else:
    print ("Loggedin failed using Xpath")
driver.quit ()