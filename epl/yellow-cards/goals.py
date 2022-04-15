# import required modules
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
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

url = "https://www.mykhel.com/football/premier-league-team-stats-l8/"     # set the url

driver.get(url)     # open the url
driver.maximize_window()    # maximize the window

print("waiting for page to load ...")
time.sleep(10)   # wait for 10 seconds

page_code = driver.page_source      # Get the source code of the page

soup = BeautifulSoup(page_code, 'lxml')     # Parse the source code

div_table = soup.find("div", {"id": "goals-block"})

table =div_table.find("table")      # Find the table

headers = []    # Create an empty list to store the table headers

# Loop through the table header and store the text in the list
for th in table.find_all("th"):
    headers.append(th.text)

df = pd.DataFrame(columns=headers)    # Create a dataframe with the headers

# Loop through the table body and store the text in the dataframe
for row in table.find_all("tr")[1:]:
    data = row.find_all("td")
    row_data = [td.text for td in data]
    length = len(df)
    df.loc[length] = row_data

print(df)
df.to_csv('./data/goals.csv', index=False)

# Kill Firefox Browser
os.system('pkill -f firefox')
