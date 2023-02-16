import re
def insert_data(custlist):
    customer={'name':'','gender':'',"email":'',"birthyear":''}  
    customer['name'] = input('이름 >>>')
    while True:
        customer['gender'] = input('성별(M,m or F,f) >>> ').upper()
        if customer['gender'] in ('M','F'):
            break
    while True:
        customer['email'] = input('이메일 >>> ')
        check = None 
        for idx, i in enumerate(custlist):
            if i['email'] == customer['email']:
                check=idx
                break
        if check==None:
            p = re.compile('@[a-z]{2,}[.][a-z]{2,}')
            if p.search(customer['email'])!=None:
                break
            else:
                print('@를 포함한 정확한 이메일을 입력하세요')
        else:
            print('중복되는 이메일이 있습니다.')

    while True:
        customer['birthyear'] = input('출생년도(4자리) >>> ')
        try:
            int(customer['birthyear'])
        except:
            print('숫자를 입력하세요')
        else:
            if len(customer['birthyear']) == 4:
                break
            else:
                print('4자리로 입력해주세요')
    print(customer)
    custlist.append(customer)
    page = len(custlist)-1
    return page

def current_data(custlist,page):
    if page >= 0:
        print(f'현재 페이지는 {page+1}페이지 입니다.')
        print(custlist[page])
    else:
        print('입력된 정보가 없습니다.')

def before_data(custlist,page):
    if page <= 0:
        print('첫번째 페이지 입니다.') 
        print(page)
    else:
        page -= 1
        print(f'현재 페이지는 {page+1}페이지 입니다.')
        print(custlist[page])
    return page

def next_data(custlist,page):
    if page >= len(custlist)-1:
        print('마지막 페이지 입니다.')
        print(page)
    else:
        page += 1
        print(f'현재 페이지는 {page+1}페이지 입니다.')
        print(custlist[page])
    return page


def update_data(custlist):
    email = input('수정할 고객의 이메일 >>> ')
    idx = -1
    for id, i in enumerate(custlist):
        if i['email'] == email:
            print(i['email'])
            idx = id
            break
    if idx == -1:
        print('등록되지 않은 이메일입니다.')
    else:
        key = input('''
다음 중 수정할 항목은(name,gender,birthyear)
수정할 정보가 없으면 enter >>> ''')
        if key in ('name','gender','birthyear'):
            custlist[idx][key] = input('수정할 {}를 입력하세요'.format(key))


def delete_data(custlist,page):
    email = input('삭제하려는 고객의 이메일을 입력하세요 >>> ').strip()
    delok = 0
    for idx,i in enumerate(custlist):
        if i['email'] == email:
            data = custlist.pop(idx)
            print('{}님의 정보가 삭제되었습니다.'.format(data['name']))
            delok=1
            break
    if delok == 0:
        print('등록되지 않은 이메일입니다.')
    print(custlist)
    page = len(custlist)-1
    return page

if __name__ == '__main__':
    pass