from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# page.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = page.find_element(By.XPATH, "//*[@id='articlecount']/a[1]")
# print(article_count)


driver.get("https://secure-retreat-92358.herokuapp.com/")
name = driver.find_element(By.NAME, "fName")
name.send_keys("My Name")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("My Last Name")

email = driver.find_element(By.NAME, "email")
email.send_keys("my@email.com")

signup_button = driver.find_element(By.XPATH, "/html/body/form/button")
signup_button.click()
