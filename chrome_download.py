import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

download_path = os.getcwd()

prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)

service = Service(r"E:\drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(
    service=service,
    options=options
)

driver.maximize_window()

driver.get(
    "https://file-examples.com/index.php/sample-documents-download/"
)

driver.find_element(
    By.XPATH,
    "(//a[contains(text(),'Download sample DOC file')])[1]"
).click()

time.sleep(10)

driver.quit()

print("Download completed.")
print("Downloaded to:", download_path)