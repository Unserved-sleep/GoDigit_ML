# driver.find_element(
#     By.XPATH,
#     "//input[@id='datepicker']"
# ).send_keys("05/30/2022")    normal date picker

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

expected_year = "2027"
expected_month = "June"
expected_date = "15"

driver.find_element(By.ID, "datepicker").click()

while True:
    current_month = driver.find_element(
        By.CLASS_NAME,
        "ui-datepicker-month"
    ).text

    current_year = driver.find_element(
        By.CLASS_NAME,
        "ui-datepicker-year"
    ).text

    print(f"Current: {current_month} {current_year}")

    if current_month == expected_month and \
       current_year == expected_year:
        break

    else:
        driver.find_element(
            By.XPATH,
            "//span[text()='Next']"
        ).click()


dates = driver.find_elements(
    By.XPATH,
    "//table[@class='ui-datepicker-calendar']//td/a"
)

for date in dates:
    if date.text == expected_date:
        date.click()
        break

time.sleep(5)
driver.quit()
