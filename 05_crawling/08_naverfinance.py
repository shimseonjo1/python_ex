import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/exchangeList.naver'
re = requests.get(url).text
soup = BeautifulSoup(re,'html.parser')
name = []
price = []

data = soup.select('td.tit a')
# print(data)
for item in data:
    name.append(item.string.strip())
# print(name)

data = soup.select('td.sale')
for item in data:
    price.append(float(item.string.replace(',','')))
# print(price)
items = list(zip(name,price))
print(items)


