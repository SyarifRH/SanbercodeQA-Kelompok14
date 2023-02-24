import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem
from page import link
from data import inputan
import baseLogin

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_login_success(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, link.dashboard_url)
        response_data = driver.find_element(By.CLASS_NAME,elem.top_header).text
        self.assertIn('Dashboard', response_data)


    def test_b_login_failed_upcase_usn(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_upcase_usn(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, link.dashboard_url)
        response_data = driver.find_element(By.CLASS_NAME,elem.top_header).text
        self.assertIn('Dashboard', response_data)

    def test_c_login_failed_wrong_usn(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_wrong_usn(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME,elem.inv_cred).text
        self.assertIn(inputan.inv_cred, response_data)

    def test_d_login_failed_wrong_pw(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_wrong_pw(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME,elem.inv_cred).text
        self.assertIn(inputan.inv_cred, response_data)

    def test_e_login_failed_blank_all(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_blank_all(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME,elem.required).text
        self.assertIn(inputan.required, response_data)

    def test_f_login_failed_blank_usn(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_blank_usn(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME,elem.required).text
        self.assertIn(inputan.required, response_data)

    def test_g_login_failed_blank_pw(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_blank_pw(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, link.base_url)
        response_data = driver.find_element(By.CLASS_NAME,elem.required).text
        self.assertIn(inputan.required, response_data)

    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()