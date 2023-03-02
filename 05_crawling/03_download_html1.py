import requests

# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# print(r.json())

r = requests.get('https://www.naver.com')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
# print(r.text)
# print(r.json())