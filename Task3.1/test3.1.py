from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
import random

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(2)

driver.find_element(By.ID, "gender-male").click()
time.sleep(2)


driver.find_element(By.ID, "gender-male").click()
time.sleep(2)

driver.find_element(By.ID, "FirstName").send_keys("Elon")
time.sleep(1)
driver.find_element(By.ID, "LastName").send_keys("Musk")
time.sleep(1)
driver.find_element(By.ID, "Email").send_keys("ElonMusk@ColdMail.Com")
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys("coldmail44")
time.sleep(1)
driver.find_element(By.ID, "ConfirmPassword").send_keys("coldmail44")
time.sleep(2)

driver.find_element(By.ID, "register-button").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input.button-1.register-continue-button").click()
time.sleep(15)