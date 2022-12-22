import requests
from bs4 import BeautifulSoup
import regex as re

stock_url = "https://www.1stock1.com/1stock1_113.htm"
page = requests.get(stock_url)

stock_page = BeautifulSoup(page.content, 'html.parser')

stock_url_list = []

for a in stock_page.find_all('a', href=re.compile(r'1stock1_\d+\.htm')):
    if re.match(r'.+ - \(\w+\)', a.text):
        stock_url_list.append([a.text, a['href']])

print(stock_url_list)

