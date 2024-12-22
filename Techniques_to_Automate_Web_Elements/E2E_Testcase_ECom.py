import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)

ExpectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
ActualList = []

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))

for result in results:
    ActualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()  #Chaining Parent webElement to Child webElement

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discountedAmt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert totalAmount > discountedAmt
