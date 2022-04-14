from nerodia.browser import Browser
import pandas as pd
import time

# Using Selenium Chrome Options, set headless so the physical GUI of Chrome doesn't have to be used, and no sandbox to avoid crashes on Deepnote
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox') # Remove if running outside deepnote

browser = Browser('chrome', options=options) # Create Browser

browser.goto('https://www.premierleague.com/stats/top/players/goals?se=418') # Now use the browser to navigate to the EPL Stats Page

time.sleep(4) # Allow data time to load into HTML

goals_df = pd.read_html(browser.html)[0] # Use Pandas to fetch all the tables within the browser html, select the first table it finds ([0])

# Note: On the EPL site, when you've reached the end of the table, the table's Page Next element has 'inactive' added to it's class. Use browser tools to inspect the Page Next html element on the last page of the goals table to see for yourself.
# Note: As we know this, we can keep clicking the Page Next button and scraping the table until the element is 'inactive'. In Python we can use while not:
while not browser.div(class_name=['paginationBtn', 'paginationNextContainer', 'inactive']).exists:
  browser.div(class_name=['paginationBtn', 'paginationNextContainer']).fire_event('onClick') # fire onClick event on page next element. If it was a button element (not a div element), we could simply use .click() 
  # print('Next Page')
  goals_df = goals_df.append(pd.read_html(browser.html)[0]) # append the table from this page with the existing goals dataframe.

browser.close() # Close Browser

goals_df = goals_df[goals_df['Stat'] > 0] # Random Players at end of table with 0 goals...

goals_df = goals_df.dropna(axis=1, how='all') # Random Unamed Column (all NaN elements, so clear columns where 'all' values are NaN)

goals_df.to_csv(r'data/epl_goals_20_21.csv', index=False) # Save dataframe to new csv file

goals_df