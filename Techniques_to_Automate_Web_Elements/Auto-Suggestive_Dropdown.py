from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print(driver.current_url)
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        time.sleep(2)
        break

assert (driver.find_element(By.ID, "autosuggest").get_attribute('value')) == 'India'
