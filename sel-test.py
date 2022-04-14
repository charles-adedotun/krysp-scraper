from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

import time

driver.get("https://www.tripadvisor.com/Airline_Review-d8729157-Reviews-Spirit-Airlines#REVIEWS")
more_buttons = driver.find_elements_by_class_name("moreLink")
for x in range(len(more_buttons)):
  if more_buttons[x].is_displayed():
      driver.execute_script("arguments[0].click();", more_buttons[x])
      time.sleep(1)
page_source = driver.page_source
print(page_source)