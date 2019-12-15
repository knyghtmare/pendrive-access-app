from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("Passkey App")
master.geometry("300x300")

pendrive_in = IntVar()
pendrive_in.set(0)

def unlock():
    global pendrive_in, label1, label2
    value = pendrive_in.get()
    
    if value == 1:
        messagebox.showinfo("System Response", "Pendrive has been Inserted. Keyboard and Computer Screen have been unlocked.")
        label1 = Label(master, text = "The Keyboard has been unlocked.")
        label1.grid(row = 3, column = 1, columnspan = 5)
        label2 = Label(master, text = "The Computer Screen has been unlocked.")
        label2.grid(row = 4, column = 1, columnspan = 5)
    elif value == 0:
        messagebox.showinfo("System Response", "Pendrive has been Removed. Keyboard and Computer Screen have been locked.")
        label1 = Label(master, text = "The Keyboard is Locked.")
        label1.grid(row = 3, column = 1, columnspan = 5)
        label2 = Label(master, text = "The Computer Screen is Locked.")
        label2.grid(row = 4, column = 1, columnspan = 5)
    return

frame = LabelFrame(master, text = "Pendrive Access App", height = 300, width = 300, padx = 10, pady = 10)
frame.grid(row = 0, column = 2, columnspan = 5, rowspan = 6)

label0 = Label(master, text = "Insert Pendrive Here")
label0.grid(row = 1, column = 1, columnspan = 5)

quit_btn = Button(master, text = "Quit", padx = 10, pady = 10, command = master.quit, fg = "orange", highlightbackground = "black")
quit_btn.grid(row = 5, column = 1, columnspan = 5)

pendrive_checkbox = Checkbutton(master, text = "Pendrive", variable = pendrive_in, command = unlock)
pendrive_checkbox.grid(row = 2, column = 1, columnspan = 5)

label1 = Label(master, text = "The Keyboard is Locked.")
label1.grid(row = 3, column = 1, columnspan = 5)
label2 = Label(master, text = "The Computer Screen is Locked.")
label2.grid(row = 4, column = 1, columnspan = 5)

master.mainloop()