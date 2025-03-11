from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

with open("data1.txt", "r") as file1:
    lines1 = [line1.strip() for line1 in file1]

with open("data2.txt", "r") as file2:
    lines2 = [line2.strip() for line2 in file2] 


driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

time.sleep(2)

driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(2)

driver.find_element(By.ID, "Email").send_keys("ElonMusk@ColdMail.Com")
time.sleep(2)

driver.find_element(By.ID, "Password").send_keys("coldmail44")
time.sleep(2)

driver.find_element("xpath", "//input[@type='submit' and @value='Log in']").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Digital downloads").click()
time.sleep(2)

print("Processing items...")

i = 0

#process each item from file1
for line1 in lines1:
    try:
        i += 1

        driver.find_element(By.LINK_TEXT, line1).click()
        time.sleep(2)

        driver.find_element(By.CLASS_NAME, "button-1.add-to-cart-button").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Digital downloads").click()
        time.sleep(2)

        print(f"{i}. {line1} was successfully added to the cart.")
        
    except Exception as e:
        print(f"Error adding {line1}: {str(e)}")

#process each item from file 2
for line2 in lines2:
    try:
        i += 1

        driver.find_element(By.LINK_TEXT, line2).click()
        time.sleep(2)

        driver.find_element(By.CLASS_NAME, "button-1.add-to-cart-button").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Digital downloads").click()
        time.sleep(2)

        print(f"{i}. {line2} was successfully added to the cart.")
        
    except Exception as e:
        print(f"Error adding {line2}: {str(e)}")

driver.find_element(By.LINK_TEXT, "Shopping cart").click()
time.sleep(2)

driver.find_element(By.ID, "termsofservice").click()
time.sleep(2)


driver.find_element(By.ID, "checkout").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "button-1.new-address-next-step-button").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[contains(@class, 'payment-method-next-step-button') and @value='Continue']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[contains(@class, 'payment-info-next-step-button') and @value='Continue']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[contains(@class, 'confirm-order-next-step-button') and @value='Confirm']").click()
time.sleep(2)

print("Verifying order confirmation...")

time.sleep(10)

message = driver.find_element(By.XPATH, "//div[@class='section order-completed']//div[@class='title']/strong").text
print(message)

time.sleep(10)

driver.find_element(By.XPATH, "//input[@class='button-2 order-completed-continue-button' and @value='Continue']").click()

time.sleep(2)

driver.quit()