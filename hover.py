from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()

driver.get("https://opensource-demadmo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

admin = driver.find_element(By.XPATH,"//span[text()='Admin']")
user_management = driver.find_element(By.XPATH,"//span[text()='User Management']")
users = driver.find_element(By.XPATH,"//a[text()='Users']")

actions = ActionChains(driver)

actions.move_to_element(admin)\
       .move_to_element(user_management)\
       .move_to_element(users)\
       .click()\
       .perform()
#move_to_element -hower
#perform - to perform action