#Goal:
"""Open login page

both wrong inputs

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
url= "https://practicetestautomation.com/practice-test-loginz/"
try:
    driver.get(url)
    if "Page not found" in driver.title or "The page you are looking for" in driver.page_source:
     print ("404 not found")
     filename = "page_loading_issue_" +time.strftime("%Y%m%d_%H%M%S")+ (".png")
     driver.save_screenshot (filename)
     print ("Screenshot saved succesfully: ", filename)
     driver.quit()
     exit()
   
except Exception as e:
   print ("cannot reach: ",e)
   filename = "url_error_" + time.strftime("%Y%m%d_%H%M%S") + ".png"
   driver.save_screenshot(filename)
   print("📸 Screenshot saved as:", filename)
   driver.quit()

   exit ()

try:
 
    print ("Website opened successfully: ",driver.current_url)
    print ("Page title is: ", driver.title)
    driver.find_element (By.ID, "username"). send_keys ("students")
    driver.find_element (By.ID, "password"). send_keys ("Password1234")
    time.sleep (2)
    driver.find_element (By.ID, "submit"). click ()
    time.sleep (2)
    error_message= driver.find_element (By.ID, "error").text
    print ("Error message is:", error_message)
    expected = "Your username is invalid!"
    if expected in error_message:
     print ("Negative test passed: Error message is correct.")
    else:
     print("❌ Negative test failed: Error message is wrong.")
     time.sleep (2)
     filename= "login error_" + time.strftime ("%Y%m%d_%H%M%S") + ".png"
     driver.save_screenshot (filename)
     print ("Screenshot saved as ",filename)
except Exception as e:
    print("❌ Something went wrong during login test:", e)  
    filename= "login error_" + time.strftime ("%Y%m%d_%H%M%S") + ".png"
    driver.save_screenshot (filename)
    print ("Screenshot saved as ",filename)
driver.quit ()