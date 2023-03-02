# https://search.naver.com/search.naver?sm=tab_sug.mbk&where=nexearch&query=%EB%B2%9A%EA%BD%83%EC%B6%95%EC%A0%9C&oquery=%EB%B2%97%EA%BD%83&tqi=iss4cdprvmZssjvKNq4ssssstNR-391098&acq=%EB%B2%97%EA%BD%83&acr=4&qdt=0

from urllib import request, parse
query = input('검색할 키 >>> ')
api = 'https://search.naver.com/search.naver?'
values = {
# 'sm':'tab_sug.mbk',
# 'where':'nexearch',
'query': query,
# 'oquery':'벚꽃',
# 'tqi':'iss4cdprvmZssjvKNq4ssssstNR-391098',
# 'acq':'벚꽃',
# 'acr':4,
# 'qdt':0,
}

params = parse.urlencode(values)
print(params)
url = api + params
print(url)

result = request.urlopen(url).read().decode('utf8')
print(result)