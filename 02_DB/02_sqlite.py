import sqlite3,os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db')
cur = conn.cursor()
cur.execute('''
select * from stocks
''')
# print(cur.fetchall())
for item in cur.fetchall():
    print(item[0],item[1],item[2],item[3],item[4])

conn.close()