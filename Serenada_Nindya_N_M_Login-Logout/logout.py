import unittest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem
from page import link
from data import inputan
import login
import baseLogin

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_logout_success(self):
        # steps
        #login
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)
        #login.test_a_login_success(self)

        #logout
        driver.find_element(By.CLASS_NAME, elem.user_drop).click() #isi email
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click() # menu Logout
        time.sleep(2)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME,elem.login_page).text
        self.assertIn(inputan.login_title, response_data)


    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()