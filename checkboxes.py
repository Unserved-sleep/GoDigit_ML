from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

checkboxes = driver.find_elements(
    By.XPATH,
    "//input[@type='checkbox' and contains(@id,'day')]"
)
for checkbox in checkboxes:
    checkbox.click()

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

driver.find_element(
    By.LINK_TEXT,
    "Digital downloads"
).click()
# By.PARTIAL_LINK_TEXT,
#     "Digital"