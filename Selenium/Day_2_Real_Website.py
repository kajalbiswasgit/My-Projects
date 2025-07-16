from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= webdriver.Chrome (service=Service(ChromeDriverManager().install()))
try:
    driver.get ("https://linkedin.com")
    time.sleep (5)
    print ("The page title is:", driver.title)
    print ("The current URL is:", driver.current_url)
    filename= "linkedin_" + time.strftime ("%Y%m%d_%H%M%S") + ".png"
    driver.save_screenshot (filename)
    print ("Screenshot saved successfully ", filename)
except Exception:
    print("something went worng")
    driver.quit ()
try:
    driver.get ("https://bbc.com")
    time.sleep (5)
    print ("The page title is:", driver.title)
    print ("The current URL is:", driver.current_url)
    filename= "bbc_" + time.strftime ("%Y%m%d_%H%M%S") + ".png"
    driver.save_screenshot (filename)
    print ("Screenshot saved successfully ", filename)
except Exception:
    print("something went worng")
    driver.quit ()