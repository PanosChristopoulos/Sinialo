from tkinter import * 
root=Tk()
label_1 = Label(root,text="money:")
label_2 = Label(root,text="days:")
label_3 = Label(root,text="people:")
entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
photo_1 = PhotoImage(file = "a.png")
label_0=Label(root,image=photo_1) 
label_0.pack()

label_1.pack()
entry_1.pack()
label_2.pack()
entry_2.pack() 
label_3.pack()
entry_3.pack()
photo_2 = PhotoImage(file = "aa.png")
label_4=Label(root,image=photo_2) 
label_4.pack()

mainloop() 