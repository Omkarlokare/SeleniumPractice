from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.current_url)
print(driver.title)

# CSS_Selector  tagname[@attriubute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('OM LOKARE')
driver.find_element(By.NAME, "email").send_keys('ABC@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('abc123')
driver.find_element(By.ID, 'exampleCheck1').click()

time.sleep(3)
#Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(1)
dropdown.select_by_visible_text('Female')
time.sleep(3)

# XPATH //input[@attribute='value']
driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('HelloAgain')
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

driver.find_element(By.XPATH, "//input[@value='Submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert 'Success' in message

driver.maximize_window()
time.sleep(5)
