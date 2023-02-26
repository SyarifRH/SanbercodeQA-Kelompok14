import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from script import element
import basicLogin

class TestEmployeeList(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # Test HRM08 (Failed search employee list by employee name)
    def test_HRM_08(self):
        # Login
        driver = self.driver #buka web browser
        basicLogin.valid_login(driver)
    
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

    # Test HRM09 (Failed search employee list by employee Is)
    def test_HRM_09(self):
        # Login
        driver = self.driver #buka web browser
        basicLogin.valid_login(driver)
    
        #PIM Menu
        driver.find_element(By.LINK_TEXT, element.PIM).click() #klik PIM menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,element.employee_list).click() #klik Employee list
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, element.search_employee_by_Id).send_keys("2000") #masukkan employee id
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, element.search_button).click() # klik search button
        time.sleep(2)

        #validation of error
        error_Id= driver.find_element(By.XPATH, element.employee_not_found).text
        self.assertIn("No Records Found",error_Id)

    # Test HRM10 (failed add button on employee list sub-menu)
    def test_HRM_10(self):
        # Login
        driver = self.driver #buka web browser
        basicLogin.valid_login(driver)

        #PIM Menu
        driver.find_element(By.LINK_TEXT, element.PIM).click() #klik PIM menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,element.employee_list).click() #klik Employee list
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, element.add_button).click() # klik add button
        time.sleep(2)
        driver.find_element(By.NAME, element.first_name).send_keys("aku") # isi first name
        time.sleep(1)
        driver.find_element(By.NAME, element.middle_name).send_keys("saya") # isi middle name
        time.sleep(1)
        driver.find_element(By.NAME, element.last_name).send_keys("me") # isi last name
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, element.save_button).click() #klik save
        time.sleep(8)
       
       

    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()
    