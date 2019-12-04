from tkinter import *
window = Tk()
window.title("Proiect final")
window.geometry ("800x400")



label1=Label(window,text="Name",font=("bold",10), pady=20)
label1.grid(row=1,column=0,)


label2=Label(window,text="CNP",font=("bold",10), pady=20)
label2.grid(row=2,column=0)

label3=Label(window,text="Salariu",font=("bold",10), pady=20)
label3.grid(row=3,column=0)

name_text=StringVar()
entry1=Entry(window, textvariable=name_text)
entry1.grid(row=1,column=1,sticky=W)
entry1.insert(0,"Enter your name: ")

CNP_text=StringVar()
entry2=Entry(window,textvariable=CNP_text)
entry2.grid(row=2,column=1,sticky=W)
entry2.insert(0,"Enter your CNP: ")

salariu=StringVar()
entry3=Entry(window,textvariable=salariu)
entry3.grid(row=3,column=1,sticky=W)
entry3.insert(0,"Enter your Salariu: ")


b1=Button(window,text="add entry", width=12)
b1.grid(row=1, column=3)

b2=Button(window,text="delete entry", width=12)
b2.grid(row=1, column=4)

b3=Button(window,text="modify entry", width=12)
b3.grid(row=2, column=3)

b4=Button(window,text="modify salariu", width=12)
b4.grid(row=2, column=4)

b5=Button(window,text="view all", width=12)
b5.grid(row=3, column=3)

b6=Button(window,text="-5% ", width=12)
b6.grid(row=3, column=4)

listbox=Listbox(window,height=10,width=59)
listbox.grid(row=4,column=1, rowspan =3, columnspan=2)

scrollbar=Scrollbar(window)
scrollbar.grid(row=4,column=0, sticky= 'ns',rowspan =6)

listbox.configure(yscrollcommand=scrollbar.set) #connect scrollbar 
scrollbar.configure(command=listbox.yview)

# name_text=StringVar()
# entry4=Entry(window,textvariable=name_text)
# entry4.grid(row=0,column=0)


window.mainloop()