from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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

driver.get("https://opensupplyhub.org/")
driver.maximize_window()

print(driver.title)  # get title of the page
print(driver.current_url)  # get current url

driver.get("https://lun.ua/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()

driver.close()