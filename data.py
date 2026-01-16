import sqlite3
con = sqlite3.connect("SCHLOR.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS teachers(
            phone INTEGER UNIQUE ,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            passward TEXT NOT NULL
        )
        """)
con.commit()
con.close()
print("yes table is created")