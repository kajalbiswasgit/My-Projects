from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome (service=Service (ChromeDriverManager().install()))
driver.get ("https://demoqa.com/select-menu")
time.sleep (2)
driver.maximize_window ()
dropdown= driver.find_element(By.XPATH,"//select[@id='oldSelectMenu']" )
select= Select (dropdown)
select.select_by_visible_text ("Purple")
time.sleep(3)
print ("Purple is selected now")
driver.quit()