import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")

links = driver.find_elements(By.TAG_NAME, "a")
broken_links = 0

for link in links:
    url = link.get_attribute("href")
    try:
        response = requests.head(url)
        if response.status_code >= 400:
            print(url,
                  "Broken Link")
            broken_links += 1
        else:
            print(url,
                  "Valid Link")
    except:
        pass

print("Total Broken Links:",
      broken_links)
driver.quit()