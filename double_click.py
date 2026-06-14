from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")


field1 = driver.find_element(By.ID, "field1")

field1.clear()
field1.send_keys("Welcome")

button = driver.find_element(
    By.XPATH,
    "//button[text()='Copy Text']"
)

actions = ActionChains(driver)

actions.double_click(button).perform()


# Drag and Drop
# source = driver.find_element(By.ID,"draggable")
# target = driver.find_element(By.ID,"droppable")
#
# actions = ActionChains(driver)
#
# actions.drag_and_drop(
#     source,
#     target
# ).perform()


# sliders - volumes
# actions.drag_and_drop_by_offset(
#     min_slider,
#     100,
#     0
# ).perform()
#
# actions.drag_and_drop_by_offset(
#     max_slider,
#     -50,
#     0
# ).perform()


# scrolling webpage
# driver.execute_script(
#     "window.scrollBy(0,3000)"
# )

# driver.execute_script(
#     "arguments[0].scrollIntoView();",
#     element
# )   until webpage is visible

# to bottom
# "window.scrollBy(0,document.body.scrollHeight)"

#to top
#    "window.scrollBy(0,-document.body.scrollHeight)"
