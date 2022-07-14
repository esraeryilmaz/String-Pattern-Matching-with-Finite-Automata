# User Interface implementation

import pattern_matching
from tkinter import *

root = Tk() 
root.geometry("900x600")
root.configure(bg="azure")

root.title("PATTERN MATCHING") 
Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP)

f1 = Frame(root, width =1600, height = 100, relief = SUNKEN) 
f1.configure(bg = "azure")
f1.pack(side = LEFT)

lblInfo = Label(Tops, font = ('helvetica', 30, 'bold'),text="String Pattern Matching with Finite Automata", fg = "Black", bd = 10, anchor='w') 
lblInfo.grid(row = 0, column = 0)
lblInfo.configure(bg = "azure")

str_ip = StringVar() 
pattern_ip = StringVar() 
index_op = StringVar()

def qExit(): 
	root.destroy()

def Reset():
	str_ip.set("")
	pattern_ip.set("")
	index_op.set("")

lblReference = Label(f1, font = ('arial', 18, 'bold'), text = "Enter the string : ", bd = 16, anchor = "w") 
lblReference.grid(row = 1, column = 0) 
lblReference.configure(bg = "azure")

txtReference = Entry(f1, font = ('arial', 18, 'bold'), textvariable = str_ip, bd = 10, insertwidth = 4, bg = "bisque", justify = 'right') 
txtReference.grid(row = 1, column = 1)

lbldestin = Label(f1, font = ('arial', 18, 'bold'), text = "Enter pattern to find : ", bd = 16, anchor = "w") 
lbldestin.grid(row = 3, column = 0)
lbldestin.configure(bg = "azure")

txtdestin = Entry(f1, font = ('arial', 18, 'bold'),textvariable = pattern_ip, bd = 10, insertwidth = 4, bg = "bisque", justify = 'right') 
txtdestin.grid(row = 3, column = 1) 

lblkey = Label(f1, font = ('arial', 18, 'bold'), text = "Pattern found at index position : ", bd = 16, anchor = "w") 
lblkey.grid(row = 5, column = 0) 
lblkey.configure(bg = "azure")

txtkey = Entry(f1, font = ('arial', 18, 'bold'), textvariable = index_op, bd = 10, insertwidth = 4,bg = "bisque", justify = 'right') 
txtkey.grid(row = 5, column = 1) 


# This function calls the pattern matching algorithms function which is called search().
def Find():
	if(len(str_ip.get()) == 0):
		index_op.set("Please enter string !")
		return
	elif(len(pattern_ip.get()) == 0):
		index_op.set("Please enter pattern !")
		return

	# resultList keeps the result index of the searched pattern.
	resultList = []
	resultList = pattern_matching.searchPattern(pattern_ip.get(), str_ip.get())

	if(len(resultList) == 0):
		index_op.set("No pattern found !")
		print("No pattern found !")
		return
	index_op.set(str(resultList))


# Defining all of the buttons on the interface
btnFind = Button(f1, padx = 16, pady = 8, bd = 8, fg = "black", font = ('arial', 24, 'bold'),
			width = 10, text = "FIND ! ", bg = "DarkOliveGreen3", command = Find).grid(row = 7, column = 1)
btnReset = Button(f1, padx = 16, pady = 8, bd = 8, fg = "white", font = ('arial', 16, 'bold'),
			width = 7, text = "RESET", bg = "coral3", command = Reset).grid(row = 10, column = 0)
btnExit = Button(f1, padx = 16, pady = 8, bd = 8,fg = "white", font = ('arial', 16, 'bold'),
			width = 7, text = "EXIT", bg = "coral4",command = qExit).grid(row = 12, column = 0)
root.mainloop()
