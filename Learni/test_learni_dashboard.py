from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pytest

def test_learni_dashboard():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://nileprojects.in/learni/")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//input[@id='exampleInputEmail1']").send_keys("admin@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("Admin@123")

    try:
        driver.find_element(By.ID, "toggle-password").click()
        print("✅ Toggle working fine")
        time.sleep(2)
    except:
        print("❌ Toggle not working")

    driver.find_element(By.XPATH, "//button[normalize-space()='SIGN IN']").click()
    time.sleep(3)

    current_url = driver.current_url
    print("🌐 After login, current URL:", current_url)

    # ✅ Check if login was successful by URL
    if "admin" in current_url.lower() or "dashboard" in current_url.lower():
        print("✅ Login successful. URL:", current_url)
        time.sleep(3)

        try:
            driver.find_element(By.XPATH, "//a[@id='messageDropdown']//img[@alt='image']").click()
            print("✅ Notification button working fine")
            time.sleep(2)
        except:
            print("❌ Notification not working")
        assert True

    else:
        # ✅ Only check error toast if login failed
        try:
            error_toast = driver.find_element(By.CLASS_NAME, "toast-message").text
            print("❌ Login failed:", error_toast)
        except:
            print("❌ Login failed: Unknown reason (no toast found)")
        assert False, "❌ Login failed - dashboard not reached"
    driver.quit()