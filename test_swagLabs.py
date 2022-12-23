from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from constants import *


class Test_SwagLabs:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    # test case for correctly login
    def test_login(self,):
        self.driver.get(BASE_DOMAIN_URL)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.ID, USERNAME_INPUT_ID)))
        usernameInput = self.driver.find_element(By.ID, USERNAME_INPUT_ID)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.ID, PASSWORD_INPUT_ID)))
        passwordInput = self.driver.find_element(By.ID, PASSWORD_INPUT_ID)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.ID, LOGIN_BUTTON_ID)))
        loginButton = self.driver.find_element(By.ID, LOGIN_BUTTON_ID)

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, USERNAME)
        action.send_keys_to_element(passwordInput, PASSWORD)
        action.click(loginButton)
        action.pause(2)
        action.perform()
        currentUrl = self.driver.current_url

        assert currentUrl == CURRENT_URL

    # test case for fail login with false parameters and check error message
    def test_fail_login(self):
        self.driver.get(BASE_DOMAIN_URL)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.ID, USERNAME_INPUT_ID)))
        usernameInput = self.driver.find_element(By.ID, USERNAME_INPUT_ID)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.ID, PASSWORD_INPUT_ID)))
        passwordInput = self.driver.find_element(By.ID, PASSWORD_INPUT_ID)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.ID, LOGIN_BUTTON_ID)))
        loginButton = self.driver.find_element(By.ID, LOGIN_BUTTON_ID)

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, "USERNAME")
        action.send_keys_to_element(passwordInput, "PASSWORD")
        action.click(loginButton)
        action.pause(2)
        action.perform()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ERROR_XPATH)))
        errorMessage = self.driver.find_element(By.XPATH, ERROR_XPATH)
        text = errorMessage.text

        assert text == ERROR_MESSAGE

    # test case to check that total product equals 6
    def test_total_inventory(self):
        self.test_login()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, INVENTORY_ITEM)))
        productList = self.driver.find_elements(By.CLASS_NAME, INVENTORY_ITEM)
        totalProd = len(productList)

        assert totalProd == 6

    def test_add_button(self):
        self.test_login()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, INVENTORY_ITEM)))
        addButton = self.driver.find_element(By.ID, ADD_BUTTON_ID)

        action = ActionChains(self.driver)
        action.click(addButton)
        action.pause(3)
        action.perform()

        removeButton = self.driver.find_element(By.ID, REMOVE_BUTTON_ID)
        removeButtonText = removeButton.text

        assert removeButtonText == REMOVE_BUTTON_TEXT

    def test_basket_count(self):
        self.test_login()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, INVENTORY_ITEM)))
        addButton = self.driver.find_element(By.ID, ADD_BUTTON_ID)

        action = ActionChains(self.driver)
        action.click(addButton)
        action.pause(3)
        action.perform()

        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,BASKET)))
        basketBadge = self.driver.find_element(By.CLASS_NAME,BASKET)
        text = basketBadge.text

        assert text == "1"

    