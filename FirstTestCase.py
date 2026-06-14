#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

#service = Service(r"E:\drivers\chromedriver-win64\chromedriver.exe")
#driver = webdriver.Chrome(service=service)
driver = uc.Chrome()
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com")

# Clear existing text and enter email
email = driver.find_element(By.ID, "Email")
email.clear()
email.send_keys("admin@yourstore.com")
#driver.findlelemnt by xpath, link_text, partial_link_text

# Clear existing password and enter password
password = driver.find_element(By.NAME, "Password")
password.clear()
password.send_keys("admin")

# Click login button
login_btn = driver.find_element(By.CLASS_NAME, "login-button")
login_btn.click()

time.sleep(10)

act_title = driver.title
print("Page Title:", act_title)

if act_title == "Dashboard / nopCommerce administration":
    print("Login Successful")
else:
    print("Login Failed")

#driver.close() for closing 1
driver.quit()


#sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
#print(len(sliders))   find all sliders, or class objs,
#by.tab_name, "a"      find all links
#elements for all, element for first