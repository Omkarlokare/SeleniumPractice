import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
#driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to_window(windowsOpened[1])
print(driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text)
driver.close()
driver.switch_to_window(windowsOpened[0])

assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

print(driver.title)
print(driver.current_url)