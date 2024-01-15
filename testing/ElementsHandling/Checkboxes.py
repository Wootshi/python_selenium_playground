from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome driver. Need to initiate Service() separately.
# Downloads chromedriver automatically if its not specified,
# does some more stuff as well
# serviceObj = Service('/usr/local/bin/chromedriver')  # seleniumManager
# driver = webdriver.Chrome(service=serviceObj)

# Firefox driver. Same logic
# serviceObj = Service('/usr/local/bin/geckodriver')  # seleniumManager
# driver = webdriver.Firefox(service=serviceObj)

serviceObj = Service('/usr/local/bin/msedgedriver')  # seleniumManager
driver = webdriver.Edge(service=serviceObj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
# not really an optimal way,
# but shows how you can gather elements in list,
# iterate and find something you're interested in
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

checkboxes = driver.find_element(By.CSS_SELECTOR, "input[value='radio3']")
checkboxes.click()
# is_selected() in action
assert checkboxes.is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
#negative assertion
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
