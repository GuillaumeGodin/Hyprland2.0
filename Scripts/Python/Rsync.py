# sudo apt-get install python3-tk

import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

root = tk.Tk()
#root.geometry("600x140")
root.resizable(height = None, width = None)
root.resizable(0, 0)
root.title("Rsync")
root.config(background="black")

def Widgets():

    #    pane = Frame(root, bg="black")
    pane = Frame(root)    
    pane.pack(fill=X, expand=True)

    # 1st Row Header---------------------------------------------------------------------------------
    head_label = Label(pane, text="Rsync", bg="blue", font="SegoeUI 14", fg="white", width=55)
    head_label.grid(row=0, column=0, columnspan=4, sticky="n")

    # 2nd Row origin----------------------------------------------------------------------------------
    origin_label = Label(pane, text="From :", bg="white", font="Arial")
    origin_label.grid(row=1, column=0, sticky="enw")
    root.originText = Entry(pane, textvariable=from_Path, font="Arial", width=45)
    root.originText.grid(row=1, column=1, columnspan=2, sticky="new")
    browse_B = Button(pane, text="Browse", bg="bisque", font="Arial", command=Browse_From, relief=GROOVE, pady=0)
    browse_B.grid(row=1, column=3, sticky="wne")

    # 3rd Row Destination-----------------------------------------------------------------------------
    destination_label = Label(pane, text="To :", bg="white", font="Arial")
    destination_label.grid(row=2, column=0, sticky="enw")
    root.destinationText = Entry(pane, textvariable=to_Path, font="Arial")
    root.destinationText.grid(row=2, column=1, columnspan=2, sticky="new")
    browse_B = Button(pane, text="Browse", bg="bisque", font="Arial", command=Browse_To, relief=GROOVE, pady=0)
    browse_B.grid(row=2, column=3, sticky="wne")

    # 4th Row Button B--------------------------------------------------------------------------------
    Download_B = Button(pane, text="Full Sync", font="Arial", bg="thistle1", command=FullRsync, relief=GROOVE, pady=0)
    Download_B.grid(row=4, column=0, columnspan=2, sticky="ew", pady=5, padx=20)
    Download_B = Button(pane, text="Sync Keep Latest", font="Arial", bg="thistle1", command=RsyncKeepLatest, relief=GROOVE, pady=0)
    Download_B.grid(row=4, column=2, columnspan=2, sticky="we", pady=5, padx=20)

#-----------------------------------------------------------------------------------------------------
def Browse_From():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="From Folder")
    from_Path.set(download_Directory)

def Browse_To():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="To Folder")
    to_Path.set(download_Directory)


def FullRsync():

    os.system(
        'rsync -asvAX --delete --exclude "*Trash-1000" "{}/" "{}/"'.format(from_Path.get(), to_Path.get()))
        #rsync -aAX --delete --exclude '*Trash-1000' /media/g/10TB/* /media/g/10TB\ \(Backup\)/ 

def RsyncKeepLatest():

    os.system(
        'rsync -asuv "{}/" "{}/"'.format(from_Path.get(), to_Path.get()))

# Creating the tkinter Variables
video_Link = StringVar()
video_Name = StringVar()
from_Path = StringVar()
to_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()