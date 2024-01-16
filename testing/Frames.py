from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service('/usr/local/bin/chromedriver')  # seleniumManager
driver = webdriver.Chrome(service=serviceObj)

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/iframe")

# w/o switching to frame, following code won't work.
# Frame is like a page within a page, embedded
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Test check check")
# switching back to default page
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
