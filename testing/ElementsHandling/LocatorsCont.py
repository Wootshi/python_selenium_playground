from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serviceObj = Service('/usr/local/bin/chromedriver')  # seleniumManager
driver = webdriver.Chrome(service=serviceObj)

# viable locators are:
# ID, Xpath, CSS, ClassName, name, linkText, etc. goto by.py for more info
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)

# css with id
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
# css with classname
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
assertionText = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
print(assertionText)
assert "Success" in assertionText
#xpath with index
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("bruh")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

#dropdowns
gender_dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
gender_dropdown.select_by_index(1)
gender_dropdown.select_by_visible_text("Male")


driver.implicitly_wait(30)