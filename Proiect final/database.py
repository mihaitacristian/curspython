# from tkinter import *

# root = Tk()
# # Create a lable Widget
# myLabel = Label(root, text="Hello World!")
# #Shovind in to the screen 
# myLabel.pack()

# root.mainloop()

############################### Using grid function 

# from tkinter import *

# root = Tk()
# # Create a lable Widget
# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="Hello World!")
# #Shovind in to the screen 
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)

# root.mainloop()

############################### 
# from tkinter import *

# root = Tk()

# def myClick():
#     myLabel = Label(root, text="Look! Iclicked a Button!!")
#     myLabel.pack()

# myButton =Button(root, text="Click me!", command=myClick, fg="blue", bg="#000000")   #fb -culoarea scrisului din buton bg-culoarea butonului
# myButton.pack()

# root.mainloop()

############################ Create Input Fields With TKinter and Python

# from tkinter import *

# root = Tk()

# e = Entry(root, width=50)
# e.pack()
# e.insert(0,"Enter your name: ") # insert a text 

# def myClick():
#     myLabel = Label(root, text="Hello " + e.get()) # e.get() is get function
#     myLabel.pack()

# myButton =Button(root, text="Click me!", command=myClick)  
# myButton.pack()

# root.mainloop()
# ##############Create calculator


from tkinter import *

root = Tk()
root.title("Simple Calculator") # The title of the GUI interface

e = Entry(root, width=35, borderwidth= "5")
e.grid(row=0, column=0,columnspan=3, padx=10, pady= 10)  #columnspan nr de coloane

# e.insert(0,"Enter your name: ") # insert a text 

def button_click(number):
    #e.delete(0,END)  # delete what is in the box
    current=e.get()
    e.delete(0, END)
    e.insert(0 , str(current) + str(number)) # insert 

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num=int(first_number)
    e.delete(0, END)

def button_equal(): 
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "divison":
        e.insert(0, f_num / int(second_number))
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num=int(first_number)
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num=int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num=int(first_number)
    e.delete(0, END)

#Define buttons
button_1 =Button(root, text="1", padx=40, pady=20,command=lambda:button_click(1))
button_2 =Button(root, text="2", padx=40, pady=20,command=lambda:button_click(2))  
button_3 =Button(root, text="3", padx=40, pady=20,command=lambda:button_click(3))  
button_4 =Button(root, text="4", padx=40, pady=20,command=lambda:button_click(4))  
button_5 =Button(root, text="5", padx=40, pady=20,command=lambda:button_click(5))  
button_6 =Button(root, text="6", padx=40, pady=20,command=lambda:button_click(6))  
button_7 =Button(root, text="7", padx=40, pady=20,command=lambda:button_click(7))  
button_8 =Button(root, text="8", padx=40, pady=20,command=lambda:button_click(8))  
button_9 =Button(root, text="9", padx=40, pady=20,command=lambda:button_click(9))    
button_0 =Button(root, text="0", padx=40, pady=20,command=lambda:button_click(0))
button_add =Button(root, text="+", padx=39, pady=20,command=button_add)
button_equal =Button(root, text="=", padx=91, pady=20,command=button_equal)
button_clear =Button(root, text="Clear", padx=79, pady=20,command=button_clear)
button_subtract =Button(root, text="-", padx=41, pady=20,command=button_subtract)
button_multiply =Button(root, text="*", padx=40, pady=20,command=button_multiply)
button_divide =Button(root, text="/", padx=41, pady=20,command=button_divide)

######Put the buttons on the screen 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2) #columnspan=2 face butonul pe 2 coloane
button_clear.grid(row=4, column=1,columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()