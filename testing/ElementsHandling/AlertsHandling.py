from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObj = Service('/usr/local/bin/msedgedriver')  # seleniumManager
driver = webdriver.Edge(service=serviceObj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# handling browser built-in alerts

name = "Petro"

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
alert_text = alert.text

print(alert_text)
assert name in alert_text

alert.accept()
# alert.dismiss()
