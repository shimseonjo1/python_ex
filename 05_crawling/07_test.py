import requests
from urllib import request
from bs4 import BeautifulSoup
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%B4%84
key = input('검색어 >>> ')
url='https://search.naver.com/search.naver'
param ={
    'query':key,
    'where':'image'
}
res = requests.get(url, params=param)
soup = BeautifulSoup(res.text,'lxml')
result = soup.find_all('img')
# print(result)
for i,item in enumerate(result):
    try:
        # print(item['src'])
        index = item['src'].index('&')
        src = item['src'][:index]
        print('----------')
        print(src)
        filetype = src[-3:]
        print(filetype)
        request.urlretrieve(src,'05_crawling/down/'+str(i)+'.'+filetype)
    except:
        print('url 오류')
    if i >= 10:break
