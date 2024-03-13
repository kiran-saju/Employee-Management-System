import sqlite3
class Database:
    #constructor
    def __init__(self,db): #db is object of database
        #connection variable
        self.con=sqlite3.connect(db)
        #cursor object-for excecuting every query
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS emp(
        id Integer Primary key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()
    
    #Insert Function
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into emp values(null,?,?,?,?,?,?,?)",(name,age,doj,email,gender,contact,address))
        self.con.commit()

    #Fetch All data from DB
    def fetch(self):
        self.cur.execute("select*from emp")
        rows=self.cur.fetchall()
        #print(rows)
        return rows 

    #delete a record 
    def remove(self,id):
        self.cur.execute("delete from emp where id=?",(id,))
        self.con.commit()

    #update a record
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update emp set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",
                         (name,age,doj,email,gender,contact,address,id))
        self.con.commit()
        
    
#obj1=Database("Emp.db")
#obj1.insert("Sasi","28","12-10-2021","Sasi@gmail.com","male","7488181331","Sasi Villa")
#obj1.fetch()
# obj1.remove("2")
#obj1.update("3","Manu","25","12-10-2021","Sam@gmail.com","male","7488181221","Man8 Villa")

