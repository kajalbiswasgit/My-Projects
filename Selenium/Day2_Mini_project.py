# Goal:

"""Open a news website

Print the page title

Take a screenshot

Print the current URL

Then close the browser"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= webdriver.Chrome (service=Service(ChromeDriverManager().install()))
try:
    driver.get ("https://www.news18.com/")
    print("New18 opened successsfully")
    time.sleep(5)  
    print ("Page title is: ",driver.title)
   # Short dynamic screenshot name (one line)
    filename= "News18_ss_" + time.strftime ("%Y%m%d_%H%M%S")+ ".png"
    driver.save_screenshot (filename)
    print ("Screenshot saved successfully: ", filename)
    driver.current_url
    print ("Page url is:", driver.current_url)
except Exception:
    print ("Something went wrong")

driver.quit()
