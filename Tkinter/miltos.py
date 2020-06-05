from tkinter import *
import tkinter as tk
root = tk.Tk()
frame_1 = Frame(root)
root.title('background image')
fname = "img/login.png"
bg_image = tk.PhotoImage(file=fname)
w = bg_image.width()
h = bg_image.height()
root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')
entry_1 = Entry(root,show="*")
entry_2 = Entry(root)
entry_1.place(relx = 0.5, rely = 0.65, anchor = CENTER)
entry_2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn1 = tk.Button(cv,bg="BLACK",fg="WHITE", text="Login", width=15)
btn1.place(relx = 0.5, rely = 0.75, anchor = CENTER)
btn1 = tk.Button(cv,bg="BLACK",fg="WHITE", text="Back", width=15)
btn1.place(relx = 0.5, rely = 0.83, anchor = CENTER)

root.mainloop()