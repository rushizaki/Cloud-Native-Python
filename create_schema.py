import sqlite3

conn = sqlite3.connect('apirelease.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE apirelease(
buildtime date,
version varchar(30) primary key,
links varchar2(30), methods varchar2(30));
""")

print('Table apirelease created')
conn.close()