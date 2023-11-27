from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

elements = driver.find_elements(By.XPATH, "//*[@id='content']/div/section/div[3]/div[2]/div/ul/li")

events = {index: {"time": parts[0], "name": parts[1]} for index, element in enumerate(elements)
          if (parts := element.text.split("\n"))
          }

print(events)
driver.quit()
