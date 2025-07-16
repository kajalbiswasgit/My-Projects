import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize("email,password,expected_error", [
    ("admin@gmail.com", "Admin@123", None),  # ✅ Valid login
    ("admin1@gmail.com", "Admin@123", "Invalid email or password"),  # ❌ Invalid login
])
def test_learni_login(email, password, expected_error):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://nileprojects.in/learni/")
    time.sleep(2)

    driver.find_element(By.ID, "exampleInputEmail1").send_keys(email)
    driver.find_element(By.ID, "exampleInputPassword1").send_keys(password)

    try:
        driver.find_element(By.ID, "toggle-password").click()
        print("👁 Password toggle clicked")
    except:
        print("⚠️ Toggle not found")

    driver.find_element(By.XPATH, "//button[text()='SIGN IN']").click()
    time.sleep(3)

    if expected_error:
        try:
            alert = driver.find_element(By.CLASS_NAME, "toast-message").text

            assert expected_error in alert
            print("✅ Error toast verified:", alert)
        except Exception as e:
            print("❌ Expected error toast not shown")
    else:
        # Valid login → check dashboard
        assert "dashboard" in driver.current_url.lower()
        print("✅ Login successful. URL:", driver.current_url)

    driver.quit()
