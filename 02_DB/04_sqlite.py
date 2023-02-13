import sqlite3,os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db')
cur = conn.cursor()
sql = 'insert into stocks values(?,?,?,?,?)'
# data = ('2022-01-08','buy','ibm',1000,45.00)
# cur.execute(sql,data)
data = [('2022-01-08','buy','ibm',1000,45.00),
        ('2022-02-011','sell','ibm',500,48.00),
        ('2022-03-08','buy','msft',400,72.00),
        ('2022-07-20','buy','rhat',120,37.00),
        ('2022-11-08','sell','rhat',150,45.00),]
cur.executemany(sql,data)
conn.commit()
conn.close()