from tkinter import *
from tkinter.ttk import Combobox

w = Tk()
w.geometry("900x700")
w['background']='#B9E5E1'

f1 = Frame(w,width = 100,height = 100,background = '#E0F1F0',highlightthickness = 3)
f1.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=1)

admin = Label(f1,text="Admin",fg="black",bg='#E0F1F0', font=("Arial Bold", 50))
admin.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=1)

f2 =Frame(w,width = 700,height = 100,background = '#A6CBCB',highlightthickness = 3)
f2.grid(row=0,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

cn = Label(f2,text="Company Name",fg="yellow",bg="#A6CBCB",font=("Arial Bold", 50))
cn.grid(row=0,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

f3 =Frame(w,background = '#D183E7',highlightthickness = 3)
f3.grid(row=1,column=0,ipadx = 1,ipady=1,padx=1,pady=1)

db = Button(f3,text="Dashboard",fg="white",bg="#EE0B80", font=("Arial Bold", 20),  width = 9)
db.grid(row=1,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
q  = Button(f3,text="Queries",fg="white",bg="#EE0B80", font=("Arial Bold", 20),  width = 9)
q.grid(row=2,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
login = Button(f3,text="Login",fg="white",bg="#EE0B80", font=("Arial Bold", 20),  width = 9)
login.grid(row=3,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
b = Label(f3,text="",bg="#D183E7", font=("Arial Bold", 20))
b.grid(row=4,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

b1 = Label(f3,text="",bg="#D183E7", font=("Arial Bold", 20))
b1.grid(row=5,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
logout = Button(f3,text="Logout",fg="white",bg="#EE0B80", font=("Arial Bold", 20),  width = 9)
logout.grid(row=6,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

quit = Button(f3,text="Quit",fg="white",bg="#EE0B80", font=("Arial Bold", 20),  width = 9)
quit.grid(row=7,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

f4 =Frame(w,background = '#B9E5E1',highlightthickness = 3)
f4.grid(row=1,column=1,ipadx = 1,ipady=1,padx=1,pady=1)

qs = Label(f4,text="Query Submission",fg="white",bg='#B9E5E1', font=("Arial Bold", 20))
qs.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=1)
combo = Combobox(f4)
combo['values']= (1, 2, 3, 4, 5)
combo.current(1) #set the selected item
combo.grid(column=1, row=0)
notes = Text(f4,height=20,width=30).grid(row=1, column=1)
submit = Button(f4,text="Submit",fg="white",bg="#B9E5E1", font=("Arial Bold", 10))
submit.grid(row=8,column=2,ipadx = 10,ipady=10,padx=1,pady=1)


w.mainloop()