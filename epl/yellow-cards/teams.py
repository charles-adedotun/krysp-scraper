# Import required modules
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
import requests
import time
from bs4 import BeautifulSoup
import lxml
import pandas as pd

# Set up the webdriver
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

url = "https://www.premierleague.com/stats/top/clubs/total_yel_card?se=418"     # set the url

driver.get(url)     # open the url
driver.maximize_window()    # maximize the window

print("waiting for page to load ...")
time.sleep(10)   # wait for 10 seconds

page_code = driver.page_source      # Get the source code of the page

soup = BeautifulSoup(page_code, 'lxml')     # Parse the source code

table = soup.find("table")      # Find the table

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

# Export the dataframe to a csv file
print(df)
df.to_csv('./data/teams.csv', index=False)

# Kill Firefox Browser
os.system('pkill -f firefox')