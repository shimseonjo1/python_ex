import cardfunc as cf

# card=[{'name':'홍길동', 'address':'서울', 'tel':'111-1111-1111', 'email':'hong@gmail.com'},
#       {'name':'김나리', 'address':'광주', 'tel':'111-1111-1111', 'email':'kim@gmail.com'}]
card = []
card = cf.dataload(card)
while True:
    menu = input('''
--------------------------------------------------
1.저장  2.수정  3.삭제  4.리스트  5.검색  6.종료(Q)
--------------------------------------------------
>>> ''')
    if menu =='1':
        cf.save(card)
    elif menu == '2':
        cf.update(card)
    elif menu == '3':
        cf.delete(card)
    elif menu == '4':
        cf.cardlist(card)
    elif menu == '5':
        cf.search(card)
    elif menu in ('6','Q','q'):
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')
cf.datasave(card)