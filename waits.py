from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

driver = uc.Chrome()

driver.get("https://google.com")
driver.implicitly_wait(10)
#continues immediately when element appears
search = driver.find_element(By.NAME, "q")

search.send_keys("Selenium")

search.submit()

time.sleep(5)

driver.quit()