from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askdirectory
import os
import shutil


music = ["mp3", "3gp", "aa", "aac", "act", "aiff", "alac", "amr", "ape", "au",
         "m4a", "m4b", "m4p", "mmf", "mp3", "mpc", "wav"]

video = ["mp4", "avi", "mkv", "3gp", "hdv", "webm", "wmv"]

image = ["jpg", "jpeg", "png", "ico", "gif", "bmp", "webp", "heif"]

document = ["doc", "docm", "docx", "dot", "dotm", "htm", "html", "pdf", "odt", "rtf", "txt", "xml"]

dataset = ["csv", "sql", "splite", "db"]

program = ["java", "php", "CPP", "C", "cs", "js"]

win = Tk()


def pop_up():
    popup = Tk()
    popup.wm_title("Warning !")
    label = Label(popup, text="All Files Successfully Sorted.")
    label.pack(side="top", fill="x", pady=10, padx=10)
    Ok = Button(popup, width=20, text="Ok", command=popup.destroy)
    Ok.pack()
    popup.mainloop()


def openfiledialog():
    file = askdirectory(title="Select Folder")
    path.set(file)

    os.chdir(file)
    li = os.listdir(path=file)
    mu = 0
    doc = 0
    vid = 0
    db = 0
    im = 0
    py = 0
    pro = 0
    other = 0
    total = 0
    cur_path = os.getcwd()

    for i in li:
        if os.path.isfile(os.path.join(file, i)):
            ext = str(i.split(".")[-1]).lower()
            if ext in music:
                mu += 1
            elif ext in video:
                vid += 1
            elif ext in image:
                im += 1
            elif ext in document:
                doc += 1
            elif ext in dataset:
                db += 1
            elif ext == "py":
                py += 1
            elif ext in program:
                pro += 1
            else:
                other += 1
            total += 1

    image_list["text"] = f"Image : {str(im)}"
    video_list["text"] = f"Video : {str(vid)}"
    music_list["text"] = f"Music : {str(mu)}"
    Doc_list["text"] = f"Document : {str(doc)}"
    db_list["text"] = f"DataSets : {str(db)}"
    Other_list["text"] = f"Other : {str(other)}"
    total_list["text"] = f"Total Files : {str(total)}"
    python_list["text"] = f".py : {str(py)}"
    pro_list["text"] = f"Programming Files : {str(pro)}"

    try:
        if im > 0:
            os.makedirs(os.path.join(file, "Images"))
        if vid > 0:
            os.makedirs(os.path.join(file, "Videos"))
        if mu > 0:
            os.makedirs(os.path.join(file, "Musics"))
        if doc > 0:
            os.makedirs(os.path.join(file, "Documents"))
        if db > 0:
            os.makedirs(os.path.join(file, "DataSet Files"))
        if py > 0:
            os.makedirs(os.path.join(file, "Python Files"))
        if pro > 0:
            os.makedirs(os.path.join(file, "Program Files"))
        if other > 0:
            os.makedirs(os.path.join(file, "Others"))
    except FileExistsError as f:
        pass

    for i in li:
        if os.path.isfile(os.path.join(cur_path, i)):
            ext = str(i.split(".")[-1]).lower()
            if ext in music:
                shutil.move(file+f"/{i}", file+"/Musics")
            elif ext in video:
                shutil.move(file + f"/{i}", file + "/Videos")
            elif ext in image:
                shutil.move(file + f"/{i}", file + "/Images")
            elif ext in document:
                shutil.move(file + f"/{i}", file + "/Documents")
            elif ext in dataset:
                shutil.move(file + f"/{i}", file + "/DataSet Files")
            elif ext == "py":
                shutil.move(file + f"/{i}", file + "/Python Files")
            elif ext in program:
                shutil.move(file + f"/{i}", file + "/Program Files")
            else:
                shutil.move(file + f"/{i}", file + "/Others")
                
    pop_up()


win.geometry("800x500")
win.maxsize(width=800, height=500)

file_label = Label(win, text="Choose Folder", font=("Arial", 20))
file_label.grid(row=0, column=0, columnspan=5, pady=10)

path = StringVar()
path_text = Entry(win, width=100, textvariable=path)
path_text.grid(row=1, column=0, columnspan=3, padx=20)

file_dialog = Button(win, text="Open", command=openfiledialog)
file_dialog.grid(row=1, column=4, padx=20)

python_list = Label(win, text=".py : 0", font=("Arial", 15))
python_list.grid(row=2, column=0, pady=10)

image_list = Label(win, text="Image : 0", font=("Arial", 15))
image_list.grid(row=3, column=0, pady=10)

video_list = Label(win, text="Video : 0", font=("Arial", 15))
video_list.grid(row=4, column=0, pady=10)

Doc_list = Label(win, text="Document : 0", font=("Arial", 15))
Doc_list.grid(row=5, column=0, pady=10)

music_list = Label(win, text="Music : 0", font=("Arial", 15))
music_list.grid(row=6, column=0, pady=10)

db_list = Label(win, text="DataSet : 0", font=("Arial", 15))
db_list.grid(row=7, column=0, pady=10)

Other_list = Label(win, text="Other : 0", font=("Arial", 15))
Other_list.grid(row=8, column=0, pady=10)

pro_list = Label(win, text="Programming Files : 0", font=("Arial", 15))
pro_list.grid(row=9, column=0, pady=10)

total_list = Label(win, text="Total Files : 0", font=("Arial", 15))
total_list.grid(row=10, column=0, columnspan=5, pady=10)

win.mainloop()
