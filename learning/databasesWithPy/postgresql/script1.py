import sqlite3

def create_table():
	conn=sqlite3.connect("lite1.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE if NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)")
	conn.commit()
	conn.close()

def insert(item,quantity,price):
	conn=sqlite3.connect("lite1.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
	conn.commit()
	conn.close()	

create_table()
#insert("wine bottle",8,185.0)
#insert("coffee",4,205.25)

def view():	
	conn=sqlite3.connect("lite1.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM store")	
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(item):
	conn=sqlite3.connect("lite1.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM store WHERE item=?",(item,))
	conn.commit()
	conn.close()

def update(item,quantity,price):
	conn=sqlite3.connect("lite1.db")
	cur=conn.cursor()
	cur.execute("UPDATE store SET quantity=? , price=? WHERE item=?",(quantity,price,item))
	conn.commit()
	conn.close()	

delete("coffee")

update("wine bottle",3,675.75)

print(view())