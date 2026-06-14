from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element(
    By.XPATH,
    "//span[text()='right click me']"
)

actions = ActionChains(driver)

actions.context_click(button).perform()
time.sleep(2)
driver.find_element(
    By.XPATH,
    "//span[text()='Copy']"
).click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)