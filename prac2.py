from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://topheroes.store.kopglobal.com/en")
driver.maximize_window()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.find_element(By.XPATH,"//div[contains(@class,'h-[54px]')]").click()
driver.find_element(By.CLASS_NAME, "el-input__inner").send_keys("1496421902550")
driver.find_element(By.CLASS_NAME, "site-button").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[contains(@class, 'mt-[46px]')]").click()
time.sleep(3)
driver.refresh()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "site-input__inner").send_keys("GearGB")
driver.find_element(By.XPATH, "//div[contains(@class, 'justify-center')]//button").click()

time.sleep(100)


