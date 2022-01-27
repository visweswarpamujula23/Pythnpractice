from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Program Files\Drivers\chromedriver')

driver.get("http://www.python.org")

print(driver.title)

driver.close()
#driver.quit()
