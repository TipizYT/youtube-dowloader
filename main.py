import tkinter
import tkinter.messagebox
import webbrowser
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from typing import MutableSet
from pytube import YouTube

root = Tk()

root.title ('Tipiz YouTube Video Downloader')
root.geometry('650x200')
root.resizable(width=False,height=False)
#root.iconbitmap('yt.ico')

vlink = StringVar()
folder_path = StringVar()


def about():
    webbrowser.open('https://www.gooogle.com')

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def Download_Video():
    video = YouTube (str(vlink.get()))
    dlocation = str(folder_path.get())
    dv = video.streams.get_highest_resolution()
    dv.download(dlocation)
    message = tkinter.messagebox.showinfo(title="Download Report", message="Your Video Downloaded Sucessfully!")


menubar = Menu(root)  
file = Menu(menubar, tearoff=0)  

file.add_command(label="Exit", command=root.quit)  
menubar.add_cascade(label="File", menu=file)  

help = Menu(menubar, tearoff=0)  
help.add_command(label="About" , command=about)  
menubar.add_cascade(label="Help", menu=help)  
  
root.config(menu=menubar)

title = tkinter.Label(
    text='YouTube Video Downloader',
    font ='arial 20 bold',   
)

title.pack()

il = tkinter.Label(
    text='Enter your YouTube Video Url',
    font='arial 15 bold'
)

il.place(x = 5, y = 57)

link = tkinter.Entry(
    width=50,
    font = 'arial 15 bold',
    textvariable=vlink).place(x = 5, y = 100)


lbl1 = Label(master=root,textvariable=folder_path)
lbl1.pack()


button2 = tkinter.Button(
    text="Browse", 
    bg='DarkGoldenrod1',
    fg='snow',
    font='arial 13',
    command=browse_button)
button2.place(x = 575, y =97)

tkinter.Button(root,text = 'DOWNLOAD VIDEO', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=400 ,y = 140)

root.mainloop()  
