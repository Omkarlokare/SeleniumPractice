import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, "div[class='tox-icon']").click()
time.sleep(2)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Im able to automate frame")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)

print(driver.title)
print(driver.current_url)