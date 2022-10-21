import pytube
import subprocess
import os

SAVE_PATH = "F:/python project by MR.SD/youtube_downloader"

link=input("Enter YouTube URL : ")

yt = pytube.YouTube(link)

count = 0
stre = yt.streams.all()

for s in stre:
	print(f"\n{count}", s, "\n")
	count += 1

num = int(input("Enter what you want to download :"))
choice = stre[num]

choice.download(SAVE_PATH)

new_filename = input("Enter filename (including extension): ")  # e.g. new_filename.mp3

default_filename = stre[num].default_filename  # get default name using pytube API
subprocess.call([                               # or subprocess.run (Python 3.5+)
	'ffmpeg',
	'-i', os.path.join(SAVE_PATH, default_filename),
	os.path.join(SAVE_PATH, new_filename)
])

print("done")