"""
search_box = driver.find_element(By.ID, "small-searchterms")
print(search_box.is_displayed()) ---- true/false

print(search_box.is_enabled())  ----check interaction

male = driver.find_element(By.ID, "gender-male")
print(male.is_selected())   ===false
male.click()
print(male.is_selected())  ----true
"""

import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
checkbox = driver.find_element(By.ID, "sunday")
print(checkbox.is_displayed())
print(checkbox.is_enabled())
print(checkbox.is_selected())

checkbox.click()

print(checkbox.is_selected())

