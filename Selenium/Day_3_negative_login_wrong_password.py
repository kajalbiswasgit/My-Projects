#Goal:
"""Open login page

Enter correct username but wrong password

Click Login

Check if error message appears

Print message and validate it

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= webdriver.Chrome (service=Service(ChromeDriverManager().install()))
try:
 
 driver.get ("https://practicetestautomation.com/practice-test-login/")
 time.sleep(5)
 print ("Website opened successfully: ",driver.current_url)
 print ("Page title is: ", driver.title)
 driver.find_element (By.ID, "username"). send_keys ("student")
 driver.find_element (By.ID, "password"). send_keys ("wrongpassword")
 driver.find_element (By.ID, "submit"). click ()
 time.sleep (5)
 error_message= driver.find_element (By.ID, "error").text
 print ("Error message is:", error_message)
 expected = "Your password is invalids!"
 if expected in error_message:
   print ("Negative test passed: Error message is correct.")
 else:
     print("❌ Negative test failed: Error message is wrong.")
except Exception as e:
  print ("something went wrong: ", e)
  driver.quit ()