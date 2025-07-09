"""1. Open the website
2. Select a color from dropdown
3. Choose a radio button ("Impressive")
4. Print both selected values
5. Take a screenshot
6. Close the browser"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get ("https://demoqa.com/select-menu")
time.sleep(2)
dropdown = driver.find_element (By.XPATH, "//select[@id='oldSelectMenu']")
select= Select (dropdown)
select.select_by_visible_text ("Purple")
time.sleep(3)
print("✅ Selected by visible text: Purple")
driver.save_screenshot ("Dropdown selected.png")
print ("screenshot saved successfully:Dropdown selected.png")

driver.get ("https://demoqa.com/radio-button")
time.sleep (2)
radio_button= driver.find_element (By.XPATH, "//label[@for='impressiveRadio']")
radio_button.click ()
time.sleep (2)
result= driver.find_element (By.CLASS_NAME, "text-success").text
print("✅ Radio button selected:", result)
driver.quit ()