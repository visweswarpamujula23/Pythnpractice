# is_displayed()
# is_enabled()
# is_selected()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver")

driver.get("https://www.facebook.com/")

password_element= driver.find_element_by_input type("Email address or phone number")

print(password_element.is_displayed())

print(password_element.is_enabled())

user_ele = driver.find_element_by_placeholder("password")

print(user_ele.is_displayed()) #retuns true or false based on element status

print(user_ele.is_enabled()) #returns true/false