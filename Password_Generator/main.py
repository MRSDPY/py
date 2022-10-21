from tkinter import *
from tkinter.ttk import *
import random
import string

win = Tk()

upper_ = list(string.ascii_uppercase)
lower_ = list(string.ascii_lowercase)
digit_ = list(string.digits)
special_ = list(string.punctuation)


def list_to_str(li):
    string = ""
    for i in li:
        string += str(i)

    return string


def get_empty_spot(lis):
    n = random.randint(0, len(lis) - 1)

    while lis[n] != "":
        n = random.randint(0, len(lis) - 1)

    return n


def make_better(passData):
    if passData is None:
        return
    return_str = ["" for _ in range(len(passData))]
    string = ""
    replace_word = {
        "a": "@",
        "h": "#",
        "s": "$",
        "i": "!",
        "d": "?",
    }

    for i in range(len(passData)):
        if passData[i].lower() in replace_word:
            return_str[i] = replace_word[passData[i]]
        else:
            return_str[i] = passData[i]

    string = list_to_str(return_str)

    return string


def password():
    user_data = user_word.get()
    user_data = make_better(user_data if user_data is not "" else None)
    length = size.get()
    final_password = ["" for _ in range(length)]
    condition = {
        0: length // 4,
        1: length // 4,
        2: length // 4,
        3: length // 4,
        4: length - ((length // 4) * 4)
    }

    if length >= 8:
        global digit_, upper_, lower_, special_
        random.shuffle(digit_)
        random.shuffle(upper_)
        random.shuffle(lower_)
        random.shuffle(special_)
        for i, v in condition.items():

            for j in range(v):
                if i == 0:
                    final_password[get_empty_spot(final_password)] = random.choice(lower_)
                elif i == 1:
                    final_password[get_empty_spot(final_password)] = random.choice(upper_)
                elif i == 2:
                    final_password[get_empty_spot(final_password)] = random.choice(digit_)
                elif i == 3:
                    final_password[get_empty_spot(final_password)] = random.choice(special_)
                else:
                    final_password[get_empty_spot(final_password)] = random.choice(
                        [random.choice(special_), random.choice(digit_), random.choice(upper_),
                         random.choice(lower_)])
        output.delete('1.0', INSERT)
        output.insert(INSERT, list_to_str(final_password))
    else:
        popup = Tk()
        popup.wm_title("Warning !")
        label = Label(popup, text="You can't create password with less than 8 char.")
        label.pack(side="top", fill="x", pady=10, padx=10)
        Ok = Button(popup, width=20, text="Ok", command=popup.destroy)
        Ok.pack()
        popup.mainloop()


win.geometry("915x500")
win.maxsize(width=915, height=500)

user_word = StringVar()

user_label = Label(win, text="Enter your word :", font=15)
user_label.grid(row=0, column=1, pady=10)

input_field = Entry(master=win, textvariable=user_word)
input_field.grid(row=0, column=5, pady=10)

note = Label(win,
             text="Note: You can only enter word with length less than or equal to 4 \n\t otherwise we can't add all word of your entered string.",
             font=20)
note.grid(row=1, column=1, columnspan=5, pady=10)

size = IntVar()

user_label = Label(win, text="Enter size that you wan't :", font=15)
user_label.grid(row=2, column=1, pady=10)

input_field = Entry(master=win, textvariable=size)
input_field.grid(row=2, column=5, pady=10)

generate = Button(win, width=15, text="Generate", command=password)
generate.grid(row=3, column=1, columnspan=5, pady=10, padx=10)

label = Label(win, text="Suggested Password :", font=15)
label.grid(row=4, column=1, columnspan=5, padx=10, pady=10)

output = Text(win, height=20, width=59, font=('Arial', 20))
output.grid(row=5, column=1, columnspan=5, padx=10, pady=10)

win.mainloop()
