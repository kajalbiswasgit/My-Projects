from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
driver = webdriver.Chrome (service=Service(ChromeDriverManager().install()))
try:
    driver.get ("https://thiswebsitedoesnotexistanywhere999.com")
    
    time.sleep (2)
except Exception:
    print ("Something went wrong:")

driver.quit()
