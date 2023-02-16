import customer as cus
custlist= [{'name': 'hong1', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthday': '2000'},
           {'name': 'hong2', 'gender': 'M', 'email': 'hong2@gmail.com', 'birthday': '2000'},
           {'name': 'hong3', 'gender': 'M', 'email': 'hong3@gmail.com', 'birthday': '2000'},
           {'name': 'hong4', 'gender': 'M', 'email': 'hong4@gmail.com', 'birthday': '2000'}]
page=3

while True:
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

    if choice=="I":
        page = cus.insert_data(custlist)
    elif choice=="C":
        cus.current_data(custlist,page)
    elif choice == 'P':
        page = cus.before_data(custlist,page)
    elif choice == 'N':
        page = cus.next_data(custlist,page)
    elif choice=='D':
        page = cus.delete_data(custlist,page)
    elif choice=="U": 
        cus.update_data(custlist)            
    elif choice=="Q":
        print("프로그램 종료")
        break
    else:
        print('메뉴를 잘못선택하셨습니다.')