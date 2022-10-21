from pytube import YouTube

# url = str(input("Enter YouTube URL : "))

url = ""
path = "F:/python project by MR.SD/youtube_downloader"

y = YouTube("https://www.youtube.com/watch?v=HZJY_7X_LWs")

strm = y.streams.all()

for i in strm:
    print(i)

print(strm)

# strm.download(path)

print("done")
