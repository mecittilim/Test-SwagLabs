from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from constants import *
driver = webdriver.Chrome()
driver.maximize_window()

def test_fail_login():
        driver.get(BASE_DOMAIN_URL)
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_INPUT_ID )))
        usernameInput = driver.find_element(By.ID,USERNAME_INPUT_ID)
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.ID, PASSWORD_INPUT_ID )))
        passwordInput = driver.find_element(By.ID,PASSWORD_INPUT_ID)
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.ID, LOGIN_BUTTON_ID )))
        loginButton = driver.find_element(By.ID,LOGIN_BUTTON_ID)
        
        action = ActionChains(driver)
        action.send_keys_to_element(usernameInput,USERNAME)
        action.send_keys_to_element(passwordInput,PASSWORD)
        action.click(loginButton)
        action.pause(2)
        action.perform()

        sleep(2)
        productList = driver.find_element(By.XPATH,'//*[@class="inventory_item"]')
        lengthOfProducts = len(productList)
        print(lengthOfProducts)
        


test_fail_login()