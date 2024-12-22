import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for option in checkboxes:
    if option.get_attribute("value") == "option2":
        option.click()
        time.sleep(2)
        assert option.is_selected()
        break

radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobutton[1].click()
time.sleep(2)
assert radiobutton[1].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()