from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver")

driver.maximize_window()

driver.get("https://www.facebook.com/")

driver.find_element(By.XPATH,"//*[text()='Create New Account']").click()