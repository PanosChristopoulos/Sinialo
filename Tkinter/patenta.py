from  tkinter import *
from PIL import ImageTk,Image
root = Tk()

root.geometry("375x650")
root.resizable(False,False)

image3 = ImageTk.PhotoImage(Image.open("img/bg.png"))
label3 = Label(image = image3,bg="CadetBlue1")
label3.place(x=0,y=0,relwidth=1, relheight=1)

popularButtton = Button(root, text= "Σύνδεση", padx=100, pady=25,bg="#011534",fg="white")
popularButtton.place(x=63,y=442)


popularButtton = Button(root, text= "Εγγραφή", padx=100, pady=25,bg="#011534",fg="white")
popularButtton.place(x=63,y=547)

root.mainloop()