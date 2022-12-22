# DOWNLOAD PYTHON
# https://www.python.org/downloads/windows/

import requests
from bs4 import BeautifulSoup
import regex as re

alphabetical_stocks = "https://www.1stock1.com/1stock1_113.htm"
page = requests.get(alphabetical_stocks)

alphabetical_page = BeautifulSoup(page.content, 'html.parser')

stock_url_list = []

for a in alphabetical_page.find_all('a', href=re.compile(r'1stock1_\d+\.htm')):
    if re.match(r'.+ - \(\w+\)', a.text):
        stock_url_list.append([a.text, f'1stock1.com/{a["href"]}'])

print(stock_url_list)

single_stock = "https://www.1stock1.com/1stock1_1882.htm"
single_stock_page = requests.get(single_stock)

single_stock_page = BeautifulSoup(single_stock_page.content, 'html.parser')

single_stock_values = []

for table in single_stock_page.find_all('tbody', href=False):
    for row in table.find_all('tr'):
        mini_list = []
        columns = row.find_all('td')
        if len(columns) == 5:
            for x in columns:
                mini_list.append(x.text.strip())
        if mini_list:
            single_stock_values.append(mini_list)

print(single_stock_values)
