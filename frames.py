"""
driver.switch_to.frame("frameName")
driver.switch_to.frame("frameID")

frame = driver.find_element(
    By.XPATH,
    "//iframe"
)
driver.switch_to.frame(frame)

driver.switch_to.frame(0)

driver.switch_to.default_content()  ---return to main page
"""


# driver.switch_to.frame("packageListFrame")
#
# driver.find_element(
#     By.LINK_TEXT,
#     "org.openqa.selenium"
# ).click()
#
# driver.switch_to.default_content()
#
# driver.switch_to.frame("packageFrame")
#
# driver.find_element(
#     By.LINK_TEXT,
#     "WebDriver"
# ).click()
#
# driver.switch_to.default_content()
#
# driver.switch_to.frame("classFrame")
#
# driver.find_element(
#     By.LINK_TEXT,
#     "Help"
# ).click()


# outer = driver.find_element(
#     By.XPATH,
#     "//iframe[1]"
# )
#
# driver.switch_to.frame(outer)
#
# inner = driver.find_element(
#     By.XPATH,
#     "//iframe"
# )
#
# driver.switch_to.frame(inner)
#
# driver.find_element(
#     By.XPATH,
#     "//input"
# ).send_keys("Welcome")  --switch to parent frame
''' outer frame -> inner frame-> element

print(driver.current_window_handle)  current window id
print(driver.window_handles)  all window handles
driver.switch_to.window(windowID)  switching between windows

if driver.title == "Child Window":
       driver.close()   closing specific
''' 