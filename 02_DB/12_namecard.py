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

import namecard
