"""
<select>
    <option>India</option>
    <option>USA</option>
</select>
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get(
    "https://testautomationpractice.blogspot.com/"
)

dropdown = driver.find_element(
    By.ID,
    "country"
)

drp = Select(dropdown)
drp.select_by_visible_text("India")
driver.quit()