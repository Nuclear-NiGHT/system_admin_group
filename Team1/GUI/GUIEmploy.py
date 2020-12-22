import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=5)

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


root.mainloop()