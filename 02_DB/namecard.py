import oracledb
oracledb.init_oracle_client()

'''
drop table namecard;

drop sequence namecard_seq;

create sequence namecard_seq 
increment by 1
start with 1;

'''
def create_table():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            sql = '''
            create table namecard(
                cardid number primary key,
                name varchar2(50),
                address varchar2(100),
                tel varchar2(20),
                email varchar2(50)
            )
            '''
            try:
                cur.execute(sql)
            except Exception as e:
                print(e)

def insert_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            sql = 'insert into namecard values(namecard_seq.NEXTVAL,:1,:2,:3,:4)'
            name = input('이름 >>> ')
            address = input('주소 >>> ')
            tel = input('전화번호 >>> ')
            email = input('이메일 >>> ')
            try:
                cur.execute(sql,(name,address,tel,email))
                conn.commit()
            except Exception as e:
                print(e)

def update_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            cardid_list = []
            for item in cur.execute('select * from namecard'):
                print(f'등록번호:{item[0]},이름:{item[1]},전화번호:{item[3]},이메일:{item[4]},주소:{item[2]}')
                cardid_list.append(item[0])
            key = int(input('수정할 등록번호 >>> '))
            if key in cardid_list:
                col = input('수정할 항목(name,address,tel,email)>>> ')
                data = input('수정할 값 >>> ')
                sql = f'update namecard set {col} =:1 where cardid = :2'
                cur.execute(sql,(data,key))
                conn.commit()

def delete_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            cardid_list = []
            for item in cur.execute('select * from namecard'):
                print(f'등록번호:{item[0]},이름:{item[1]},전화번호:{item[3]},이메일:{item[4]},주소:{item[2]}')
                cardid_list.append(item[0])
            key = int(input('삭제할 등록번호 >>> '))
            if key in cardid_list:
                sql = f'delete namecard where cardid = :1'
                cur.execute(sql,(key,))
                conn.commit()

def search_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            cardid_list = []
            for item in cur.execute('select cardid from namecard'):
                cardid_list.append(item[0])
            print(cardid_list)
            key = int(input('검색할 등록번호 >>> '))
            cur.execute('select * from namecard where cardid = :1',(key,))
            print(cur.fetchone())

def list_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            key = input('정렬 키(name,tel,address,email) >>> ')
            sort = input('오름차순(asc),내림차순(desc) >>> ')
            if key in ('name','tel','address','email') and sort in ('asc','desc'):
                sql = f'select * from namecard order by {key} {sort}'
                for item in cur.execute(sql):
                    print(f'등록번호:{item[0]},이름:{item[1]},전화번호:{item[3]},이메일:{item[4]},주소:{item[2]}')

if __name__ == '__main__':
    create_table()
    # insert_card()
    # update_card()
    # delete_card()
    # search_card()
    list_card()