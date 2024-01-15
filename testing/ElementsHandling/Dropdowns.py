import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serviceObj = Service('/usr/local/bin/chromedriver')  # seleniumManager
driver = webdriver.Chrome(service=serviceObj)

# viable locators are:
# ID, Xpath, CSS, ClassName, name, linkText, etc. goto by.py for more info
driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.implicitly_wait(10)

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

countries_elements = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries_elements))  # len() gets the lenght of the list
countries = []

for country in countries_elements:
    countries.append(country.text)
for country in countries_elements:
    if country.text == "India":
        country.click()
        break

print(countries)
isIndiaPresent = "India" in countries
if not isIndiaPresent:
    print("India is not present in the list!")

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
