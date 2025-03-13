from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

mail = "hopefully@mail.com"

with open("data1.txt", "r") as file1:
    lines1 = [line1.strip() for line1 in file1]

with open("data2.txt", "r") as file2:
    lines2 = [line2.strip() for line2 in file2] 

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)


driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(2)

driver.find_element(By.ID, "gender-male").click()
time.sleep(2)


driver.find_element(By.ID, "gender-male").click()
time.sleep(2)

driver.find_element(By.ID, "FirstName").send_keys("Melon")
time.sleep(1)
driver.find_element(By.ID, "LastName").send_keys("Musk")
time.sleep(1)
driver.find_element(By.ID, "Email").send_keys(mail)
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys("coldmail44")
time.sleep(1)
driver.find_element(By.ID, "ConfirmPassword").send_keys("coldmail44")
time.sleep(2)

driver.find_element(By.ID, "register-button").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input.button-1.register-continue-button").click()
time.sleep(2)

driver.quit()

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(2)

driver.find_element(By.ID, "Email").send_keys(mail)
time.sleep(2)

driver.find_element(By.ID, "Password").send_keys("coldmail44")
time.sleep(2)

driver.find_element("xpath", "//input[@type='submit' and @value='Log in']").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Digital downloads").click()
time.sleep(2)

print("Processing items...")

i = 0

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
        print(f"Error adding {line1}")

driver.find_element(By.LINK_TEXT, "Shopping cart").click()
time.sleep(2)

driver.find_element(By.ID, "termsofservice").click()
time.sleep(2)

driver.find_element(By.ID, "checkout").click()
time.sleep(2)

try:
    dropdown = Select(driver.find_element(By.ID, "BillingNewAddress_CountryId"))
    dropdown.select_by_visible_text("Uzbekistan")
    time.sleep(2)

    city_input = driver.find_element(By.ID, "BillingNewAddress_City")
    if not city_input.get_attribute('value'): 
        city_input.send_keys("Tashkent")
        time.sleep(2)

    address_input = driver.find_element(By.ID, "BillingNewAddress_Address1")
    if not address_input.get_attribute('value'):
        address_input.send_keys("Random street...")
        time.sleep(2)

    zip_input = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
    if not zip_input.get_attribute('value'): 
        zip_input.send_keys("21244")
        time.sleep(2)

    phone_input = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
    if not phone_input.get_attribute('value'): 
        phone_input.send_keys("+000 00 000 00")
        time.sleep(2)

except Exception as e:
    print(f"")

time.sleep(5)

driver.find_element(By.CLASS_NAME, "button-1.new-address-next-step-button").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[contains(@class, 'payment-method-next-step-button') and @value='Continue']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[contains(@class, 'payment-info-next-step-button') and @value='Continue']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[contains(@class, 'confirm-order-next-step-button') and @value='Confirm']").click()
time.sleep(2)

try:
    message = driver.find_element(By.XPATH, "//div[@class='section order-completed']//div[@class='title']/strong").text
    print(message)
except Exception as ex:
    print(f"The checkout was unsuccessful")

driver.quit()

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(2)

driver.find_element(By.ID, "Email").send_keys(mail)
time.sleep(2)

driver.find_element(By.ID, "Password").send_keys("coldmail44")
time.sleep(2)

driver.find_element("xpath", "//input[@type='submit' and @value='Log in']").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Digital downloads").click()
time.sleep(2)

print("Processing items...")

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
        print(f"Error adding {line2}")

driver.find_element(By.LINK_TEXT, "Shopping cart").click()
time.sleep(2)

driver.find_element(By.ID, "termsofservice").click()
time.sleep(2)

driver.find_element(By.ID, "checkout").click()
time.sleep(2)

try:
    dropdown = Select(driver.find_element(By.ID, "BillingNewAddress_CountryId"))
    dropdown.select_by_visible_text("Uzbekistan")
    time.sleep(2)

    city_input = driver.find_element(By.ID, "BillingNewAddress_City")
    if not city_input.get_attribute('value'): 
        city_input.send_keys("Tashkent")
        time.sleep(2)

    address_input = driver.find_element(By.ID, "BillingNewAddress_Address1")
    if not address_input.get_attribute('value'):
        address_input.send_keys("Random street...")
        time.sleep(2)

    zip_input = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
    if not zip_input.get_attribute('value'): 
        zip_input.send_keys("21244")
        time.sleep(2)

    phone_input = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
    if not phone_input.get_attribute('value'): 
        phone_input.send_keys("+000 00 000 00")
        time.sleep(2)

except Exception as e:
    print(f"")

time.sleep(5)

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

try:
    message = driver.find_element(By.XPATH, "//div[@class='section order-completed']//div[@class='title']/strong").text
    print(message)
except Exception as ex:
    print(f"The checkout was unsuccessful")


time.sleep(10)

driver.find_element(By.XPATH, "//input[@class='button-2 order-completed-continue-button' and @value='Continue']").click()

time.sleep(2)

driver.quit()