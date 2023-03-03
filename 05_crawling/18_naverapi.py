import urllib.request
import json

client_id = ""
client_secret = ""
query = input('검색할 단어 >>> ')
encText = urllib.parse.quote(query)
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

data = response_body.decode('utf-8')
print(type(data))
result = json.loads(data)
print(type(result))
print(result["items"][0]['title'])