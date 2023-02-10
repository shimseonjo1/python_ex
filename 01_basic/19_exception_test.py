# for i in range(10):
#     try:
#         result = 10/i
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         print(result)
#     finally:
#         print('프로그램 종료')

# while True:
#     value = input('변환할 정수값을 입력해 주세요:')
#     for digit in value:
#         if digit not in '0123456789':
#             raise ValueError('숫자값이 아닙니다.')
#     print(int(value))

def get_binary_number(decimal_number):
    assert isinstance(decimal_number,int)
    return bin(decimal_number)

print(get_binary_number(10))
print(get_binary_number('10'))