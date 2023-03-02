from urllib import request

url = 'https://www.naver.com/'
result = request.urlopen(url).read()
print(type(result))
print(result.decode('utf8'))