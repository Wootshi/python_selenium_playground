from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service('/usr/local/bin/geckodriver')  # seleniumManager
driver = webdriver.Firefox(service=serviceObj)
action = ActionChains(driver)

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
# getting the window_handles property. Creates a list with windows objects
windows_opened = driver.window_handles

driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

# closing newly opened window
driver.close()

driver.switch_to.window(windows_opened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text




