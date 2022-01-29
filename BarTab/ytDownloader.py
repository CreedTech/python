from tkinter import *
from tkinter import ttk, filedialog

from pytube import YouTube

Folder_Name = ""


def open_location():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        locationError.config(text=Folder_Name, fg="green")
    else:
        locationError.config(text="Choose your folder", fg="red")


def download():
    choice = downloadChoices.get()
    url = entry.get()

    if len(url) > 1:
        error.config(text="")
        yt = YouTube(url)

        if choice == choices[0]:
            select = yt.streams.filter(progressive=True).first()

        elif choice == choices[1]:
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif choice == choices[2]:
            select = yt.streams.filter(only_audio=True).first()

        else:
            error.config(text="Paste Link Again", fg="red")

    select.download(Folder_Name)
    error.config(text="Download Completed")


root = Tk()
root.title("Creed Youtube Downloader")
root.geometry('350x400')
root.columnconfigure(0, weight=1)

label_for_yt = Label(root, text="Enter the link", font="poppins,15")
label_for_yt.grid()

link = StringVar()
entry = Entry(root, width=50, textvariable=link)
entry.grid()

error = Label(root, text="Error Msg", fg="blue", font="poppins,10")
error.grid()

save = Label(root, text="Save", font="poppins,15,bold")
save.grid()

saveBtn = Button(root, width=10, bg="blue", fg="white", text="Choose Path", command=open_location)
saveBtn.grid()

locationError = Label(root, text="Path Error Msg", fg="blue", font="poppins,10")
locationError.grid()

quality = Label(root, text="Select Quality", font="poppins,15")
quality.grid()

choices = ["720p", "144p", "Only Audio"]
downloadChoices = ttk.Combobox(root, values=choices)
downloadChoices.grid()

downloadBtn = Button(root, text="Download", width=10, bg="blue", fg="white", command=download)
downloadBtn.grid()

root.mainloop()
