from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

input1 = driver.find_element(
    By.XPATH,
    "//input[@id='input1']"
)
time.sleep(4)
input1.send_keys("Welcome to Selenium")

act = ActionChains(driver)
time.sleep(2)
# CTRL + A
act.key_down(Keys.CONTROL)\
   .send_keys('a')\
   .key_up(Keys.CONTROL)\
   .perform()
time.sleep(1)
# CTRL + C
act.key_down(Keys.CONTROL)\
   .send_keys('c')\
   .key_up(Keys.CONTROL)\
   .perform()
time.sleep(1)
# TAB
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.TAB).perform()

time.sleep(1)
# CTRL + V
act.key_down(Keys.CONTROL)\
   .send_keys('v')\
   .key_up(Keys.CONTROL)\
   .perform()
time.sleep(1)