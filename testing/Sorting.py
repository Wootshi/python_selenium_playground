from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service('/usr/local/bin/chromedriver')  # seleniumManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")  # option argument for driver
driver = webdriver.Chrome(service=serviceObj)

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

browser_sorted_veggies = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggie_web_elements = driver.find_elements(By.XPATH, "//tr/td[1]")

for e in veggie_web_elements:
    browser_sorted_veggies.append(e.text)

# gotta copy the list so both vars point to actual different lists
original_list = browser_sorted_veggies.copy()

# sorting the list
browser_sorted_veggies.sort()
print(browser_sorted_veggies)
print(original_list)

assert browser_sorted_veggies == original_list
