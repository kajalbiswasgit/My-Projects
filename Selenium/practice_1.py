from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get ("https://google.com")
driver.save_screenshot ("google_front.png")
time.sleep(2)

driver.get ("https://facebook.com")
time.sleep(2)

driver.quit