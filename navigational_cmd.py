import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

"""
driver.back()
driver.forward()
driver.refresh()
"""

driver.get("https://www.amazon.in")

driver.get("https://www.flipkart.com")

driver.back()

driver.forward()

driver.refresh()


#Browser Commands
# .close(), .quit()

"""
button = driver.find_element(By.TAG_NAME, "button")
print(button.text)
print(label.text)

<input value="admin@yourstore.com">
email = driver.find_element(By.ID, "Email")
print(email.get_attribute("value"))
"""