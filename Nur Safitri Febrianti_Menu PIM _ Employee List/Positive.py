import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from script import element
from info import data
import basicLogin


class TestPIMEmployeeList(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # Test HRM01 (Success search employee list by employee name)
    def test_HRM_01(self):
        # Login
        driver = self.driver #buka web browser
        basicLogin.valid_login(driver)

        #PIM Menu
        driver.find_element(By.LINK_TEXT, element.PIM).click() #klik PIM menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,element.employee_list).click() #klik Employee list
        time.sleep(1)
        driver.find_element(By.XPATH, element.search_employee_by_name).send_keys("Garry") #masukkan nama employee
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, element.search_button).click() # klik search button
        time.sleep(1)

        response_data= driver.find_element(By.LINK_TEXT, element.employee_list).text
        self.assertEqual(response_data, data.employee_list)
    
    # Test HRM02 (Success search employee list by employee id)
    def test_HRM_02(self):
        # Login
        driver = self.driver #buka web browser
        basicLogin.valid_login(driver)
    
        #PIM Menu
        driver.find_element(By.LINK_TEXT, element.PIM).click() #klik PIM menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,element.employee_list).click() #klik Employee list
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, element.search_employee_by_Id).send_keys("0016") #masukkan employee id
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, element.search_button)
        time.sleep(2)

        response = driver.find_element(By.LINK_TEXT,element.employee_list).text
        self.assertEqual(response, data.employee_list)
    
    # Test HRM03 (Success search employee list by employent status)
    def test_HRM_03(self):
        # Login
        driver = self.driver #buka web browser
        basicLogin.valid_login(driver)
    
        #PIM Menu
        driver.find_element(By.LINK_TEXT, element.PIM).click() #klik PIM menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,element.employee_list).click() #klik Employee list
        time.sleep(1)
        driver.find_element(By.XPATH, element.select_employment_status).click()
        time.sleep(2)
        driver.find_element(By.XPATH,element.select_full_time_contract).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, element.search_button)
        time.sleep(2)

        employment_status = driver.find_element(By.XPATH, element.employee_information).text
        self.assertIn("Full-Time Contract", employment_status)
    
    # Test HRM04 (Success search employee list by job title)
    def test_HRM_04(self):
        # Login
        driver = self.driver #buka web browser
        basicLogin.valid_login(driver)
    
        #PIM Menu
        driver.find_element(By.LINK_TEXT, element.PIM).click() #klik PIM menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,element.employee_list).click() #klik Employee list
        time.sleep(1)
        driver.find_element(By.XPATH, element.select_job_title).click() #klik Select job title
        time.sleep(3)
        driver.find_element(By.XPATH, element.select_chief_executive_officer).click() #klik job title
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, element.search_button)
        time.sleep(2)

        
        employee_jobtitle = driver.find_element(By.XPATH, element.employee_list_table).text
        self.assertIn("Job Title", employee_jobtitle)


    # Test HRM05 (Success search employee list by sub menu)
    def test_HRM_05(self):
        # Login
        driver = self.driver #buka web browser
        basicLogin.valid_login(driver)

        #PIM Menu
        driver.find_element(By.LINK_TEXT, element.PIM).click() #klik PIM menu
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,element.employee_list).click() #klik Employee list
        time.sleep(1)
        driver.find_element(By.XPATH, element.select_sub_unit).click() #klik Select Sub Unit
        time.sleep(2)
        driver.find_element(By.XPATH, element.select_OrangeHRM).click() #klik OrangeHRM
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, element.search_button).click() # klik search button
        time.sleep(3)


        employee_subunit = driver.find_element(By.XPATH, element.employee_sub_unit_table).text
        self.assertIn("Sub Unit", employee_subunit)

    def tearDown(self):
        self.driver.close()
    
        

if __name__ == "__main__":
    unittest.main()
