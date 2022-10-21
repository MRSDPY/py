from tkinter import *
from tkinter.ttk import *

tk = Tk()
tk.maxsize(width=300, height=170)

def click():
	pass

btn1 = Button(tk, text="-", width=10, command=click)
btn1.grid(row=0, column=0, padx=10, pady=10)

btn2 = Button(tk, text="-", width=10, command=click)
btn2.grid(row=0, column=1, padx=10, pady=10)

btn3 = Button(tk, text="-", width=10, command=click)
btn3.grid(row=0, column=2, padx=10, pady=10)

btn4 = Button(tk, text="-", width=10, command=click)
btn4.grid(row=1, column=0, padx=10, pady=10)

btn5 = Button(tk, text="-", width=10, command=click)
btn5.grid(row=1, column=1, padx=10, pady=10)

btn6 = Button(tk, text="-", width=10, command=click)
btn6.grid(row=1, column=2, padx=10, pady=10)

btn7 = Button(tk, text="-", width=10, command=click)
btn7.grid(row=2, column=0, padx=10, pady=10)

btn8 = Button(tk, text="-", width=10, command=click)
btn8.grid(row=2, column=1, padx=10, pady=10)

btn9 = Button(tk, text="-", width=10, command=click)
btn9.grid(row=2, column=2, padx=10, pady=10)


tk.mainloop()
