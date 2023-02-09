

def add1():
    a = input('a=')
    b = input('b=')
    print(a+b)
    return

def add2():
    a = input('a=')
    b = input('b=')
    print(a+b)
    return a+b

def add(a,b):
    a = a+b
    print('in',a)
    return a

# a=7
# b=3
# print('out',add(a,b))
# print('out',a,b)

# def add(a,b):
#     a[0] = b
#     print('in',a)
#     return a

# a = [1,2,3]
# b = [4,5,6]
# print('out',add(a,b))
# print('out',a,b)


# def test(t):
#     print(x)
#     t=20
#     print('in:',t)

# x = 10
# test(x)
# print('out:',x)
# print('out:',t)


# def add(a,b=6):
#     return a+b

# print(add(2))


def add(**a):
    print(a)

print(add(a=1,b=3,f=6))









