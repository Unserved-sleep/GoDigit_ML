from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)

spans = driver.find_elements(By.XPATH, "(//div[@class='_Zmx1a_fluidQuadImageLabelBody_3tld0'])[1]//span")

for span in spans[:2]:
     print(span.text)
print(len(spans))
