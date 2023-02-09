card=[['홍길동', '서울', '111-1111-1111', 'hong@gmail.com'],
      ['김나리', '광주', '111-1111-1111', 'kim@gmail.com']]
while True:
    menu = input('''
--------------------------------------------------
1.저장  2.수정  3.삭제  4.리스트  5.검색  6.종료(Q)
--------------------------------------------------
>>> ''')
    if menu =='1':
        while True:
            name = input('이름을 입력하세요 >>>')
            check = 0
            for item in card:
                if item[0] == name:
                    check = 1
            if check == 0:
                break
            print('중복되는 이름이 있습니다.')
            
        address = input('주소를 입력하세요 >>>')
        tel = input('전화번호를 입력하세요 >>>')
        email = input('이메일을 입력하세요 >>>')
        card.append([name,address,tel,email])   
        print(card)
    elif menu == '2':
        name = input('수정할 데이터 이름 >>>')
        idx = -1
        for i, item in enumerate(card):
            if item[0] == name:
                idx = i
                update = int(input('수정할 정보(1.address,2.tel,3.email)>>> '))
                card[idx][update] = input('수정내용>>> ')
                print(card[idx])
                break
        if idx == -1:
            print('등록되지 않은 데이터 입니다.')

    elif menu == '3':
        name = input('삭제할 이름 입력 >>> ')
        delok = 0
        for i, item in enumerate(card):
            if item[0] == name :
                print(item,'삭제!!')
                del card[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 데이터 입니다.')    

    elif menu == '4':
        for item in card:
            print(f'''
----------------------------------
  이    름 : {item[0]}
  주    소 : {item[1]}
  전화번호 : {item[2]}
  이 메 일 : {item[3]} ''')

    elif menu == '5':
        name = input('검색할 이름 >>>')
        idx = -1
        for i, item in enumerate(card):
            if item[0] == name:
                idx = i
                print(item)
                break
        if idx == -1:
            print('등록되지 않은 데이터 입니다.')

    elif menu in ('6','Q','q'):
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')