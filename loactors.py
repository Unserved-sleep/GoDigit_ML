import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
driver = uc.Chrome()
driver.get("https://www.inmotionhosting.com/")
driver.maximize_window()
time.sleep(10)

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))