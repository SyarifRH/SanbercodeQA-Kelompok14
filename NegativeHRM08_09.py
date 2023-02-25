import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import element
from data import inputan
import baseLogin



class TestPIMEmployeeList(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.Username = "Admin"
        self.password = "admin123"

    # Test HRM08 (Failed search employee list by employee name)
    def test_HRM_08(self):
        # Login
        driver = self.driver #buka web browser
        baseLogin.valid_login(driver)

        #Verifikasi valid Login
        valid_login = driver.find_element(By.XPATH, element.header).text
        self.assertIn(inputan.header_dashboard, valid_login)
    
        #PIM Menu
        driver.find_element(By.LINK_TEXT, element.PIM).click() #klik PIM menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,element.employee_list).click() #klik Employee list
        time.sleep(1)
        driver.find_element(By.XPATH, element.search_employee_by_name).send_keys("admin") #masukkan employee name
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, element.search_button).click() # klik search button
        time.sleep(2)

        #validation of error
        error_message= driver.find_element(By.XPATH, element.employee_not_found).text
        self.assertIn("No Records Found",error_message)


    def tearDown(self):
        self.driver.close()
        
        

if __name__ == "__main__":
    unittest.main()
    