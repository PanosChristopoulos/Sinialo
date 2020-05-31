from tkinter import *
import tkinter as tk
import resultScreen
def main():

	


	root = tk.Tk()
	frame_1 = Frame(root)
	root.title('background image')
	fname = "img/selectorscreen.png"

	def resultFrame():
		root.destroy()
		resultScreen.main()
	
	bg_image = tk.PhotoImage(file=fname)
	w = bg_image.width()
	h = bg_image.height()
	root.geometry("%dx%d+50+30" % (w, h))
	cv = tk.Canvas(width=w, height=h)
	cv.pack(side='top', fill='both', expand='yes')
	cv.create_image(0, 0, image=bg_image, anchor='nw')
	entry_1 = Entry(root,width=100)
	entry_2 = Entry(root,width=100)
	entry_3 = Entry(root,width=100)
	entry_1.place(width=100, relx = 0.52, rely = 0.43, anchor = CENTER)
	entry_2.place(width=100, relx = 0.3, rely = 0.43, anchor = CENTER)
	entry_3.place(width=100, relx = 0.75, rely = 0.43, anchor = CENTER)
	btn1 = tk.Button(cv, text="Submit",bg = "GREEN",fg="WHITE",command=resultFrame)
	btn1.place(relx = 0.8, rely = 0.55, anchor = CENTER)

	

	root.mainloop()

if __name__=="__main__":
    main()