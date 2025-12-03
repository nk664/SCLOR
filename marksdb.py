import sqlite3
con = sqlite3.connect("student.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS python(roll_no PRIMARY KEY, name, Python )")

con.commit()
con.close()
print("yes table is created")