from tkinter import *
from bank_managment_bk import *
#from tkinter import messagebox as m


x=account() #creating object
root=Tk()
def CREATE(): #create function
    root=Tk()
    #root.geometry('500x500')
    root.configure(bg='brown')
    root.title('create account')
    
    #def close():
     #   if m.askyesno('CLOSE','Do you want to close the window'):
      #      root.destroy()
            
    label=Label(root,text='NEW ACCOUNT',font='TImes 16 italic',bg='red')
    label.grid(row=0,column=0,columnspan=10,pady=10)
    label=Label(root,font="Times 16 bold",justify='left',text='AC_NO',fg='red',bg='brown')
    label.grid(column=0,row=1)
    label=Label(root,font="Times 16 bold",justify='left',text='Name',fg='orange',bg='brown')
    label.grid(column=0,row=2)
    label=Label(root,font="Times 16 bold",justify='left',text='Age',fg='orange',bg='brown')
    label.grid(column=0,row=3)
    label=Label(root,font="Times 16 bold",justify='left',text='phone',fg='orange',bg='brown')
    label.grid(column=0,row=4)
    label=Label(root,font="Times 16 bold",justify='left',text='Email',fg='orange',bg='brown')
    label.grid(column=0,row=5)

    entry1=Entry(root,width=20,justify='left',bd=3)
    entry1.grid(column=1,row=1,padx=20)
    entry2=Entry(root,width=20,justify='left',bd=3)
    entry2.grid(column=1,row=2,padx=20)
    entry3=Entry(root,width=20,justify='left',bd=3)
    entry3.grid(column=1,row=3,padx=20)
    entry4=Entry(root,width=20,justify='left',bd=3)
    entry4.grid(column=1,row=4,padx=20)
    entry5=Entry(root,width=20,justify='left',bd=3)
    entry5.grid(column=1,row=5,padx=20)

    b1=Button(root,width=10,bg='orange',text='create',relief=RAISED,cursor='circle')
    b1['command']= lambda :x.create_submit(entry1,entry2,entry3,entry4,entry5) #calling create_submit func
    b1.grid(row=6,column=1,pady=10)

    b2=Button(root,width=10,bg='orange',text='exit',relief=RAISED,cursor='circle',command=root.destroy)
    b2.grid(row=6,column=2,pady=10)

def UPDATE(): #update function
    root=Tk()
    root.configure(bg='brown')
    root.title('update account')

    label=Label(root,text='UPDATE ACCOUNT',font='TImes 16 italic',bg='red')
    label.grid(row=0,column=0,columnspan=10,pady=10)
    label=Label(root,font="Times 16 bold",justify='left',text='AC_NO',fg='white',bg='brown')
    label.grid(column=0,row=1)
    label=Label(root,font="Times 16 bold",justify='left',text='Name',fg='orange',bg='brown')
    label.grid(column=0,row=2)
    label=Label(root,font="Times 16 bold",justify='left',text='Age',fg='orange',bg='brown')
    label.grid(column=0,row=3)
    label=Label(root,font="Times 16 bold",justify='left',text='phone',fg='orange',bg='brown')
    label.grid(column=0,row=4)
    label=Label(root,font="Times 16 bold",justify='left',text='Email',fg='orange',bg='brown')
    label.grid(column=0,row=5)

    entry1=Entry(root,width=20,justify='left',bd=3)
    entry1.grid(column=1,row=1,padx=20)
    entry2=Entry(root,width=20,justify='left',bd=3)
    entry2.grid(column=1,row=2,padx=20)
    entry3=Entry(root,width=20,justify='left',bd=3)
    entry3.grid(column=1,row=3,padx=20)
    entry4=Entry(root,width=20,justify='left',bd=3)
    entry4.grid(column=1,row=4,padx=20)
    entry5=Entry(root,width=20,justify='left',bd=3)
    entry5.grid(column=1,row=5,padx=20)

    b1=Button(root,width=10,bg='orange',text='update',relief=RAISED,cursor='circle')
    b1['command']= lambda :x.update_account(entry1,entry2,entry3,entry4,entry5) #calling update_account func
    b1.grid(row=6,column=1,pady=10)

    b2=Button(root,width=10,bg='orange',text='exit',relief=RAISED,cursor='circle',command=root.destroy)
    b2.grid(row=6,column=2,pady=10)


    root.mainloop()

def DELETE():
    root=Tk()
    root.title('delete account')

    label=Label(root,text='DELETE ACCOUNT',font='TImes 16 italic')
    label.grid(row=0,column=1,columnspan=6)
    label=Label(root,font="Times 16 bold",justify='left',text='AC_NO')
    label.grid(column=0,row=1)

    entry1=Entry(root,width=20,justify='left')
    entry1.grid(column=1,row=1,padx=20)
    
    b1=Button(root,width=10,bg='orange',text='delete',relief=RAISED,cursor='circle')
    b1['command']=lambda:x.delete_account(entry1) #calling delete_acc func
    b1.grid(row=6,column=1,pady=10)

    b2=Button(root,width=10,bg='orange',text='exit',relief=RAISED,cursor='circle',command=root.destroy)
    b2.grid(row=6,column=2,pady=10)

    root.mainloop()
def DEPOSIT():
    root=Tk()

    label=Label(root,text='DEPOSIT MONEY',font='TImes 16 italic bold',fg='orange')
    label.grid(row=0,column=1,columnspan=6)
    label=Label(root,font="Times 16 bold",justify='left',text='AC_NO')
    label.grid(column=0,row=1)
    label=Label(root,font="Times 16 bold",justify='left',text='AMOUNT')
    label.grid(column=0,row=2)

    entry1=Entry(root,width=20,justify='left')
    entry1.grid(column=1,row=1,padx=20)
    entry2=Entry(root,width=20,justify='left')
    entry2.grid(column=1,row=2,padx=20)
        
    b1=Button(root,width=10,bg='orange',text='deposit',relief=RAISED,cursor='circle')
    b1['command']=lambda:x.deposit_money(entry1,entry2) #calling deposit_money func
    b1.grid(row=6,column=1,pady=10)

    b2=Button(root,width=10,bg='orange',text='exit',relief=RAISED,cursor='circle',command=root.destroy)
    b2.grid(row=6,column=2,pady=10)

    root.mainloop()

def WITHDRAW():
    root =Tk()

    label=Label(root,text='WITHDRAW MONEY',font='TImes 16 italic bold',fg='orange')
    label.grid(row=0,column=1,columnspan=6)
    label=Label(root,font="Times 16 bold",justify='left',text='AC_NO')
    label.grid(column=0,row=1)
    label=Label(root,font="Times 16 bold",justify='left',text='WITHDRAW')
    label.grid(column=0,row=2)

    entry1=Entry(root,width=20,justify='left')
    entry1.grid(column=1,row=1,padx=20)
    entry2=Entry(root,width=20,justify='left')
    entry2.grid(column=1,row=2,padx=20)
        
    b1=Button(root,width=10,bg='orange',text='withdraw',relief=RAISED,cursor='circle')
    b1['command']=lambda:x.withdraw_money(entry1,entry2) #calling withdraw_money func
    b1.grid(row=6,column=1,pady=10)

    b2=Button(root,width=10,bg='orange',text='exit',relief=RAISED,cursor='circle',command=root.destroy)
    b2.grid(row=6,column=2,pady=10)

    root.mainloop()

def VIEW():
    info=x.view_account()
    root=Tk()
    frame=Frame(root)
    frame.pack()
    #view_var=StringVar()
    #view_var.set()
       #======heading==========
    label=Label(frame,text='Ac_no',font='times 12 bold',bg='orange')
    label.grid(row=0,column=0)
    label=Label(frame,text='Name',font='times 12 bold',bg='orange')
    label.grid(row=0,column=1)
    label=Label(frame,text='Age',font='times 12 bold',bg='orange')
    label.grid(row=0,column=2)
    label=Label(frame,text='Phone',font='times 12 bold',bg='orange')
    label.grid(row=0,column=3)
    label=Label(frame,text='Email',font='times 12 bold',bg='orange')
    label.grid(row=0,column=4)
    label=Label(frame,text='Balance',font='times 12 bold',bg='orange')
    label.grid(row=0,column=5)
    
    #========content====================
    i=1
    for value in info:
        #print(value,len(value))
        for j in range(len(value)):
            label=Label(frame,text=value[j])
            label.grid(row=i,column=j)
        i+=1
    
        
    root.mainloop()

def SEARCH():
    
    root=Tk()
    
    upper_frame=Frame(root)
    upper_frame.pack(side=TOP)

    lower_frame=Frame(root,pady=15)
    lower_frame.pack(side=BOTTOM)

    label=Label(upper_frame,font='TIMES 14 italic bold',text='SEARCH',fg='orange')
    label.grid(row=0,column=1,columnspan=6)
    label=Label(upper_frame,font="Times 16 bold",justify='left',text='AC_NO')
    label.grid(column=0,row=1)

    entry1=Entry(upper_frame,width=20,justify='left')
    entry1.grid(column=1,row=1,padx=20)

    def f():
        value=x.search_account(entry1)
        #==========heading===========
        label=Label(lower_frame,text='Ac_no',font='times 12 bold',bg='orange')
        label.grid(row=0,column=0)
        label=Label(lower_frame,text='Name',font='times 12 bold',bg='orange')
        label.grid(row=0,column=1)
        label=Label(lower_frame,text='Age',font='times 12 bold',bg='orange')
        label.grid(row=0,column=2)
        label=Label(lower_frame,text='Phone',font='times 12 bold',bg='orange')
        label.grid(row=0,column=3)
        label=Label(lower_frame,text='Email',font='times 12 bold',bg='orange')
        label.grid(row=0,column=4)
        label=Label(lower_frame,text='Balance',font='times 12 bold',bg='orange')
        label.grid(row=0,column=5)

        #=============content================
        for j in range(len(value)):
            label=Label(lower_frame,text=value[j])
            label.grid(row=1,column=j)

        
    #value=x.search_account(entry1.get())

    b1=Button(upper_frame,width=10,bg='orange',text='search',relief=RAISED,cursor='circle')
    b1['command']=f   #calling above function f()
    b1.grid(row=6,column=1,pady=10)

    b2=Button(upper_frame,width=10,bg='orange',text='exit',relief=RAISED,cursor='circle',command=root.destroy)
    b2.grid(row=6,column=2,pady=10)

    
    root.mainloop()
    
    
def DESTROY():
    root.destroy()
    #obj=x.CREATE()
    #obj.root.destroy()

    
# //////////////////////////////////////////////main window////////////////////////////
root.configure(bg='green')
upper_frame=Frame(root,bd=1)
upper_frame.pack(side=TOP)
lower_frame=Frame(root,bg='orange',bd=2)
lower_frame.pack()                                              #consumer transfer national bank
head=Label(upper_frame,width='20',height='3',fg='orange',text='CTNB BANK',font='Times 20 italic',bg='brown',relief=GROOVE)
head.grid(row=0,column=0)
#=======Options=================
option1=Button(lower_frame,text='CREATE',relief=RAISED,borderwidth=3,activebackground='red',command=CREATE)
option1.grid(row=1,column=0)
l=Label(lower_frame,bg='orange',width=2)
l.grid(row=1,column=1)
option2=Button(lower_frame,text='UPDATE AC',relief=RAISED,borderwidth=3,activebackground='red',command=UPDATE)
option2.grid(row=1,column=2)
option3=Button(lower_frame,text='DELETE',relief=RAISED,borderwidth=3,activebackground='red',command=DELETE)
option3.grid(row=3,column=0)
option4=Button(lower_frame,text='VIEW',relief=RAISED,borderwidth=3,activebackground='red',command=VIEW)
option4.grid(row=3,column=2)
option5=Button(lower_frame,text='DEPOSIT',relief=RAISED,borderwidth=3,activebackground='red',command=DEPOSIT)
option5.grid(row=5,column=0)
option6=Button(lower_frame,text='WITHDRAW',relief=RAISED,borderwidth=3,activebackground='red',command=WITHDRAW)
option6.grid(row=5,column=2)
option7=Button(lower_frame,text='SEARCH',relief=RAISED,borderwidth=3,activebackground='red',command=SEARCH)
option7.grid(row=7,column=0)
option8=Button(lower_frame,text='EXIT',relief=RAISED,borderwidth=3,activebackground='red',command=DESTROY)
option8.grid(row=7,column=2)

root.mainloop()

#conn=s.connect('ravi.db')
#rows=conn.execute('SELECT * FROM details')
#for row in rows:
 #   print(row)

 #/////problem//////////////
#password login
#view()
#validate entry

#____concept____:
#Label is generally used to make any single input fill up and for any single line text.
