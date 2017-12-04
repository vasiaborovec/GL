import sqlite3
import random

con = sqlite3.connect('pythonsqlite.db')
cur = con.cursor()

names = ['a', 'b', 'c', 'd', 'e']
status = ['activ', 'block', 'activ']
print(random.choice(names))

for i in range(1, 1001):
    cur.execute("insert into Users values (?, ?, ?, ?, ?)", (i, random.choice(names), random.choice(status), '2008-11-11', '2008-11-11'))
con.commit()
for i in range(1, 1000000):
    cur.execute("insert into Comments values (?, ?, ?)",(i,'some text', random.randint(1, 855)))
con.commit()
con.close()