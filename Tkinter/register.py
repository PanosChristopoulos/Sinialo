from tkinter import *
import tkinter as tk
root = tk.Tk()
frame_1 = Frame(root)
root.title('background image')
fname = "img/register.png"
bg_image = tk.PhotoImage(file=fname)
w = bg_image.width()
h = bg_image.height()
root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')
entry_1 = Entry(root,show="*")
entry_2 = Entry(root)
entry_3 = Entry(root)
entry_1.place(relx = 0.31, rely = 0.58, anchor = CENTER)
entry_2.place(relx = 0.31, rely = 0.69, anchor = CENTER)
entry_3.place(relx = 0.31, rely = 0.46, anchor = CENTER)


btn1 = tk.Button(cv,bg="GREEN",fg="WHITE", text="Register")
btn1.place(relx = 0.7, rely = 0.73, anchor = CENTER)
root.mainloop()
