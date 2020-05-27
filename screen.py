 
from tkinter import * 
root=Tk()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
label_1 = Label(root, text="SINIALO ")
label_2 = Label(root, text="once a year go someplace you have never been before->Dalai Lama")
photo = PhotoImage(file = "aaa.png")
label_3=Label(root,image=photo) 
button1 = Button(bottomFrame,text="Login",fg="purple")
button2 = Button(bottomFrame,text="Register",fg="purple")
photo_1 = PhotoImage(file = "a.png")
label_0 = Label(root,image=photo_1)
label_0.pack()
label_1.pack()
label_2.pack()
label_3.pack() 
button1.pack(side=LEFT)
button2.pack(side=LEFT)   

                   
mainloop() 
  















