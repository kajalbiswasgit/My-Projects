#| Task                          | Skill                  |
"""| --------------------------- | ---------------------- |
| Fill in username & password    | `send_keys()`          |
| Click a button                 | `click()`              |
| Get feedback message           | `.text`                |
| Validate login success/fail    | `assert`, `if-else`    |
| Practice with a live demo site | Real-world interaction |
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # ✅ Add this
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= webdriver.Chrome (service=Service(ChromeDriverManager().install()))
try:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep (5)
    # Step 1: Enter username
    driver.find_element(By.ID, "username"). send_keys ("student")
    # Step 2: Enter password
    driver.find_element(By.ID, "password").send_keys("Password123")
    # Step 3: Click the Login button
    driver.find_element(By.ID, "submit").click ()
    time.sleep(5)
    # Step 4: Check if login success message appears
    success_message= driver.find_element (By.TAG_NAME, "h1").text
    print ("The success message is: ", success_message)
    # Step 5: Validate
    if "Logged In Successfully" in success_message:
     print ("Logged In Successfully")
    else:
     print ("Login failed")
except Exception:
     print("Something went wrong")
driver.quit()