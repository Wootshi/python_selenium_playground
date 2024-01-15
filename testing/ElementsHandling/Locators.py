from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service('/usr/local/bin/chromedriver')  # seleniumManager
driver = webdriver.Chrome(service=serviceObj)

# viable locators are:
# ID, Xpath, CSS, ClassName, name, linkText, etc. goto by.py for more info
driver.get("https://opensupplyhub.org/auth/register")
driver.implicitly_wait(10)

driver.find_element(By.ID, "email").send_keys("heihachi@ukr.com")
driver.find_element(By.ID, "name").send_keys("Mishima Zaibatsu")
driver.find_element(By.ID, "newsletter").click()

# css selectors
driver.find_element(By.CSS_SELECTOR, "input[id='description'").send_keys("Family Business")

# xpath
driver.find_element(By.XPATH, "//input[@id='tos']").click()

# text using xpath
driver.find_element(By.XPATH, "//div[contains(text(), 'Register')]").click()
driver.implicitly_wait(10)

assertionText = driver.find_element(By.XPATH, "//ul[following-sibling::button]").text
print(assertionText)

# basic assert expression
assert "Missing required field Password" in assertionText