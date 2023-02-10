class Account:

    account_count = 0  # 계좌가 개설된 건수

    @classmethod
    def get_account_num(cls):
       return  Account.account_count

    def __init__(self,name,balance):
        Account.account_count += 1
        self.account_number = Account.account_count
        self.name = name
        self.balance = balance
        self.total_log = []
        self.deposit_count = 0

    def deposit(self,amonut):  #입금처리
       if amonut >= 1:
        self.total_log.append(('입금',amonut))
        self.balance += amonut
        self.deposit_count += 1
        print(amonut,'원 입금처리 완료!')
        if self.deposit_count % 5 == 0:
            interest = round(self.balance * 0.01,-1)
            self.balance += interest
            self.total_log.append(('이자',interest))
            print(interest,'원의 이자가 지급되었습니다.')

    def withdraw(self,amount): #출금처리
        if self.balance >= amount:
            self.total_log.append(('출금',amount))
            self.balance -= amount
            print(amount,'원 출금처리 완료!')
        else:
            print('잔고가 부족합니다.')

    def displayinfo(self): #계좌정보출력함수
        print(self.__str__())

    def __str__(self):
        return f'예금주:{self.name}, 계좌번호:{self.account_number}, 잔고:{self.balance}'

# print(Account.account_count)
print(Account.get_account_num())
a = Account('홍길동',2000)
a.displayinfo()
a.deposit(5000)
a.displayinfo()
a.withdraw(4000)
a.displayinfo()
a.withdraw(4000)
a.displayinfo()
print(a.total_log)
