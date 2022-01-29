from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.title("Youtube Downloader")
link = StringVar()
Label(text="Creed Youtube Downloader 😍😘🥰", font="poppins 20 bold", pady=30).pack()
Label(text="Enter link here: ", fg="red", font="poppins 10 bold").pack()
link_entry = Entry(width=50, border=5, textvariable=link).pack()

value = 1


def downloader():
    global value
    value -= 1
    if value == 0:
        Label(text="DOWNLOADING", font="poppins 10 bold", bg="red").pack()
        value = 1
    else:
        pass
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download("C:\\Users\\AY\\Downloads")
    Label(text="DOWNLOADED", font="poppins 20 bold", bg="red").pack()


Button(text="DOWNLOAD😁😑", font="poppins 20 bold", bg="red", padx=2, command=downloader).pack()

root.mainloop()
