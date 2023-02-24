import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Create Login Add Employee And Disable Login Details by Okta Reza#

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
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click() # menu PIM
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click() # button Add Employee
        time.sleep(2)
        self.driver.find_element(By.NAME, "firstName").send_keys("asus") # isi nama first name
        time.sleep(1)
        self.driver.find_element(By.NAME, "middleName").send_keys("tuf") # isi nama middle name
        time.sleep(1)
        self.driver.find_element(By.NAME, "lastName").send_keys("a15") # isi nama last name
        time.sleep(1)

       # Klik switch button "Create Login Details"
        # Mengaktifkan switch button
        switch_button = self.driver.find_element(By.CLASS_NAME, "oxd-switch-input")
        switch_button.click()
        time.sleep(2)

        #klik username
        self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div[3]/div/div/div/div[2]/input").click()
        time.sleep(5) 
        
        #input username
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("asustuff_Gaming")
        time.sleep(3)

        #radio button disable
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-group:nth-child(2) .oxd-radio-input").click()
        time.sleep(3)

        # isi password di kolom password
        password_field = self.driver.find_element(By.CSS_SELECTOR, "input.oxd-input[type='password']")
        password_field.send_keys("Asustuf123!")
        time.sleep(3)

        # pindah ke kolom konfirmasi password menggunakan tab
        password_field.click()
        password_field.send_keys(Keys.TAB)
        time.sleep(6)

        # isi password di kolom konfirmasi password
        confirm_password_field = self.driver.find_element(By.CSS_SELECTOR, "input.oxd-input[type='password'][data-v-844e87dc]")
        ActionChains(self.driver).send_keys("Asustuf123!").perform()
        time.sleep(6)


        self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary").click() #klik save
        time.sleep(8)

    # assertion dan pesan
        self.assertEqual(self.driver.title, "OrangeHRM", msg="Gagal untuk testing")

    def tearDown(self):
        self.driver.quit()
        print("Hasil Testing Sesuai Dengan Test Case Yang Dikerjakan")

if __name__ == "__main__":
    unittest.main()
