import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from element import elem
from data import addData

# Test Case Menu Admin - Organization - Locations


class TestAOL(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # variable data
        self.url = "https://opensource-demo.orangehrmlive.com/"

    def tearDown(self):
        self.browser.quit()

    # TC001-Admin has successfully added a new location
    def test_success_add_a_new_location(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys(addData.name)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        ####
        # DROPDOWN COUNTRY
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        ####
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')

    # TC002-Admin failed to add new location
    def test_failed_to_add_new_location(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        ####
        # DROPDOWN COUNTRY
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        ####
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)
        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]").text
        self.assertIn(response_data, 'Add Location')

    # TC003-Cancel button save click when adding new location
    def test_cancel_save_when_adding_new_location(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys(addData.name)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        ####
        # DROPDOWN COUNTRY
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        ####
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)
        # Button Cancel
        driver.find_element(
            By.XPATH, elem.btnCancel).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')

    # TC004-Search for location
    def test_search_for_location(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(addData.name)
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text
        self.assertIn(response_data, '(1) Record Found')

    # TC005-Cancel button click when editing location
    def test_cancel_button_click_when_editing_location(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(addData.name)
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)
        # Button Edit
        driver.find_element(By.XPATH, elem.btnEdit).click()
        time.sleep(5)
        # Button Cancel
        driver.find_element(By.XPATH, elem.btnCancel).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')

    # TC006-Edit Location
    def test_edit_location(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(addData.name)
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)
        # Button Edit
        driver.find_element(By.XPATH, elem.btnEdit).click()
        time.sleep(3)
        # Edit Data
        cityEdit = driver.find_element(By.XPATH, elem.cityEdit)
        cityEdit.send_keys(Keys.CONTROL + "a")
        cityEdit.send_keys(Keys.BACKSPACE)
        cityEdit.send_keys("Jakarta")
        time.sleep(2)
        addressEdit = driver.find_element(By.XPATH, elem.addressEdit)
        addressEdit.send_keys(Keys.CONTROL + "a")
        addressEdit.send_keys(Keys.BACKSPACE)
        addressEdit.send_keys("Jakarta, tanggerang, jabodetabek")
        time.sleep(2)
        stateEdit = driver.find_element(By.XPATH, elem.stateEdit)
        stateEdit.send_keys(Keys.CONTROL + "a")
        stateEdit.send_keys(Keys.BACKSPACE)
        stateEdit.send_keys("Banyumas Indah")
        time.sleep(2)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSaveEdit).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')

    # TC007-Delete location
    def test_delete_location(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(addData.name)
        time.sleep(1)
        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)
        # Button Delete
        driver.find_element(By.XPATH, elem.btnDelete).click()
        time.sleep(5)
        # konfirmasi delete
        driver.find_element(By.XPATH, elem.confirmDelete).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')

    # TC008-Add location failed due to invalid input
    def test_add_location_failed_due_to_invalid_input(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys(addData.name)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        # Test Negative Input string for type Integer only
        driver.find_element(By.XPATH, elem.fax).send_keys("asdaA2@321")
        time.sleep(1)
        ####
        # DROPDOWN COUNTRY
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        ####
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)
        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]").text
        self.assertIn(response_data, 'Add Location')

    # TC009-Edit location failed due to missing required fields
    def test_location_failed_due_to_missing_required_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(addData.name)
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)
        # Button Edit
        driver.find_element(By.XPATH, elem.btnEdit).click()
        time.sleep(3)
        # Edit Data
        nameEdit = driver.find_element(By.XPATH, elem.nameEdit)
        nameEdit.send_keys(Keys.CONTROL + "a")
        nameEdit.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        addressEdit = driver.find_element(By.XPATH, elem.addressEdit)
        addressEdit.send_keys(Keys.CONTROL + "a")
        addressEdit.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        stateEdit = driver.find_element(By.XPATH, elem.stateEdit)
        stateEdit.send_keys(Keys.CONTROL + "a")
        stateEdit.send_keys(Keys.BACKSPACE)
        time.sleep(2)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSaveEdit).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]").text
        self.assertIn(response_data, 'Edit Location')

    # TC0010-Search location failed due to invalid keyword
    def test_Search_location_failed_due_to_invalid_keyword(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys("qwertyuiop")
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text
        self.assertIn(response_data, 'No Records Found')


if __name__ == "__main__":
    unittest.main()
