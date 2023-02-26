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


# TC 7 Test the delete button on the job titles form by Putri Fanny#

class OHRM7(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_button_delete(self):
        # steps
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.NAME, "username").send_keys("Admin")  # isi email
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")  # isi password
        time.sleep(1)
        browser.find_element(
            By.CLASS_NAME, "orangehrm-login-button").click()  # button login
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()  # klik Admin
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click()  # klik Job
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click()  # klik Job titles
        time.sleep(5)

        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[4]/div/button[1]").click()  # klik delete
        time.sleep(4)
        browser.find_element(
            By.XPATH, "/html/body/div/div[3]/div/div/div/div[3]/button[2]").click()  # klik Yes, Delete
        time.sleep(4)

        # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList"
        self.assertEqual(expected_current_url, browser.current_url)

    def tearDown(self):
        self.browser.close()
        print("Hasil Testing Sesuai Dengan Test Case Yang Dikerjakan")


if __name__ == "__main__":
    unittest.main()
