from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, ClassName, Name, linkText
driver.find_element(By.CSS_SELECTOR, "name").send_keys("OM")
driver.find_element(By.NAME, "email").send_keys("demo@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")

driver.maximize_window()
print(driver.title)
print(driver.current_url)