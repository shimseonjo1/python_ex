import oracledb
oracledb.init_oracle_client()
with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as connection:
    with connection.cursor() as cursor:
        sql = """select * from dept where deptno = :1"""
        for r in cursor.execute(sql,[10]):
            print(r)