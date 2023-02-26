import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from script import element
from info import data

def valid_login(driver):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.NAME, element.username).send_keys(data.username) #isi username
    time.sleep(1)
    driver.find_element(By.NAME, element.password).send_keys(data.password) #isi password
    time.sleep(1)    
    driver.find_element(By.CLASS_NAME, element.login_btn).click() #klik login
    time.sleep(1)
    