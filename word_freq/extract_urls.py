from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Insert your query
query = 'кльтура+спорт'

# Url we want to parse
URL = 'http://www.rbc.ru/search/?query=' + query

# Open page in browser
browser = webdriver.Chrome()
browser.get(URL)
time.sleep(1)
elem = browser.find_element_by_tag_name("body")

# Handle infinite scroller
no_of_pagedowns = 200
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1

# Get html
html_source = browser.page_source
soup = BeautifulSoup(html_source, 'html.parser')

# Get urls from html
with open('urls.txt', 'a') as output:
    counter = 1
    for href in soup.find_all('a'):
        classes = href.get('class')
        if classes is not None and 'search-item' in classes:

            output.write('{}\n'.format(href.get('href')))
            print('Saved {} urls'.format(counter))
            counter += 1