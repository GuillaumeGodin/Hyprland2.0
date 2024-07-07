# sudo apt-get install python3-tk
# VCFUEFULG83CBRB2

import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pathlib import Path

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
    head_label = Label(pane, text="Tstock", bg="yellow", font="SegoeUI 14", fg="Black", width=55)
    head_label.grid(row=0, column=0, columnspan=4, sticky="n")

    # 2nd Row origin----------------------------------------------------------------------------------
    origin_label = Label(pane, text=".conf :", bg="white", font="Arial")
    origin_label.grid(row=1, column=0, sticky="enw")
    root.originText = Entry(pane, textvariable=from_Path, font="Arial", width=45)
    root.originText.grid(row=1, column=1, columnspan=3, sticky="new")

    # 3rd Row Button B--------------------------------------------------------------------------------
    Download_B = Button(pane, text="OK", font="Arial", bg="thistle1", command=FullRsync, relief=GROOVE, pady=0)
    Download_B.grid(row=2, column=0, columnspan=4, sticky="ew", pady=5, padx=20)

#-----------------------------------------------------------------------------------------------------
def Browse_From():
    download_Directory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH", title="From Folder")
    from_Path.set(download_Directory)


def FullRsync():
    #print(from_Path.get())
    os.system('kitty 2> /dev/null tstock {}'.format(from_Path.get()))

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