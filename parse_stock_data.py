# DOWNLOAD PYTHON
# https://www.python.org/downloads/windows/

import requests
from bs4 import BeautifulSoup
import regex as re
import pandas as pd


all_letters_url = "https://www.1stock1.com/1stock1_112.htm"
page = requests.get(all_letters_url)
all_letters_page = BeautifulSoup(page.content, 'html.parser')

lettered_websites = []

for x in all_letters_page.find_all('a', href=re.compile(r'1stock1_\d+\.htm')):
    if re.match('[A-Z] Stocks.*', x.text):
        lettered_websites.append([x.text, f"https://www.1stock1.com/{x['href']}"])



all_stock_values = []

for page_letter, alphabetical_stocks in lettered_websites:
    print(f'You are now starting: {page_letter}')
    page = requests.get(alphabetical_stocks)

    alphabetical_page = BeautifulSoup(page.content, 'html.parser')

    stock_url_list = []

    for a in alphabetical_page.find_all('a', href=re.compile(r'1stock1_\d+\.htm')):
        if re.match(r'.+ - \(\w+\)', a.text):
            stock_url_list.append([a.text, f'https://www.1stock1.com/{a["href"]}'])

    for stock_name, single_stock_url in stock_url_list:
        single_stock_page = requests.get(single_stock_url)

        single_stock_page = BeautifulSoup(single_stock_page.content, 'html.parser')

        for table in single_stock_page.find_all('tbody', href=False):
            for row in table.find_all('tr'):
                mini_list = []
                columns = row.find_all('td')
                if len(columns) == 5:
                    for x in columns:
                        mini_list.append(x.text.strip())
                if mini_list:
                    all_stock_values.append([stock_name, single_stock_url] + mini_list)

df_columns = ['company_name', 'company_url', 'year', 'start_price', 'end_price', 'gain_or_loss',
              'percent_gain_or_loss']

stock_df = pd.DataFrame(all_stock_values, columns=df_columns)

stock_df.drop(stock_df[stock_df['year'] == 'Year'].index, inplace=True)

print(stock_df)

stock_df.to_csv('/Users/samuelspencer/Gain_Loss_Web_Scrape/all_stocks_and_prices.csv', sep='|')
