from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Login")


def default():
    messagebox.showerror(message = "not implemented")

def checkPassword():
    username = textName.get("1.0", 'end-1c')
    password = textPass.get("1.0", 'end-1c')

    if username == "1":
        if password == "2":
            openMainPage()
 
    else:
        messagebox.showerror(message = "Wrong Credentials")
        print("error")


def openMainPage():

    global canvas
    global lavelName

    windowLog = Toplevel()
    windowLog.title("Access Log")

    logCanvas = Canvas(root, width=100, height=150)
    logCanvas.grid(columnspan=12)
    windowLog.geometry('450x300')

    logLabelName = Label(windowLog, text="testtest:", font = ("MyFont", 12))
    logLabelName.grid(column=2, row=1, columnspan = 11)
    logAdminButton = Button(windowLog, text = "Admin", font = "MyFont", command = default)
    logAdminButton.grid(column = 1, row = 1)
    logQuriesButton = Button(windowLog, text = "Quries", font = "MyFont", command = default)
    logQuriesButton.grid(column = 1, row = 2)
    logLoginsButton = Button(windowLog, text = "Log-ins", font = "MyFont", command = default)
    logLoginsButton.grid(column = 1, row = 3)
    logLogoutButton = Button(windowLog, text = "Log Out", font = "MyFont", command = default)
    logLogoutButton.grid(column = 1, row = 4)
    logQuitButtton = Button(windowLog, text = "Quit", font = "MyFont", command = default)
    logQuitButtton.grid(column = 1, row = 5)


    
canvas = Canvas(root, width=100, height=150)
canvas.grid(columnspan=5)
root.geometry('450x300')

logo = Image.open('logo.gif')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=2, row=0)

labelTitle = Label(root, text="Company Name", font = ("MyFont", 44))
labelTitle.grid(column=3, row=0)


labelName = Label(root, text="Username:", font = ("MyFont", 12))
labelName.grid(column=2, row=1)

textName = Text(width = 30, height = 1)
textName.grid(column = 3, row = 1)

labelPass = Label(root, text="Password:", font = ("MyFont", 12))
labelPass.grid(column=2, row=2)

textPass = Text(width = 30, height = 1)
textPass.grid(column = 3, row = 2)

btnLogin = Button(root, text = "Log in", font = "MyFont", command = checkPassword)
btnLogin.grid(column = 3, row = 3)



root.mainloop()