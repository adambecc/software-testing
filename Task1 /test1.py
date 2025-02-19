from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()

#abre la pagina
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

#selecciona el apartado de giftcards
driver.find_element(By.CSS_SELECTOR, "a[href='/gift-cards']").click()
time.sleep(2)

#filtrar el precio > 99
products = driver.find_elements(By.CSS_SELECTOR, ".product-grid .item-box")
for product in products:
        price_text = product.find_element(By.CLASS_NAME, "price").text.replace("$", "")
        if float(price_text) > 99:
            product.find_element(By.TAG_NAME, "a").click()
            time.sleep(2)

driver.find_element(By.ID, "giftcard_4_RecipientName").send_keys("Elon Musk")
time.sleep(1)
driver.find_element(By.ID, "giftcard_4_SenderName").send_keys("Adam Becc")
time.sleep(1)
driver.find_element(By.ID, "addtocart_4_EnteredQuantity").clear()
driver.find_element(By.ID, "addtocart_4_EnteredQuantity").send_keys(5000)
time.sleep(1)

driver.find_element(By.ID, "add-to-cart-button-4").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-wishlist-button-4").click()
time.sleep(1)

#driver.find_element(By.CSS_SELECTOR, "a[href='/jewelry']").click()
driver.find_element(By.LINK_TEXT, "JEWELRY").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT, "Create Your Own Jewelry").click()
time.sleep(1)

material = Select(driver.find_element(By.ID, "product_attribute_71_9_15"))
time.sleep(1)
material.select_by_visible_text("Silver (1 mm)")
time.sleep(1)

driver.find_element(By.ID, "product_attribute_71_10_16").send_keys("80")
time.sleep(1)

driver.find_element(By.ID, "product_attribute_71_11_17_50").click()
time.sleep(1)

driver.find_element(By.ID, "addtocart_71_EnteredQuantity").clear()
time.sleep(1)

driver.find_element(By.ID, "addtocart_71_EnteredQuantity").send_keys(26)
time.sleep(1)

driver.find_element(By.ID, "add-to-cart-button-71").click()
time.sleep(1)

driver.find_element(By.ID, "add-to-wishlist-button-71").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT, "Wishlist").click()
time.sleep(1)

checkboxes = driver.find_elements(By.CLASS_NAME, "add-to-cart")
for checkbox in checkboxes:
    checkbox.click()

driver.find_element(By.NAME, "addtocartbutton").click()
time.sleep(2)

sub_total = driver.find_element(By.CSS_SELECTOR, ".cart-total .product-price").text.replace("$", "")
assert float(sub_total) == 1002600.00, f"Subtotal mismatch: {sub_total}"
print("Automated Test Passed: Subtotal is correct!")
time.sleep(15)

driver.quit()
