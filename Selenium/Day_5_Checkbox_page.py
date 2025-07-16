# Open the Checkbox page → Select a box → Confirm it's selected → Take screenshot → Close browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_checkbox_page():

   driver= webdriver.Chrome (service= Service (ChromeDriverManager().install()))
   driver.get ("https://demoqa.com/checkbox")
   time.sleep (2)
   try:
    expand_button=driver.find_element (By.XPATH, "//button[@title='Expand all']")
    expand_button.click ()
    print ("Expand button working")
   except Exception as e:
    print ("Expand button not showing", e)
   time.sleep (2)
   try:
    checkbox= driver.find_element (By.XPATH, "//span[@class='rct-title' and text()='Desktop']")
    checkbox.click ()
    print ("Desktop button working",)
   except Exception as e:
    print ("Desktop button not showing", e)
   filename="working_file_"+ time.strftime("%Y%m%d_%H%M%S") +".png"
   driver.save_screenshot (filename)
   print ("Screenshot saved: ",filename)
   time.sleep (2)