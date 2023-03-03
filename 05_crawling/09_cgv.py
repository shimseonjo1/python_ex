from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/'
response = request.urlopen(url)
soup = BeautifulSoup(response,'html.parser')
print(soup)

result = soup.select('strong.title')
print(result)

for item in result:
    print(item.string)