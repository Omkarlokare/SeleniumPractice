import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\lokar\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

browserSortedVeggieList = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
time.sleep(2)
# click on the column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
time.sleep(2)

# Collect all the veggie names = browserSortedVeggieList
veggieWebElement = driver.find_elements(By.XPATH, "//td[1]")
for i in veggieWebElement:
    browserSortedVeggieList.append(i.text)

originalBrowserSortedVeggieList = browserSortedVeggieList.copy()
# Sort the browserSortedVeggieList => which becomes newSortedList
browserSortedVeggieList.sort()

# browserSortedVeggieList == newSortedList
assert browserSortedVeggieList == originalBrowserSortedVeggieList
