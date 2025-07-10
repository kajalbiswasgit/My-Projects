# One simple login test with screenshot on failure

"""Opens browser

1. Goes to login page

2. Enters username & password

3. Clicks Login

4. Checks if login was successful

5. If failed → takes screenshot

6. Prints pass/fail ✅❌

7. Closes browser

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver= webdriver.Chrome (service=Service (ChromeDriverManager().install()))
import time
driver.get ("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window ()
time.sleep(2)

driver.find_element (By.ID, "username").send_keys("student")
driver.find_element (By.ID, "password").send_keys("Password123")
driver.find_element (By.ID, "submit").click ()
time.sleep (2)

if "Logged In Successfully" in driver.title:
    time.sleep (2)
    print ("Loggedin Successfully")

else:
    print ("Login failed.taking screenshot")
    filename= "Login_failed" + time.strftime ("%Y%m%d_%H%M%S") + ".png"
    driver.save_screenshot (filename)
    print ("screeenshot saved successsfully", filename)
driver.quit ()