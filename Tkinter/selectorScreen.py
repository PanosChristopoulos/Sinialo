from tkinter import *
import tkinter as tk
import resultScreen

budget = 0.1
days = 0.1
people = 0.1

def main():
	

	root = tk.Tk()
	frame_1 = Frame(root)
	root.title('background image')
	fname = "img/selectorscreen.png"

	def resultFrame():
		getAtr()
		root.destroy()
		resultScreen.main()
	def resultScreenPopularFrame():
		root.destroy()
		resultScreenPopular.main()
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
	entry_1.place(width=100, relx = 0.3, rely = 0.43, anchor = CENTER)
	entry_2.place(width=100, relx = 0.52, rely = 0.43, anchor = CENTER)
	entry_3.place(width=100, relx = 0.75, rely = 0.43, anchor = CENTER)
	btn1 = tk.Button(cv, text="Submit",bg = "seaGreen3",fg="WHITE",command=resultFrame)
	btn1.place(relx = 0.8, rely = 0.55, anchor = CENTER)

	def getAtr():
		global budget
		budget1 = entry_2.get()
		budget = float(budget1)
		
			
		global days
		days1 = entry_1.get()
		days = float(days1)

		global people
		people1 = entry_3.get()
		people = float(people1)
	

	root.mainloop()

def getDays():
	return budget

def getBudget():
	return days

def getPeople():
	return people

if __name__=="__main__":
    main()