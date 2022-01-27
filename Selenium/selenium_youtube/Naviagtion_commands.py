import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver")

driver.get("https://www.facebook.com/ ")

print(driver.title)

time.sleep(5)

driver.get("https://www.python.org/")

print(driver.title)
time.sleep(5)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)