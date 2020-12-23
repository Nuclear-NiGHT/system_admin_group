import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

root = tk.Tk()
root.title("Login")


def openMainPage():
    windowLog = tk.Toplevel(root)
    windowLog.title("Access Log")
    windowLog.geometry("450x300")


def checkPassword():
    username = textName.get("1.0", 'end-1c')
    password = textPass.get("1.0", 'end-1c')

    print(username)
    print(password)

    if username == "admin":
        if password == "admin1":
            openMainPage()

            
    else:
        messagebox.showerror(message = "Wrong Credentials")
        print("error")

    
canvas = tk.Canvas(root, width=100, height=150)
canvas.grid(columnspan=5)
root.geometry('450x300')

logo = Image.open('logo.gif')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=2, row=0)

labelTitle = tk.Label(root, text="Company Name", font = ("MyFont", 44))
labelTitle.grid(column=3, row=0)


labelName = tk.Label(root, text="Username:", font = ("MyFont", 12))
labelName.grid(column=2, row=1)

textName = tk.Text(width = 30, height = 1)
textName.grid(column = 3, row = 1)

labelPass = tk.Label(root, text="Password:", font = ("MyFont", 12))
labelPass.grid(column=2, row=2)

textPass = tk.Text(width = 30, height = 1)
textPass.grid(column = 3, row = 2)

btnLogin = tk.Button(root, text = "Log in", font = "MyFont", command = checkPassword)
btnLogin.grid(column = 3, row = 3)



root.mainloop()