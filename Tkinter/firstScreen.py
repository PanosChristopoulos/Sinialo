from  tkinter import *
from PIL import ImageTk,Image
import loginScreen1
import registerScreen
root = Tk()

root.geometry("375x650")
root.resizable(False,False)


def loginFrame():
	root.destroy()
	loginScreen1.main()

def registerFrame():
	root.destroy()
	registerScreen.main()


image3 = ImageTk.PhotoImage(Image.open("img/bg.png"))
label3 = Label(image = image3,bg="CadetBlue1")
label3.place(x=0,y=0,relwidth=1, relheight=1)

popularButtton = Button(root, text= "Σύνδεση", padx=100, pady=25,bg="#011534",fg="white",command=loginFrame)
popularButtton.place(x=63,y=442)


popularButtton = Button(root, text= "Εγγραφή", padx=100, pady=25,bg="#011534",fg="white",command=registerFrame)
popularButtton.place(x=63,y=547)

root.mainloop()