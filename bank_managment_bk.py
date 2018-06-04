import sqlite3 as s
from tkinter import *
from tkinter import messagebox
class account():
    #def __init__(self):
        #self.a=10
       # print("object formed")
    def create_submit(self,A,n,a,p,e):
        Ac_no=A.get()
        name=n.get()
        age=a.get()
        phone=p.get()
        email=e.get()
        balance=0
        conn=s.connect('ravi.db')
        conn.execute('CREATE TABLE IF NOT EXISTS details(Ac_no int,Name text ,Age int,phone int,email text,Balance int)')
        conn.execute("INSERT INTO details VALUES(?,?,?,?,?,?)",(Ac_no,name,age,phone,email,balance))
        conn.commit()
        conn.close()
        A.delete(0,END)
        n.delete(0,END)
        a.delete(0,END)
        p.delete(0,END)
        e.delete(0,END)
        
        
    def update_account(self,A,n,a,p,e):
        Ac_no=A.get()
        name=n.get()
        age=a.get()
        phone=p.get()
        email=e.get()
        conn=s.connect('ravi.db')
        #conn.execute('CREATE TABLE IF NOT EXISTS details(Ac_no int,Name text ,Age int,phone int,email text)')
        conn.execute("UPDATE details set Name=?,Age=?,phone=?,email=? WHERE Ac_no=?",(name,age,phone,email,Ac_no))
        conn.commit()
        conn.close()
        A.delete(0,END)
        n.delete(0,END)
        a.delete(0,END)
        p.delete(0,END)
        e.delete(0,END)
        
        
    def delete_account(self,A):
        Ac_no=A.get()
        conn=s.connect('ravi.db')
        conn.execute("DELETE FROM details WHERE Ac_No=?",(Ac_no,))
        conn.commit()
        conn.close()
        A.delete(0,END)
        
    def deposit_money(self,A,d_m):
        Ac_no=A.get()
        d=int(d_m.get())
        #print(d,d_m)
        conn=s.connect('ravi.db')
        conn_cur=conn.cursor()
        conn_cur.execute("SELECT Balance FROM details WHERE Ac_NO=?",(Ac_no,))
        l=conn_cur.fetchone()
        #print(l,d,l[0])
        d=d+l[0]
        conn.execute("UPDATE details set Balance=? WHERE Ac_NO=?",(d,Ac_no))
        conn.commit()
        conn.close()
        A.delete(0,END)
        d_m.delete(0,END)

    def withdraw_money(self,A,w_m):
        Ac_no=A.get()
        w=int(w_m.get())
        conn=s.connect('ravi.db')
        conn_cur=conn.cursor()
        conn_cur.execute("SELECT Balance FROM details WHERE Ac_NO=?",(Ac_no,))
        l=conn_cur.fetchone()
        if l[0]>=w:
            w= l[0]-w
            conn.execute("UPDATE details set Balance=? WHERE Ac_NO=?",(w,Ac_no))
            conn.commit()
        else:
            messagebox.showinfo('acc_detail','you have not sufficient balance')
        
        conn.close()
        A.delete(0,END)
        w_m.delete(0,END)

    def view_account(self):
        conn=s.connect('ravi.db')
        conn_cur=conn.cursor()
        conn_cur.execute('SELECT * FROM details')
        info=conn_cur.fetchall()
        conn.close()
        return info

    def search_account(self,A=0):
        Ac_no=A.get()
        conn=s.connect('ravi.db')
        conn_cur=conn.cursor()
        conn_cur.execute('SELECT Ac_no,Name,Age,phone,email,Balance  FROM details WHERE Ac_no=?',(Ac_no,))
        info=conn_cur.fetchone()
        conn.close()
        A.delete(0,END)
        return info
        
            
