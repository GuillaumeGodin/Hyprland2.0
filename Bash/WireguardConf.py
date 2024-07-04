# sudo apt-get install python3-tk

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
    head_label = Label(pane, text="Wireguard", bg="green", font="SegoeUI 14", fg="white", width=55)
    head_label.grid(row=0, column=0, columnspan=4, sticky="n")

    # 2nd Row origin----------------------------------------------------------------------------------
    origin_label = Label(pane, text=".conf :", bg="white", font="Arial")
    origin_label.grid(row=1, column=0, sticky="enw")
    root.originText = Entry(pane, textvariable=from_Path, font="Arial", width=45)
    root.originText.grid(row=1, column=1, columnspan=2, sticky="new")
    browse_B = Button(pane, text="Browse", bg="bisque", font="Arial", command=Browse_From, relief=GROOVE, pady=0)
    browse_B.grid(row=1, column=3, sticky="wne")

    # 3rd Row Button B--------------------------------------------------------------------------------
    Download_B = Button(pane, text="OK", font="Arial", bg="thistle1", command=FullRsync, relief=GROOVE, pady=0)
    Download_B.grid(row=2, column=0, columnspan=4, sticky="ew", pady=5, padx=20)

#-----------------------------------------------------------------------------------------------------
def Browse_From():
    download_Directory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH", title="From Folder")
    from_Path.set(download_Directory)


def FullRsync():

    name=os.path.basename('{}').format(from_Path.get())
    head, tail = os.path.split(name)
    name=os.path.basename('{}').format(tail)
    file, ext = os.path.splitext(name)
    #print(tail) #returns acer.conf
    #print(file) #returns acer

    os.system('nmcli connection import type wireguard file {}'.format(from_Path.get()))
    #print('nmcli connection import type wireguard file {}'.format(from_Path.get()))
    os.system('nmcli connection modify {} autoconnect no'.format(file))

    #moving doesn't work, needs sudo privilege
    #os.system("mv {} /etc/wireguard/{}".format(from_Path.get(), tail))
    #print("mv {} /etc/wireguard/{}".format(from_Path.get(), tail))

    #delete .conf
    os.system("rm {}".format(from_Path.get()))

    #delete (acer.conf profile)
    #nmcli connection delete acer
    #chanage autoconnect (acer.conf profile)
    #nmcli connection modify acer autoconnect no
    #see profile info for (acer.conf profile)
    #nmcli connection show acer

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