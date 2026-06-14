from selenium import webdriver
import undetected_chromedriver as uc
import time

driver = uc.Chrome()

driver.get("https://demo.nopcommerce.com/")
time.sleep(15)
print("Title:", driver.title)
print("URL:", driver.current_url)

print(driver.page_source[:300])

driver.quit()