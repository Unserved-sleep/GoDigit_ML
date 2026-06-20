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
    "plugins.always_open_pdf_externally": True,  # Download PDFs instead of opening in browser
    "safebrowsing.enabled": True
}

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)

service = Service(
    r"E:\drivers\chromedriver-win64\chromedriver.exe"
)

driver = webdriver.Chrome(
    service=service,
    options=options
)

driver.maximize_window()

driver.get(
    "https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/"
)

driver.find_element(
    By.XPATH,
    "(//a[contains(text(),'Download sample PDF file')])[1]"
).click()

time.sleep(10)

pdf_name = "file-example_PDF_1MB.pdf"  # Update this if the downloaded file name differs
pdf_path = os.path.join(download_path, pdf_name)

if os.path.exists(pdf_path):
    print("PDF downloaded successfully!")
else:
    print("PDF download failed!")
driver.quit()



# Uploading
# upload = driver.find_element(
#     By.XPATH,
#     "//input[@type='file']"
# )
#
# upload.send_keys(
#     r"C:\Users\Admin\Pictures\photo.jpg"
# )