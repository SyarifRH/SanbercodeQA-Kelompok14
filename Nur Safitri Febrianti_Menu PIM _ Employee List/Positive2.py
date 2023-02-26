import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from script import element
from info import data
import basicLogin



class TestPIMEmployeeList(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # Test HRM06 (success input data and reset data)
    def test_HRM_06(self):
        # Login
        driver = self.driver #buka web browser
        basicLogin.valid_login(driver)
    
        #PIM Menu
        driver.find_element(By.LINK_TEXT, element.PIM).click() #klik PIM menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,element.employee_list).click() #klik Employee list
        time.sleep(1)
        driver.find_element(By.XPATH, element.search_employee_by_name).send_keys("Admin") #masukkan employee name
        time.sleep(3)
        driver.find_element(By.XPATH, element.reset_button) #klik Reset button

        validate = driver.find_element(By.XPATH, element.reset_employee_name).get_attribute("value")
        self.assertIn('', validate)

    # Test HRM07 (success verify add button on employee list sub-menu)
    def test_HRM_07(self):
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
    