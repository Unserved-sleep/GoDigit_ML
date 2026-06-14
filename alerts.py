"""
alert = driver.switch_to.alert

print(myalert.text)
alert.send_keys("Welcome")  --prompt has input boxes
alert.accept()  -- click ok button
alert.dismiss()  -- cancel
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(
    By.XPATH,
    "//button[text()='Prompt Alert']"
).click()

alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Welcome")
alert.accept()