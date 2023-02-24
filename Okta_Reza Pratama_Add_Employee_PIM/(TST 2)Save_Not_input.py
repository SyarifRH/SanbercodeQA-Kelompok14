import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# TST 2 Save Not Input by Okta Reza#

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
        # steps
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin") # isi email
        time.sleep(1)
        self.driver.find_element(By.NAME, "password").send_keys("admin123") # isi password
        time.sleep(1)    
        self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click() # button login
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click() # klik PIM
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click() # klik add employee
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary").click() #klik save
        time.sleep(8)
       

    # assertion dan pesan
        self.assertEqual(self.driver.title, "OrangeHRM", msg="Gagal untuk testing")

    def tearDown(self):
        self.driver.quit()
        print("Hasil Testing Sesuai Dengan Test Case Yang Dikerjakan")


if __name__ == "__main__":
    unittest.main()
