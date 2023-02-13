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
import sqlite3,os

path = os.path.dirname(__file__)

# 테이블 생성 함수
def create_table():
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    cur.execute(
    ''' 
    create table if not exists books(
    title text,
    published_date text,
    publisher text,
    pages integer,
    recommend integer)'''
    )
    conn.commit()
    conn.close()

create_table()

# 데이터 입력함수
def insert_books():
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    title = input('제목 >>> ')
    published_date = input('출판일 >>> ')
    publisher = input('출판사 >>> ')
    pages = input('총 page >>> ')
    recommend = input('추천수 >>> ')
    sql = 'insert into books values(?,?,?,?,?)'
    cur.execute(sql,(title,published_date,publisher,pages,recommend))
    conn.commit()
    conn.close()

# insert_books()

# 전체데이터 출력 함수
def all_books():
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    sql = 'select * from books'
    cur.execute(sql)
    for item in cur.fetchall():
        print(item)
    conn.close()

# all_books()
# 레코드 개수를 정해서 출력
def some_books(number):
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    sql = 'select * from books'
    cur.execute(sql)
    for item in cur.fetchmany(number):
        print(item)
    conn.close()

# number = int(input('출력할 데이터 갯수 >>> '))
# some_books(number)

# 한권만 출력
def one_book():
    pass

# 조건 지정 및 정렬하여 검색
# 정렬(asc,desc)
def big_books(key='title',sort='asc',cond=''):
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    if cond != '':
        cond = ' where '+ cond
    sql = f'select * from books {cond} order by {key} {sort}'
    cur.execute(sql)
    for item in cur.fetchall():
        print(item)
    conn.close()

# big_books('pages','desc','pages >= 300')
# big_books('pages','desc',"title like '%머신%' ")

# 책은 title로 구분한다. 
# 책 수정
#  - published_date 출판날짜
#  - publisher 출판사
#  - pages 페이지수
#  - recommend 추천여부

def update_book():
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    all_books()
    title = input('수정할 책 제목 >>> ')
    check = 1
    while check:
        col = input('수정할 컬럼이름(published_date,publisher,pages,recommend) >>> ')
        if col in ('published_date','publisher','pages','recommend'):
            check = 0
    value = input(f'{col}컬럼 수정할 내용 입력 >>> ')
    sql = f'update books set {col} = ? where title = ? '
    cur.execute(sql,(value,title))
    conn.commit()
    conn.close()

# update_book()
# 책 삭제
def delete_book():
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    all_books()
    title = input('삭제할 책 제목 >>> ')
    sql = 'delete from books where title = ?'
    cur.execute(sql,[title])
    conn.commit()
    conn.close()

delete_book()