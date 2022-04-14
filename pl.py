from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://www.premierleague.com/stats/top/clubs/total_yel_card?se=418'

driver.get(url)

driver.implicitly_wait(10)

# js-accept-all-close

table = driver.find_element(by=By.CLASS_NAME, value="statsTableContainer")

print(table)


# driver.quit()