import sqlite3
import os
print(sqlite3.version)
print(sqlite3.sqlite_version)
path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db')
cur = conn.cursor()
cur.execute('''
create table if not exists stocks
(date text,trans text,symbol text,qty real,price real)
''')
cur.execute('''
insert into stocks values('2023-01-02','buy','rhat',100,35.23)
''')
conn.commit()
conn.close()