from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome (service=Service(ChromeDriverManager().install()))
driver.get ("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window ()
time.sleep (2)
driver.find_element (By.XPATH, "//input[@id='username']").send_keys ("student")
driver.find_element (By.XPATH, "//input[@id='password']").send_keys ("Password@123")
time.sleep (2)
driver.find_element (By.XPATH, "//button[@id='submit']").click()
time.sleep (3)
try:
    error= driver.find_element (By.XPATH, "//div[@id='error']").text.strip ()
    expected_error = "Your password is invalid!"
    if expected_error in error:
        print ("Wrong password test passed: Correct error message shown.")
    else:
        print("❌ Actual error message is:", error)
except Exception as e:
    print ("something went wrong", e)
