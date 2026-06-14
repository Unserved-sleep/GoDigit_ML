import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
driver = uc.Chrome()

driver.get("https://www.facebook.com/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("abc")
time.sleep(5)

#   tag#id, #tag.class, tag[attribute='']--any attrib can be used as combination  tag.class[attrib=]