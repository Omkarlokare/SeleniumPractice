import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Hi"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext
alert.accept()