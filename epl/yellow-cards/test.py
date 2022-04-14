# import required modules
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd

# set up the webdriver
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

url = "https://www.premierleague.com/stats/top/clubs/total_yel_card?se=418" # set the url

driver.get(url) # open the url
driver.implicitly_wait(10) # in seconds

page_code = driver.page_source # Get the source code of the page

soup = BeautifulSoup(page_code, 'lxml') # Parse the source code
# print(soup)


stats_table = soup.find_all("div", class_="table playerIndex statsTable teamStatsTable") # Find the stats table

table_header = soup.find("thead").text # Find the table header


table = soup.findChildren("tbody") # Find the table body

print(table)



driver.quit() # Close the browser
