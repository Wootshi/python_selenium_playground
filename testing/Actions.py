from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service('/usr/local/bin/chromedriver')  # seleniumManager
driver = webdriver.Chrome(service=serviceObj)
action = ActionChains(driver)
driver.maximize_window()

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/AutomationPractice")

# seems to be a bit flaky, but useful stuff nevertheless
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.ID, "Reload")).click()


