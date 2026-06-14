"""
<div>
    <table>
        <tr>
            <td>
                <a>India Tourism Dev.</a>
            </td>
            <td>375.30</td>
            <td>3.55</td>
        </tr>
    </table>
</div>

self axis:
from selenium.webdriver.common.by import By
text = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'India Tourism')]/self::a"
).text
print(text)

parent axis
//a[contains(text(),'India Tourism')]/parent::td
ancestors axis
//a[contains(text(),'India Tourism')]/ancestor::tr

child axis
//tr/child::td

all children
//tr/descendant::*


Following axis
<tr>Self</tr>
<tr>Following 1</tr>
<tr>Following 2</tr>

following = driver.find_elements(
    By.XPATH,
    "//tr/following::tr"
)
print(len(following))


Following-sibling
<tr>
</tr>

<tr>Sibling 1</tr>
<tr>Sibling 2</tr>

//tr/following-sibling::tr
following gets all nodes below
and following sibling gets all on same-level


preceding axis
//tr/preceding::tr
preceding sibling
//tr/preceding-sibling::tr
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get(
    "https://testautomationpractice.blogspot.com/?utm_source=chatgpt.com"
)

driver.maximize_window()

days = driver.find_elements(
    By.XPATH,
    "//label[normalize-space()='Saturday']/parent::div/preceding-sibling::div"
)

for day in days:
    print(day.text)

time.sleep(5)