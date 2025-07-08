from selenium import webdriver #You're telling Python: “I want to use Selenium WebDriver — the tool that controls a browser.
from selenium.webdriver.chrome.service import Service #You're saying: “I’ll use a Service to run ChromeDriver in the background
from webdriver_manager.chrome import ChromeDriverManager #You’re saying: “Don’t make me manually download anything. This saves you from confusing version issues later
import time #You're bringing in Python’s time feature so you can pause the program for a few seconds

# Automatically installs correct ChromeDriver
service = Service(ChromeDriverManager().install())

# Launch browser
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Wait for 3 seconds
time.sleep(3)

# Close browser
driver.quit()
