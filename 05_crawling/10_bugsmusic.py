from urllib import request
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
response = request.urlopen(url)
soup = BeautifulSoup(response,'html.parser')

title_list = []
artist_list = []

title = soup.select('p.title > a')
# print(title)
for item in title:
    # print(item.string)
    title_list.append(item.string)

artist = soup.select('p.artist > a')
for item in artist:
    # print(item.string)
    artist_list.append(item.string.strip())

result = list(zip(title_list,artist_list))
print(result)