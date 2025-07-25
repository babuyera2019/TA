from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium with Python")
search_box.submit()

driver.quit()