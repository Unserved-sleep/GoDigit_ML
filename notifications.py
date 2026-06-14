from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()

options = webdriver.ChromeOptions()  #create chrome options
options.add_argument("--disable-notifications") #disable

driver = webdriver.Chrome(
    service=service_obj,
    options=options
)

driver.get("https://whatmylocation.com/")
driver.maximize_window()