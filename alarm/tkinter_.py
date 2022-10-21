from tkinter import *
from tkinter.ttk import *
import datetime


window = Tk()
window.geometry("800x135")
window.minsize(width=800, height=135)

data = Label(window, text="0", font=("Arial", 79))
data.grid(row=0, column=0, pady=5, padx=5)


def update():
    # print(f"{times_} and {type__}")
    # if times_ > 0 and type__ is not "":
    time = datetime.datetime.now().time()
    # data_ = time.hour if type__ == "hour" else time.minute
    # data_ += times_
    data['text'] = time
    # if time.minute == data_:
    #     data['text'] = "Done !!!"
    #     return
    data.after(500, update)


# times = [
#     "",
#     "hour",
#     "minute",
# ]
# ch = Label(window, text="Choose type : ")
# ch.grid(row=0, column=1, padx=10, pady=10)
# code_var = StringVar()
# code = OptionMenu(window, code_var, *times)
# code.grid(row=0, column=2, padx=10, pady=10, columnspan=5)
#
# type__ = code_var.get()
#
# en = Label(window, text=f"Enter time limit : ")
# en.grid(row=1, column=1, padx=10, pady=10)
# h = IntVar()
# get = Entry(window, textvariable=h)
# get.grid(row=1, column=2, padx=10, pady=10, columnspan=5)
#
# times_ = h.get()
#
# btn = Button(window, text="Start", command=update)
# btn.grid(row=2, column=1, columnspan=5, padx=10, pady=10,)

update()

window.mainloop()
