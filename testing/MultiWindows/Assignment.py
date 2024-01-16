from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service('/usr/local/bin/geckodriver')  # seleniumManager
driver = webdriver.Firefox(service=serviceObj)
action = ActionChains(driver)

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/documents-request")
email = driver.find_element(By.CSS_SELECTOR, "p a").text

driver.get("https://rahulshettyacademy.com/loginpagePractise")
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("MyPass123!")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()

alert_locator = ".alert-danger"
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, alert_locator)))

alert = driver.find_element(By.CSS_SELECTOR, alert_locator)
alert_text = alert.text
print(alert_text)
# //div[@class="alert alert-danger col-md-12"]
driver.close()