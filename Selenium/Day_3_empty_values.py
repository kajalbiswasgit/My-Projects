# (Blank Field Test + Screenshot)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= webdriver.Chrome (service= Service (ChromeDriverManager().install()))
driver.get ("https://practicetestautomation.com/practice-test-login/")
time.sleep (2)
driver.find_element (By.ID, "username"). send_keys ("")
driver.find_element (By.ID, "password"). send_keys ("")
driver.find_element (By.ID, "submit"). click ()
time.sleep(4)
try:
    error= driver.find_element (By.ID, "error").text
    if "Your username is invalid!" in error:
        print("✅ Empty field test passed: Error message appeared.")
    else:
        print ("Error message did not match:", error)
        filename= "failed_message" + time.strftime("%Y%m%d_%H%M%S") + ".Png"
        driver.save_screenshot(filename)
        print ("screenshot saved successfully:", filename)
except Exception as e:
        print ("something went wrong", e)
driver.quit ()


