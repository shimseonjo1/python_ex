'''
계좌개설- 계좌를 새로 만듭니다.
입금 - 계좌번호를 입력받아 여러 계좌 중에서 계좌번호 일치하는 계좌에 입금
출금 - 계좌번호를 입력받아 계좌번호 일치하는 계좌에 출금처리
계좌로그 - 계좌번호를 입력받아서 해당계좌의 로그를 출력합니다.
계좌정보 - 계좌번호를 입력받아서 계좌정보를 조회합니다. 
계좌리스트 - 전체 계좌를 목록으로 출력합니다.(정렬기능있음)
종료 - 종료시 데이터는 파일로 저장합니다.
시작 - 프로그램 시작시 데이터 파일을 로드합니다.
'''
import pickle, os
from Account import Account ,str2int  # Account.deposit()
#import Account                 Account.Account.deposit()


path = os.path.dirname(__file__)
account_list=[]
with open(path + '/account.pickle','rb') as f:
    account_list = pickle.load(f)

result=list(map(lambda x:x.account_number,account_list))
Account.account_count = max(result)

while True:
    display = '''
---------------------------------------------------------------------------
1. 계좌개설  2. 입금  3. 출금  4. 계좌로그  5. 계좌정보  6. 계좌리스트  7. 종료   
---------------------------------------------------------------------------
>>>  '''
    menu = input(display)
    if menu == '1':
        name = input('이름 >>> ')
        balance = str2int('입금 금액을 입력하세요')
        account_list.append(Account(name,balance))
        print('-'*50)
        for item in account_list:
            print(item)
    elif menu =='2':
        account_num = str2int('계좌번호를 입력하세요')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                amount =  int(input('입금할 금액을 입력하세요 >>> '))   
                acc.deposit(amount)
                break
        if check == 0 :
            print('계좌번호가 없습니다.')
    elif menu =='3':
        account_num = str2int('계좌번호를 입력하세요')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                amount =  int(input('출금할 금액을 입력하세요 >>> '))   
                acc.withdraw(amount)
                break
        if check == 0 :
            print('계좌번호가 없습니다.')
    elif menu =='4':
        account_num = str2int('계좌번호를 입력하세요')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                print(acc.total_log)
                break
        if check == 0 :
            print('계좌번호가 없습니다.')
    elif menu =='5':
        account_num = str2int('계좌번호를 입력하세요')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                print(acc)
                break
        if check == 0 :
            print('계좌번호가 없습니다.')
    elif menu =='6':
        key = input('정렬 키(입력값:name,balance,account_number)>>>> ')
        sort = bool(input('오름차순(enter),내림차순(1) >>> '))
        if key in ('name','balance','account_number'):
            sorted_list = sorted(account_list,reverse=sort,key=eval(f'lambda x : x.{key}'))
        else:
            sorted_list = sorted(account_list,reverse=sort)
        for acc in sorted_list:
            print(acc)    
    elif menu =='7':
        print('프로그램 종료!!')
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')

with open(path + '/account.pickle','wb') as f:
    pickle.dump(account_list,f)