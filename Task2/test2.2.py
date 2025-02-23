from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
time.sleep(1)
driver.maximize_window()

elements_card = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
)
elements_card.click()

web_tables = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']"))
)
web_tables.click()

for _ in range(8):
    add_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "addNewRecordButton"))
    )
    add_button.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )

    driver.find_element(By.ID, "firstName").send_keys("Adam")
    driver.find_element(By.ID, "lastName").send_keys("Becc")
    driver.find_element(By.ID, "userEmail").send_keys("testing@vu.lt")
    driver.find_element(By.ID, "age").send_keys("99")
    driver.find_element(By.ID, "salary").send_keys("90000")
    driver.find_element(By.ID, "department").send_keys("Testing")

    driver.find_element(By.ID, "submit").click()

    time.sleep(1)

time.sleep(3)

next = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "-next"))
)
next.click()

time.sleep(2)

delete = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "delete-record-11"))
)
delete.click()

previous = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "-previous"))
)
previous.click()

time.sleep(5)

num_of_pages = driver.find_element(By.CLASS_NAME, "-totalPages").text

if num_of_pages == "1":
    print("Successful")
else:
    print(f"Error")

time.sleep (5)

time.sleep(3)
driver.quit()