from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service('/usr/local/bin/chromedriver')  # seleniumManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(service=serviceObj, options=chrome_options)

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
# taking screenshots manually
driver.get_screenshot_as_file("test.png")
