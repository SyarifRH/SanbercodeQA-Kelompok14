import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


#Save not input disable by Okta Reza#

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
        self.driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='PIM']").click()  # klik PIM
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click() # Klik add employee
        time.sleep(2)

        # Klik switch button "Create Login Details"
        # Mengaktifkan switch button
        switch_button = self.driver.find_element(By.CLASS_NAME, "oxd-switch-input")
        switch_button.click()
        time.sleep(2)

        #radio button disable
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-group:nth-child(2) .oxd-radio-input").click()
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary").click() #klik save
        time.sleep(8)
    
        
    # assertion dan pesan
        self.assertEqual(self.driver.title, "OrangeHRM", msg="Gagal untuk testing")

    def tearDown(self):
        self.driver.quit()
        print("Hasil Testing Sesuai Dengan Test Case Yang Dikerjakan")

if __name__ == "__main__":
    unittest.main()
