import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://trendoceans.com/blog')
print('Title: %s' % browser.title)
time.sleep(10)
browser.quit()