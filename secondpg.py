from tkinter import *
from tkinter.ttk import Combobox

w = Tk()
w.geometry("900x700")
w['background']='#bf80ff'

f1 = Frame(w,width = 100,height = 100,background = '#E0F1F0',highlightthickness = 3)
f1.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=1)

admin = Label(f1,text="Admin",fg="black",bg='#E0F1F0', font=("Arial Bold", 50))
admin.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=1)

f2 =Frame(w,width = 700,height = 100,background = '#66a3ff',highlightthickness = 3)
f2.grid(row=0,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

cn = Label(f2,text="Company Name",fg="white",bg="#A6CBCB",font=("Arial Bold", 50))
cn.grid(row=0,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

f3 =Frame(w,background = '#6EB69E',highlightthickness = 3)
f3.grid(row=1,column=0,ipadx = 1,ipady=1,padx=1,pady=1)

db = Button(f3,text="Dashboard",fg="white",bg="#726F71", font=("Arial Bold", 20),  width = 9)
db.grid(row=1,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
q  = Button(f3,text="Queries",fg="white",bg="#726F71", font=("Arial Bold", 20),  width = 9)
q.grid(row=2,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
login = Button(f3,text="Login",fg="white",bg="#726F71", font=("Arial Bold", 20),  width = 9)
login.grid(row=3,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
b = Label(f3,text="",bg="#6EB69E", font=("Arial Bold", 20))
b.grid(row=4,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

b1 = Label(f3,text="",bg="#6EB69E", font=("Arial Bold", 20))
b1.grid(row=5,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
logout = Button(f3,text="Logout",fg="white",bg="#ff4d4d", font=("Arial Bold", 20),  width = 9)
logout.grid(row=6,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

quit = Button(f3,text="Quit",fg="white",bg="#e60000", font=("Arial Bold", 20),  width = 9)
quit.grid(row=7,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

f4 =Frame(w,background = '#6EB69E',highlightthickness = 3)
f4.grid(row=1,column=1,ipadx = 1,ipady=1,padx=1,pady=1)
t1 = Text(f4,height=2,width=70)
t1.grid(row=1, column=0)
t1.insert(END,"Query -")
t2 = Text(f4,height=2,width=70)
t2.grid(row=2, column=0)
t3 =Text(f4,height=2,width=70)
t3.grid(row=3, column=0)
t4 = Text(f4,height=2,width=70)
t4.grid(row=4, column=0)
t5 = Text(f4,height=2,width=70)
t5.grid(row=5, column=0)
t6 = Text(f4,height=2,width=70)
t6.grid(row=6, column=0)
t7 = Text(f4,height=2,width=70)
t7.grid(row=7, column=0)
t8 = Text(f4,height=2,width=70)
t8.grid(row=8, column=0)
t9 = Text(f4,height=2,width=70)
t9.grid(row=9, column=0)
t0 = Text(f4,height=2,width=70)
t0.grid(row=10, column=0)
t10 = Text(f4,height=2,width=70)
t10.grid(row=11, column=0)
t11 = Text(f4,height=2,width=70)
t11.grid(row=12, column=0)
t2.insert(END,"Query -")
t3.insert(END,"Query -")
t4.insert(END,"Query -")
t5.insert(END,"Query -")
t6.insert(END,"Query -")
t7.insert(END,"Query -")
t8.insert(END,"Query -")
t9.insert(END,"Query -")
t0.insert(END,"Query -")
t10.insert(END,"Query -")
t11.insert(END,"Query -")



w.mainloop()