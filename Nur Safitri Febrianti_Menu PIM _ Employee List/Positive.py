import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from page import element
from data import inputan
import baseLogin



class TestPIMEmployeeList(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.Username = "Admin"
        self.password = "admin123"

    # Test HRM01 (Success search employee list by employee name)
    def test_HRM_01(self):
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
        driver.find_element(By.XPATH, element.search_employee_by_name).send_keys("Garry") #masukkan nama employee
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, element.search_button).click() # klik search button
        time.sleep(2)

        response_data= driver.find_element(By.LINK_TEXT,element.employee_list).text
        self.assertEqual(response_data,inputan.employee_list)
    
    # Test HRM02 (Success search employee list by employee id)
    def test_HRM_02(self):
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
        driver.find_element(By.CSS_SELECTOR, element.search_employee_by_Id).send_keys("0099") #masukkan employee id
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, element.search_button).click() # klik search button
        time.sleep(2)

        response = driver.find_element(By.LINK_TEXT,element.employee_list).text
        self.assertEqual(response,inputan.employee_list)
    
    # Test HRM03 (Success search employee list by employment status)
    def test_HRM_03(self):
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
        driver.find_element(By.XPATH, element.select_employment_status).click()
        time.sleep(3)
        driver.find_element(By.XPATH, element.select_full_time_contract).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, element.search_button).click() # klik search button
        time.sleep(3)

        employment_status = driver.find_element(By.XPATH, element.employee_information_table).text
        self.assertIn("Full-Time Contract", employment_status)

    # Test HRM04 (Success search employee list by job title)
    def test_HRM_04(self):
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
        driver.find_element(By.XPATH, element.select_employee_job_title).click() #klik Select button
        time.sleep(3)
        driver.find_element(By.XPATH, element.select_account_assistant).click() #klik job title
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, element.search_button).click() # klik search button
        time.sleep(3)

        employee_jobtitle = driver.find_element(By.XPATH, element.employee_list_table).text
        self.assertIn("Job Title", employee_jobtitle)
    
    
    # Test HRM05 (Success search employee list by sub menu)
    def test_HRM_05(self):
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
        driver.find_element(By.XPATH, element.select_sub_unit).click() #klik Select Sub Unit
        time.sleep(2)
        driver.find_element(By.XPATH, element.select_OrangeHRM).click() #klik OrangeHRM
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, element.search_button).click() # klik search button
        time.sleep(3)


        employee_subunit = driver.find_element(By.XPATH, element.employee_sub_unit_table ).text
        self.assertIn("Sub Unit", employee_subunit)
    
    # Test HRM06 (success input data and reset data)
    def test_HRM_06(self):
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
        driver.find_element(By.XPATH, element.search_employee_by_name).send_keys("Admin") #masukkan employee name
        time.sleep(1)
        driver.find_element(By.XPATH, element.reset_button) #klik Reset button

        validate = driver.find_element(By.XPATH, element.reset_employee_name).get_attribute("value")
        self.assertIn('', validate)


    def tearDown(self):
        self.driver.close()
        
        

if __name__ == "__main__":
    unittest.main()
    