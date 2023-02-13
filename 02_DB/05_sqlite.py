# 책정보를 저장하는 테이블
'''
books
 - title 책제목
 - published_date 출판날짜
 - publisher 출판사
 - pages 페이지수
 - recommend 추천여부
'''

''' 
create table if not exists books(
    title text,
    published_date text,
    publisher text,
    pages integer,
    recommend integer
)
'''
# 테이블 생성 함수
def create_table():
    pass

# 데이터 입력함수
def insert_books():
    pass

# 전체데이터 출력 함수
def all_books():
    pass

# 레코드 개수를 정해서 출력
def some_books():
    pass

# 한권만 출력
def one_book():
    pass

# 조건 지정 및 정렬하여 검색
def big_books():
    pass

# 책 수정
def update_book():
    pass

# 책 삭제
def delete_book():
    pass