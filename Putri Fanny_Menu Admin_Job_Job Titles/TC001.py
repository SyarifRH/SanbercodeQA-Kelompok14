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


# TC 1 Perform additional job data input tests by Putri Fanny#

class OHRM1(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_add_data(self):
        # steps login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin") # isi email
        time.sleep(2)
        browser.find_element(By.NAME, "password").send_keys("admin123") # isi password
        time.sleep(2)    
        browser.find_element(By.CLASS_NAME, "orangehrm-login-button").click() # button login
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik Admin
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() # klik Job
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click() # klik Job titles
        time.sleep(2)
        # isi data job title
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button").click() # klik Add
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("QA manualsss") # input job title
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").send_keys("test the application that will be released, create test cases, make a bug report") # input job desc
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea").send_keys("ini adalah catatan") # input note
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]").click() # klik submit
        time.sleep(6)

     # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList"
        self.assertEqual(expected_current_url,browser.current_url)

    def tearDown(self):
        self.browser.close() 
        print("Hasil Testing Sesuai Dengan Test Case Yang Dikerjakan")

if __name__ == "__main__":
    unittest.main()