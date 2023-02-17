import re, sys
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

class Customer:

    def __init__(self):
        self.custlist= [{'name': 'hong1', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthday': '2000'},
            {'name': 'hong2', 'gender': 'M', 'email': 'hong2@gmail.com', 'birthday': '2000'},
            {'name': 'hong3', 'gender': 'M', 'email': 'hong3@gmail.com', 'birthday': '2000'},
            {'name': 'hong4', 'gender': 'M', 'email': 'hong4@gmail.com', 'birthday': '2000'}]
        self.page=3
        while True:
            self.exe(self.display())    

    def display(self):
        choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper() 
        return choice

    def exe(self,choice):
        if choice=="I":
            self.insert_data()
        elif choice=="C":
            self.current_data()
        elif choice == 'P':
            self.before_data()
        elif choice == 'N':
            self.next_data()
        elif choice=='D':
            self.delete_data()
        elif choice=="U": 
            self.update_data()            
        elif choice=="Q":
            print("프로그램 종료")
            sys.exit()
        else:
            print('메뉴를 잘못선택하셨습니다.')

    def insert_data(self):
        customer={'name':'','gender':'',"email":'',"birthyear":''}  
        customer['name'] = input('이름 >>>')
        while True:
            customer['gender'] = input('성별(M,m or F,f) >>> ').upper()
            if customer['gender'] in ('M','F'):
                break
        while True:
            customer['email'] = input('이메일 >>> ')
            check = None 
            for idx, i in enumerate(self.custlist):
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
        self.custlist.append(customer)
        self.page = len(self.custlist)-1

    def current_data(self):
        if self.page >= 0:
            print(f'현재 페이지는 {self.page+1}페이지 입니다.')
            print(self.custlist[self.page])
        else:
            print('입력된 정보가 없습니다.')

    def before_data(self):
        if self.page <= 0:
            print('첫번째 페이지 입니다.') 
            print(self.page)
        else:
            self.page -= 1
            print(f'현재 페이지는 {self.page+1}페이지 입니다.')
            print(self.custlist[self.page])

    def next_data(self):
        if self.page >= len(self.custlist)-1:
            print('마지막 페이지 입니다.')
            print(self.page)
        else:
            self.page += 1
            print(f'현재 페이지는 {self.page+1}페이지 입니다.')
            print(self.custlist[self.page])

    def update_data(self):
        email = input('수정할 고객의 이메일 >>> ')
        idx = -1
        for id, i in enumerate(self.custlist):
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
                self.custlist[idx][key] = input('수정할 {}를 입력하세요'.format(key))

    def delete_data(self):
        email = input('삭제하려는 고객의 이메일을 입력하세요 >>> ').strip()
        delok = 0
        for idx,i in enumerate(self.custlist):
            if i['email'] == email:
                data = self.custlist.pop(idx)
                print('{}님의 정보가 삭제되었습니다.'.format(data['name']))
                delok=1
                break
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
        print(self.custlist)
        self.page = len(self.custlist)-1


if __name__ == '__main__':
    a = Customer()
    a.insert_data()
    a.current_data()
    a.before_data()
    a.before_data()
    a.next_data()
    a.next_data()
    a.update_data()
    a.delete_data()