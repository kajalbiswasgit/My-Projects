from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome (service=Service(ChromeDriverManager().install()))
import time
driver.get ("https://flipkart.com")
driver.save_screenshot ("Flipkart_ss.png")
print ("The page title is:", driver.title)


time.sleep(2)