import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem
from page import link
from data import inputan

def positive_login(driver):
    driver.get(link.base_url) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.username).send_keys(inputan.username) #isi email
    time.sleep(1)
    driver.find_element(By.NAME, elem.password).send_keys(inputan.password) #isi password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.btn_login).click()
    time.sleep(3)

def negative_login_upcase_usn(driver):
    driver.get(link.base_url) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.username).send_keys(inputan.upcase_username) #isi email
    time.sleep(1)
    driver.find_element(By.NAME, elem.password).send_keys(inputan.password) #isi password salah
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.btn_login).click()
    time.sleep(3)

def negative_login_wrong_usn(driver):
    driver.get(link.base_url) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.username).send_keys(inputan.wrong_username) #isi email
    time.sleep(1)
    driver.find_element(By.NAME, elem.password).send_keys(inputan.password) #isi password salah
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.btn_login).click()
    time.sleep(3)

def negative_login_wrong_pw(driver):
    driver.get(link.base_url) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.username).send_keys(inputan.username) #isi email
    time.sleep(1)
    driver.find_element(By.NAME, elem.password).send_keys(inputan.wrong_password) #isi password salah
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.btn_login).click()
    time.sleep(3)

def negative_login_blank_all(driver):
    driver.get(link.base_url) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.username).send_keys("") #isi email
    time.sleep(1)
    driver.find_element(By.NAME, elem.password).send_keys("") #isi password salah
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.btn_login).click()
    time.sleep(3)

def negative_login_blank_usn(driver):
    driver.get(link.base_url) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.username).send_keys("") #isi email
    time.sleep(1)
    driver.find_element(By.NAME, elem.password).send_keys(inputan.password) #isi password salah
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.btn_login).click()
    time.sleep(3)

def negative_login_blank_pw(driver):
    driver.get(link.base_url) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.username).send_keys(inputan.username) #isi email
    time.sleep(1)
    driver.find_element(By.NAME, elem.password).send_keys("") #isi password salah
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.btn_login).click()
    time.sleep(3)