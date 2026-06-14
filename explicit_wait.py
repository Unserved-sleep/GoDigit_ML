from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  undetected_chromedriver as uc
from selenium.webdriver.common.by import By

driver = uc.Chrome()

'''
element = wait.until(
    EC.presence_of_element_located((By.XPATH,
                                    "locator"))
)


button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "submit")
    )
)
button.click()

    EC.alert_is_present()
    EC.title_contains("Google")
    EC.url_contains("dashboard")

'''

driver.get("https://google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium")
search.submit()
wait = WebDriverWait(driver, 10)
#wait = WebDriverWait(driver,10,poll_frequency=2) 
link = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//h3[text()='Selenium']")
    )
)

link.click()
driver.quit()



from selenium.common.exceptions import *
wait = WebDriverWait(
    driver,
    10,
    ignored_exceptions=[
        NoSuchElementException,
        ElementNotVisibleException,
        ElementNotSelectableException
    ]
)