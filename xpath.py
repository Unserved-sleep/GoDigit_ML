"""
<input id="email" name="email" type="text">
//input[@id='email']


DOM
<html>
    <body>
        <div>
            <input id="email">
        </div>
    </body>
</html>
absolute xpath  /html/body/div/form/input

driver.find_element(By.XPATH,"/html/body/div[1]/form/input")

relative xpath  //input[@id='email']   use //

multi-attribute //input[@id='email' and @type='text']

contains function
//input[contains(@id,'email')]
starts-with
//input[starts-with(@id,'email')]

based on visible names
<button>Login</button>
//button[text()='Login']
//button[normalize-space()='Login']    handles spaces


and / or
//input[@id='email' and @type='text']
//input[@id='email' or @name='username']
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(5)
search = driver.find_element(
    By.XPATH,
    "//textarea[@name='q']"
)

search.send_keys("XPath Tutorial")
time.sleep(5)
driver.quit()