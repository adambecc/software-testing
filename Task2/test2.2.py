from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
import random

first_names = ["Elon", "Mark", "Albert", "Ryan", "Bill", "Steve", "Justin", "Michael", "Keanu", "Marie"]
last_names = ["Musk", "Zuckerberg", "Einstein", "Montgomery", "Gates", "Jobs", "Bieber", "Jordan", "Reeves", "Curie"]

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
time.sleep(1)
driver.maximize_window()

try:
    cookie_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, "close-fixedban"))
    )
    cookie_button.click()
    print("Cookie window closed")
except:
    print("No cookie window ")

elements_card = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
)
elements_card.click()

web_tables = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']"))
)
web_tables.click()

time.sleep(3)

i = 0
j = 20

rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
count = 0
for row in rows:
    cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")
    cell_texts = [cell.text.strip() for cell in cells]
    if any(cell_texts):
        count += 1
        #print(f"Row {count} contents: {cell_texts}")

k=count

row_wrap_element = driver.find_element(By.CSS_SELECTOR, ".select-wrap select")
row_wrap = int(row_wrap_element.get_attribute("value"))

for _ in range(row_wrap - count + 1):
    add_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "addNewRecordButton"))
    )
    add_button.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )

    name = random.choice(first_names)

    driver.find_element(By.ID, "firstName").send_keys(f"{name}")
    driver.find_element(By.ID, "lastName").send_keys(f"{random.choice(last_names)}")
    driver.find_element(By.ID, "userEmail").send_keys(f"{name.lower()}_st{i}@vu.lt")
    driver.find_element(By.ID, "age").send_keys(f"2{i}")
    driver.find_element(By.ID, "salary").send_keys(f"{j}{i}00")
    driver.find_element(By.ID, "department").send_keys("Software Testing")

    driver.find_element(By.ID, "submit").click()

    i += 1
    j -= 1
    k += 1

    time.sleep(1)

time.sleep(1)

next = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "-next"))
)
next.click()

time.sleep(2)

delete = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, f"delete-record-{k}"))
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

driver.quit()