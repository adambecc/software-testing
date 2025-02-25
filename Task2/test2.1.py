from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
time.sleep(2)

try:
    cookie_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, "close-fixedban"))
    )
    cookie_button.click()
    print("Cookie window closed")
except:
    print("No cookie window ")

widgets_card = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']"))
)
widgets_card.click()

progress_bar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Progress Bar']"))
)
progress_bar.click()

start_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "startStopButton"))
)
start_button.click()

reset_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "resetButton"))
)
reset_button.click()

WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.CLASS_NAME, "progress-bar").text == "0%"
)

percentage = driver.find_element(By.CLASS_NAME, "progress-bar").text

time.sleep(2)

if percentage == "0%":
    print("Successful reset")
else:
    print(f"Error: Progress bar shows {percentage}")

time.sleep(2)
driver.quit()