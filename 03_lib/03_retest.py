import re

data = """
park 800905-1049118
kim  700905-1059119
"""

# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******",data))

# p = re.compile('ab*')
# print(p.match('cabb'))
# print(p.search('cab'))
# p = re.compile('[a-z]+')
# print(p.match('1asxr한'))
# result = p.search('1asxr한')
# print(result)
# print(result.start())
# print(result.end())
# print(result.span())
# print(result.group())
# print(result.groups())

p = re.compile('[0-9]{6}[-][1-4][0-9]{6}')
result = p.finditer(data)
print(result)
for r in result: print(r)