import tkinter as tk
import tkinter.messagebox as mb

root = tk.Tk()
root.geometry("500x300")

tk.Label(root, text="Proiect final", bg="goldenrod", font="bold").pack()
tk.Label(root, text="").pack()

def addFn():
    a = input('Enter your name:')
    mb.showinfo('showinfo', a)

def subtractFn():
    a = int(input('enter first number'))
    b = int(input('enter second number'))
    mb.showinfo('showinfo', a - b)









tk.Button(root, text="Add angajat", bg="SkyBlue1", command=addFn).pack()
tk.Button(root, text="Sterge angajat", bg="SkyBlue1", command=subtractFn).pack()
tk.Button(root, text="Modificara detaliilor unui angajat", bg="SkyBlue1", command=subtractFn).pack()
tk.Button(root, text="Modificarea salariului unui angajat", bg="SkyBlue1", command=subtractFn).pack()
tk.Button(root, text="show angajati", bg="SkyBlue1", command=subtractFn).pack()
tk.Button(root, text="-5%", bg="SkyBlue1", command=subtractFn).pack()
root.mainloop()