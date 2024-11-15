#to use in terminal for video only no audio
#Desktop\Python\yt-dlp.exe --list-formats (link)
#Desktop\Python\yt-dlp.exe -f (format#) Desktop/(filename) (link)

#to use in terminal for playlist audio only
#Desktop\Python\yt-dlp.exe --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "%(title)s.%(ext)s" --yes-playlist (link)

#Ubuntu
#sudo apt install yt-DownloadPlaylist
#sudo apt install tk
#sudo apt install python3-tk

#Arch
#sudo pacman -Syu yt-dlp
#sudo pacman -S tk

import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

root = tk.Tk()
#root.geometry("600x140")
root.resizable(height = None, width = None)
root.resizable(0, 0)
root.title("Hyprland Highlight Color")
root.config(background="black")

def Widgets():

#    pane = Frame(root, bg="black")
    pane = Frame(root)    
    pane.pack(fill=X, expand=True)

#    root.grid_columnconfigure(0, weight=0)
#    root.grid_columnconfigure(1, weight=0)
#    root.grid_columnconfigure(2, weight=0)
#    root.grid_columnconfigure(3, weight=0)

    # 1st Row Header----------------------------------------------------------------------------------
    head_label = Label(pane, text="Hyprland Highlight Color", bg="orange", fg="white", font="SegoeUI 14", width=55)
#    head_label.pack(fill=X, expand=False, side=TOP)
    head_label.grid(row=0, column=0, columnspan=3, sticky="n")

    # 4th Row Destination-----------------------------------------------------------------------------
    destination_label = Label(pane, text="Color Hex Code :", bg="white", font="Arial")
    destination_label.grid(row=3, column=0, sticky="enw")
    root.destinationText = Entry(pane, font="Arial", textvariable=download_Path)
    # root.destinationText.insert(0, "/home/$USER/Music/") 
    root.destinationText.grid(row=3, column=1, sticky="new")
    browse_B = Button(pane, text="Hyprpicker", bg="bisque", font="Arial", command=hyprpickerColor, pady=0, relief=GROOVE)
    browse_B.grid(row=3, column=2, sticky="wne")
    
    # 5th Row Button Audio----------------------------------------------------------------------------
    Download_Audio = Button(pane, text="Set Color", bg="thistle1", font="Arial", command=setColor, relief=GROOVE, pady=0)
    Download_Audio.grid(row=4, column=1, sticky="new", padx=60, pady=5)

# def Browse():
#     download_Directory = filedialog.askdirectory(
#         initialdir="YOUR DIRECTORY PATH", title="Save Video")

#     download_Path.set(download_Directory)

def hyprpickerColor():
    # download_Directory = os.popen('hyprpicker').read()
    
    # download_Directory2 = os.system('{} | sed "s/^.\{1\}//" | sed "s/.\{1\}$//"'.format(download_Directory.get()))
    download_Directory = os.system('{} | sed "s/^.\{1\}//" | sed "s/.\{1\}$//"'.format(download_Directory.get()))

    download_Path.set(download_Directory)

# Creating the tkinter Variables
setColor = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()