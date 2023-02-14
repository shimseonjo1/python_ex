import oracledb
oracledb.init_oracle_client()

try:
    conn = oracledb.connect('SCOTT/TIGER@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select * from dept')
    print(cur.fetchall())
    sql ='delete dept WHERE DEPTNO = :1 '
    deptno = input('삭제할 부서코드 >>>')
    data =(deptno,)
    cur.execute(sql,data)
    conn.commit()
    conn.close()
except Exception as e:
    print(e)
