from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service('/usr/local/bin/chromedriver')  # seleniumManager
driver = webdriver.Chrome(service=serviceObj)
# waits for the element to show up, 5 seconds max.
# It's global, you don't need to specify it for every case
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

sum_of_items = 0
expected_tuple = {'Cauliflower - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Cashews - 1 Kg'}
asserted_list = []

driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ca")

products = driver.find_elements(By.CSS_SELECTOR, "div.products div.product")
products_names = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")
count_products_names = len(products_names)

while count_products_names >= 30:
    products = driver.find_elements(By.CSS_SELECTOR, "div.products div.product")
    count_products_names = len(products)

print("Current products displayed:" + str(count_products_names))
wait.until(lambda driver_: count_products_names < 30)

for product in products:
    product_text = product.find_element(By.CSS_SELECTOR, "h4.product-name").text
    asserted_list.append(product_text)
    product.find_element(By.CSS_SELECTOR, "button").click()

print(expected_tuple)
print(asserted_list)
assert sorted(expected_tuple) == sorted(asserted_list)

driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait.until(expected_conditions
           .presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
success_message = driver.find_element(By.CLASS_NAME, "promoInfo").text
assert success_message == "Code applied ..!"

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
for price in prices:
    sum_of_items = sum_of_items + float(price.text)  # casting

total_amount = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
discount_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

print("Sum of items is: " + str(sum_of_items))
print("Total amount is: " + str(total_amount))
print("Total discounted amount is: " + str(discount_amount))
assert sum_of_items == total_amount
assert total_amount > discount_amount
