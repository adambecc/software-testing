from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

old_mail = "Old4@ColdMail.Com"
new_mail = "New2@ColdMail.Com"
password = "coldmail44"

driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")

#trying to log in
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "ico-login"))).click()
time.sleep(2)

driver.find_element(By.ID, "Email").send_keys(old_mail)
driver.find_element(By.ID, "Password").send_keys(password)
driver.find_element(By.XPATH, "//input[@type='submit' and @value='Log in']").click()
time.sleep(2)

#verifying if the log in failed or not
try:
    error_message = driver.find_element(By.XPATH, "//div[@class='validation-summary-errors']").text
    print("Login failed, registering account...")
    
    #registering
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.ID, "gender-male").click()
    driver.find_element(By.ID, "FirstName").send_keys("Melon")
    driver.find_element(By.ID, "LastName").send_keys("Musk")
    driver.find_element(By.ID, "Email").send_keys(old_mail)
    driver.find_element(By.ID, "Password").send_keys(password)
    driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
    driver.find_element(By.ID, "register-button").click()
    time.sleep(2)    
    driver.find_element(By.CSS_SELECTOR, "input.button-1.register-continue-button").click()
    time.sleep(2)
    print("Account successfully registered and logged in!")
except Exception:
    print("Login successful, proceeding...")

#update the email
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "account"))).click()
time.sleep(2)

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys(new_mail)

time.sleep(2)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Save']"))).click()

time.sleep(2)

#log out
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))).click()
time.sleep(2)

#log in with the old email
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "ico-login"))).click()
time.sleep(2)

driver.find_element(By.ID, "Email").send_keys(old_mail)
driver.find_element(By.ID, "Password").send_keys(password)
driver.find_element(By.XPATH, "//input[@type='submit' and @value='Log in']").click()
time.sleep(2)

print("Trying old email...")

#old email error
try:
    error_message = driver.find_element(By.XPATH, "//div[@class='validation-summary-errors']").text
    print("Old email login failed as expected:", error_message)
except:
    print("Error: Old email worked. Changes weren't saved properly")

#log in with the new mail
print("Trying new email...")
time.sleep(2)

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys(new_mail)
driver.find_element(By.ID, "Password").send_keys(password)
driver.find_element(By.XPATH, "//input[@type='submit' and @value='Log in']").click()

time.sleep(2)
print("Changes were successful!")

driver.quit()