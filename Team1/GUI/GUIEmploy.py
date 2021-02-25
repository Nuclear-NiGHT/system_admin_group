from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox


root = Tk()
root.title("Login")


def default():
    messagebox.showerror(message = "not implemented")

def openLoginPage():
    print("login")

    def checkPassword():
        username = textName.get("1.0", 'end-1c')
        password = textPass.get("1.0", 'end-1c')

        if username == "1":
            if password == "2":
             openAdminMainPage()
 
        else:
            messagebox.showerror(message = "Wrong Credentials")
            print("error")

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

    btnLogin = Button(root, text = "Admin Log-in", font = "MyFont", command = checkPassword)
    btnLogin.grid(column = 3, row = 3)

    btnNonPassLogin = Button(root, text = "User Log-in", font = "MyFont", command = openUserMainPage)
    btnNonPassLogin.grid(column = 3, row = 4)


def openAdminMainPage():

    windowDash = Toplevel()
    windowDash.title("Dashboard")

    windowDash.geometry("900x700")
    windowDash['background']='#B9E5E1'

    #Main Window
    pageTitle = Frame(windowDash,width = 100,height = 100,background = '#E0F1F0',highlightthickness = 3)
    buttonFrame = Frame(windowDash,background = '#D183E7',highlightthickness = 3)
    companyLabelFrame = Frame(windowDash,width = 700,height = 100,background = '#A6CBCB',highlightthickness = 3)

    buttonFrame.grid(row=1,column=0,ipadx = 1,ipady=1,padx=1,pady=1)
    pageTitle.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=1)
    companyLabelFrame.grid(row=0,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

    #Page Label
    adminLabel = Label(pageTitle,text="Admin",fg="black",bg='#E0F1F0', font=("Arial Bold", 50))

    adminLabel.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=1)

    #Company Label
    companyLabel = Label(companyLabelFrame,text="Company Name",fg="yellow",bg="#A6CBCB",font=("Arial Bold", 50))

    companyLabel.grid(row=0,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

    #Left Buttons
    buttonLogout = Button(buttonFrame,text="Logout",fg="white",bg="#EE0B80", font=("Arial Bold", 20),  width = 9, command = windowDash.destroy)
    buttonQuit = Button(buttonFrame,text="Quit",fg="white",bg="#EE0B80", font=("Arial Bold", 20),  width = 9, command = root.destroy)
    
    buttonLogout.grid(row=6,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
    buttonQuit.grid(row=7,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

    #Main Body
    bodyFrame = Frame(windowDash,background = '#B9E5E1',highlightthickness = 3)
    labelSubmission = Label(bodyFrame,text="ID Number",fg="white",bg='#B9E5E1', font=("Arial Bold", 20))

    textName = Text(bodyFrame, width = 20, height = 1)
    textName.grid(column = 3, row = 1)

    combo = Combobox(bodyFrame)
    combo['values']= ("Option1", "Option2", "Option3", "Option4", "Option5")
    combo.current(1) #set the selected item

    textBox = Text(bodyFrame, width = 30, height = 20)
    textBox.grid(row = 1, column = 1)

    labelSelect = Label(bodyFrame,text="Option Select:",fg="white",bg='#B9E5E1', font=("Arial Bold", 20))

    textName.grid(column=1, row=0)
    labelSubmission.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=10)
    labelSelect.grid(row=3,column=0,ipadx = 0,ipady=0,padx=1,pady=0)
    bodyFrame.grid(row=1,column=1,ipadx = 1,ipady=1,padx=1,pady=1)

    combo.grid(row = 3,column = 1, ipady = 0, pady = 0)

    def saveToFile():

        file = open("saveOutput.txt", 'a')
        file.write("-----------------------------------\n")
        file.write("STAFF ID: ")
        file.write(textName.get("1.0", 'end-1c'))
        file.write("\n\n")
    
        file.write("REQUIREMENT: ")
        file.write(combo.get())
        file.write("\n\n")
    
        file.write("NOTE: ")
        file.write(textBox.get("1.0", 'end-1c'))
        file.write("\n")
        file.write("-----------------------------------\n")

    
    submit = Button(bodyFrame,text="Submit",fg="white",bg="#B9E5E1", font=("Arial Bold", 10), command = saveToFile)
    submit.grid(row=8,column=2,ipadx = 10,ipady=10,padx=1,pady=1)

def openUserMainPage():
    windowDash = Toplevel()
    windowDash.title("Dashboard")

    windowDash.geometry("900x700")
    windowDash['background']='#B9E5E1'

    #Main Window
    pageTitle = Frame(windowDash,width = 100,height = 100,background = '#E0F1F0',highlightthickness = 3)
    buttonFrame = Frame(windowDash,background = '#D183E7',highlightthickness = 3)
    companyLabelFrame = Frame(windowDash,width = 700,height = 100,background = '#A6CBCB',highlightthickness = 3)

    buttonFrame.grid(row=1,column=0,ipadx = 1,ipady=1,padx=1,pady=1)
    pageTitle.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=1)
    companyLabelFrame.grid(row=0,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

    #Page Label
    adminLabel = Label(pageTitle,text="User",fg="black",bg='#E0F1F0', font=("Arial Bold", 50))

    adminLabel.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=1)

    #Company Label
    companyLabel = Label(companyLabelFrame,text="Company Name",fg="yellow",bg="#A6CBCB",font=("Arial Bold", 50))

    companyLabel.grid(row=0,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

    #Left Buttons
    buttonLogout = Button(buttonFrame,text="Logout",fg="white",bg="#EE0B80", font=("Arial Bold", 20),  width = 9, command = windowDash.destroy)
    buttonQuit = Button(buttonFrame,text="Quit",fg="white",bg="#EE0B80", font=("Arial Bold", 20),  width = 9, command = root.destroy)
    
    buttonLogout.grid(row=6,column=1,ipadx = 10,ipady=10,padx=1,pady=1)
    buttonQuit.grid(row=7,column=1,ipadx = 10,ipady=10,padx=1,pady=1)

    #Main Body
    bodyFrame = Frame(windowDash,background = '#B9E5E1',highlightthickness = 3)
    labelSubmission = Label(bodyFrame,text="ID Number",fg="white",bg='#B9E5E1', font=("Arial Bold", 20))

    textName = Text(bodyFrame, width = 20, height = 1)
    textName.grid(column = 3, row = 1)

    combo = Combobox(bodyFrame)
    combo['values']= ("Option1", "Option2", "Option3", "Option4", "Option5")
    combo.current(1) #set the selected item

    textBox = Text(bodyFrame, width = 30, height = 20)
    textBox.grid(row = 1, column = 1)

    labelSelect = Label(bodyFrame,text="Option Select:",fg="white",bg='#B9E5E1', font=("Arial Bold", 20))

    textName.grid(column=1, row=0)
    labelSubmission.grid(row=0,column=0,ipadx = 10,ipady=10,padx=1,pady=10)
    labelSelect.grid(row=3,column=0,ipadx = 0,ipady=0,padx=1,pady=0)
    bodyFrame.grid(row=1,column=1,ipadx = 1,ipady=1,padx=1,pady=1)

    combo.grid(row = 3,column = 1, ipady = 0, pady = 0)

    def saveToFile():
        messagebox.showerror(message = "Insufficient Permissions")

    
    submit = Button(bodyFrame,text="Submit",fg="white",bg="#B9E5E1", font=("Arial Bold", 10), command = saveToFile)
    submit.grid(row=8,column=2,ipadx = 10,ipady=10,padx=1,pady=1)
   




openLoginPage()

root.mainloop()