from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"a[href*='/angularpractice/shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry" :
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

