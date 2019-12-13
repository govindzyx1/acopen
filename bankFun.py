import sqlite3
con=sqlite3.connect("e:\\pyprg\\mydb6.db")
cur=con.cursor()
con.execute('''create table if not exists bank(name text not null,acno integer primary key,bal integer)''')

def showOption():
    print("1 Deposit:")
    print("2 Withdraw:")
    print("3 Check bal:")
    print("4 Show Detail: ")
    print("5 Open A/c:")
    x = int(input("your option:"))
    return x

def deposite():
    acno = int(input("Enter the account no :"))
    amt = int(input("Enter the amount to deposite :"))
    cur.execute("""select bal from bank WHERE acno = %d""" %acno )
    a=cur.fetchone()
    nbal=a[0]+amt
    con.execute("""update bank SET bal = %d WHERE acno = %d"""%(nbal,acno))
    print(nbal)
    con.commit()
    
def withdraw():
    cur=con.cursor()
    acno = int(input("Enter the account no :"))
    amt = int(input("Enter the amount to withdraw :"))
    cur.execute("""select bal from bank WHERE acno = %d""" %acno )
    a=cur.fetchone()
    nbal=a[0]-amt
    cur.execute("""update bank SET bal = %d WHERE acno = %d"""%(nbal,acno))
    print(nbal)
    con.commit()

def checkBal():
    cur=con.cursor()
    acno = int(input("Enter the account no :"))
    rec=cur.execute('''select * from bank WHERE acno= %d''' %acno)
    a=cur.fetchone()
    v=a[3]
    print(v)

def openAc():
    cur=con.cursor()
    name = input("Enter the account holder name : ")
    acno = int(input("Enter the account no : "))
    bal = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current:"))
    con.execute('''insert into bank(name,acno,bal) values('%s',%d,%d)'''%(name,acno,bal))
    print("\n\n\nAccount Created")
    con.commit()

def show():
    cur=con.cursor()
    rec=cur.execute('''select * from bank''');
    for row in rec:
        print(row[0],row[1],row[2])
    

