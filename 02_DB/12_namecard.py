'''	명함관리프로그램

	데이터는 오라클저장 tablename : namecard
			       - cardid   (숫자값,기본키,자동증가)
			       - name
			       - address
			       - tel
			       - email

	프로그램 메뉴 - 명함추가, 명함 수정, 명함삭제, 명함 검색, 명함 리스트, 종료
              
	필요한 기능은 함수로 작성하세요
	  - table생성: create_table()
	  - 명함추가: insert_card()
               - 명함수정: update_card()
               - 명함삭제: delete_card()
               - 명함검색: search_card()
               - 명함리스트: list_card()
'''

import namecard as nc,sys
nc.create_table()
while True:
	display = '''
---------------------------------------------------------------
1.명함추가, 2.명함수정, 3.명함삭제, 4.명함검색, 5.명함리스트, 6.종료
>>>> '''
	menu = input(display)
	if menu == '1':
		nc.insert_card()
	elif menu == '2':
		nc.update_card()
	elif menu == '3':
		nc.delete_card()
	elif menu == '4':
		nc.search_card()
	elif menu == '5':
		nc.list_card()
	elif menu == '6':
		print('프로그램 종료!')
		sys.exit() # break
	else:
		print('메뉴 선택을 잘못하셨습니다.')
