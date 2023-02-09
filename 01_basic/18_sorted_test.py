# 리스트에 저장된 데이터 정렬
data = [
    ['홍길동','A',22],
    ['박정인','C',31],
    ['김철수','B',16],
    ['홍인경','C',23]
]

# data.sort(reverse=False,key=lambda x:(x[1],-x[2]))
# print(data)

# result = sorted(data,key=lambda x:(x[1],-x[2]))
# print(data)
# print(result)

# 딕셔너리에 저장된 데이터 정렬
data = [
    {'name':'홍길동','score':'A','age':22},
    {'name':'박정인','score':'C','age':31},
    {'name':'김철수','score':'B','age':16},
    {'name':'홍인경','score':'C','age':23}
]

# data.sort()
result = sorted(data,key=lambda x:x['name'])
print(result)


# 클래스에 저장된 데이터 정렬

