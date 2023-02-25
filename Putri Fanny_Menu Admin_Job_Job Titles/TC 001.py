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


# TC 1 Find a username if the field of username and employee name are left empty by Putri Fanny#

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
        # steps
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123") # isi password
        time.sleep(1)    
        browser.find_element(By.CLASS_NAME, "orangehrm-login-button").click() # button login
        time.sleep(2)
        browser.find_element(By.XPATH, "//span[text()='Admin']").click() # klik Admin
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("") # kosongkan field username
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input").send_keys("") # kosongkan field Employee Name
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik button search
        time.sleep(2)
        
     # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        self.assertEqual(expected_current_url,browser.current_url)

    def tearDown(self):
        self.browser.close() 
        print("Hasil Testing Sesuai Dengan Test Case Yang Dikerjakan")

if __name__ == "__main__":
    unittest.main()