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
root.title("Cryptsetup")
root.config(background="black")

def Widgets():

    #    pane = Frame(root, bg="black")
    pane = Frame(root)    
    pane.pack(fill=X, expand=True)

    # 1st Row Header---------------------------------------------------------------------------------
    head_label = Label(pane, text="Cryptsetup", bg="pink", font="SegoeUI 14", fg="black", width=55)
    head_label.grid(row=0, column=0, columnspan=4, sticky="n")

    # 2nd Row--------------------------------------------------------------------------------
    origin_label = Label(pane, text="lsblk :", bg="white", font="Arial")
    origin_label.grid(row=2, column=0, sticky="enw")
    root.originText = Entry(pane, textvariable=from_Path, font="Arial", width=45)
    root.originText.grid(row=2, column=1, columnspan=2, sticky="new")
    root.originText.insert(0, "sda1")
    browse_B = Button(pane, text="Browse", bg="bisque", font="Arial", command=Browse_From, relief=GROOVE, pady=0)
    browse_B.grid(row=2, column=3, sticky="wne")

    # 3rd Row--------------------------------------------------------------------------------
    origin_label = Label(pane, text="Sudo :", bg="white", font="Arial")
    origin_label.grid(row=3, column=0, sticky="enw")
    root.originText = Entry(pane, textvariable=password, show='-', font="Arial", width=45)
    root.originText.grid(row=3, column=1, columnspan=3, sticky="new")

    # 4th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Mount", font="Arial", bg="thistle1", command=mount, relief=GROOVE, pady=0)
    Download_B.grid(row=4, column=0, columnspan=2, sticky="ew", pady=5, padx=20)
    Download_B = Button(pane, text="Unmount", font="Arial", bg="thistle1", command=unmount, relief=GROOVE, pady=0)
    Download_B.grid(row=4, column=2, columnspan=2, sticky="we", pady=5, padx=20)

#-----------------------------------------------------------------------------------------------------
def quit():
    global root
    root.quit()

def Browse_From():
    download_Directory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH", title="From Folder")
    from_Path.set(download_Directory)

def mount():
    os.system('echo {} | sudo -S mkdir /mnt/encrypted'.format(password.get()))
    os.system('echo {} | echo {} | sudo -S cryptsetup open /dev/{} {}'.format(password.get(), password.get(), from_Path.get(), from_Path.get()))
    os.system('echo {} | sudo -S mount /dev/mapper/{} /mnt/encrypted'.format(password.get(), from_Path.get()))
    os.system('echo {} | sudo -S chown -R `whoami`:users /mnt/encrypted'.format(password.get()))
    os.system('thunar /mnt/encrypted')
    
def unmount():
    os.system('echo {} | sudo -S umount /dev/mapper/{} /mnt/encrypted'.format(password.get(), from_Path.get()))
    os.system('echo {} | sudo -S cryptsetup close {}'.format(password.get(), from_Path.get()))
    os.system('echo {} | sudo -S rm -r /mnt/encrypted'.format(password.get()))
    root.quit()

from_Path = StringVar()
rename = StringVar()
password = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()