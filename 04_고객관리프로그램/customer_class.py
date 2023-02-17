from customer import Customer

Customer()

# cus = Customer()
# while True:
#     choice=input('''
#     다음 중에서 하실 일을 골라주세요 :
#     I - 고객 정보 입력
#     C - 현재 고객 정보 조회
#     P - 이전 고객 정보 조회
#     N - 다음 고객 정보 조회
#     U - 고객 정보 수정
#     D - 고객 정보 삭제
#     Q - 프로그램 종료
#     ''').upper()  

#     if choice=="I":
#         cus.insert_data()
#     elif choice=="C":
#         cus.current_data()
#     elif choice == 'P':
#         cus.before_data()
#     elif choice == 'N':
#         cus.next_data()
#     elif choice=='D':
#         cus.delete_data()
#     elif choice=="U": 
#         cus.update_data()            
#     elif choice=="Q":
#         print("프로그램 종료")
#         break
#     else:
#         print('메뉴를 잘못선택하셨습니다.')