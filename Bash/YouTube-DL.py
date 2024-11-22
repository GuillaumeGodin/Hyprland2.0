#to use in terminal for video only no audio
#Desktop\Python\yt-dlp.exe --list-formats (link)
#Desktop\Python\yt-dlp.exe -f (format#) Desktop/(filename) (link)

#to use in terminal for playlist audio only
#Desktop\Python\yt-dlp.exe --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "%(title)s.%(ext)s" --yes-playlist (link)

#Best 1080 with audio
#yt-dlp -f "bestvideo[height<=1080]+bestaudio[ext=m4a]/bestvideo+bestaudio" (link)

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
root.title("YouTube-DL")
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
    head_label = Label(pane, text="YouTube Downloader", bg="red", fg="white", font="SegoeUI 14", width=55)
#    head_label.pack(fill=X, expand=False, side=TOP)
    head_label.grid(row=0, column=0, columnspan=3, sticky="n")

    # 2nd Row Link------------------------------------------------------------------------------------
    link_label = Label(pane, text="YouTube link :", bg="white", font="Arial")
    link_label.grid(row=1, column=0, sticky="enw")
    root.linkText = Entry(pane, font="Arial", textvariable=video_Link)
    root.linkText.grid(row=1, column=1, sticky="wne", columnspan=2)

    # 3rd Row File Name-------------------------------------------------------------------------------
    link_name = Label(pane, text="File Name :", bg="white", font="Arial")
    link_name.grid(row=2, column=0, sticky="enw")
    root.linkName = Entry(pane, font="Arial", textvariable=video_Name)
    root.linkName.insert(0, "%(title)s")
    root.linkName.grid(row=2, column=1, sticky="wne", columnspan=2)

    # 4th Row Destination-----------------------------------------------------------------------------
    destination_label = Label(pane, text="Destination :", bg="white", font="Arial")
    destination_label.grid(row=3, column=0, sticky="enw")
    root.destinationText = Entry(pane, font="Arial", textvariable=download_Path)
    root.destinationText.insert(0, "/home/$USER/Music/") 
    root.destinationText.grid(row=3, column=1, sticky="new")
    browse_B = Button(pane, text="Browse", bg="bisque", font="Arial", command=Browse, pady=0, relief=GROOVE)
    browse_B.grid(row=3, column=2, sticky="wne")
    
    # 5th Row Button Video----------------------------------------------------------------------------
    Download_Video = Button(pane, text="Video", bg="thistle1", font="Arial", command=DownloadVideo, relief=GROOVE, pady=0)
    Download_Video.grid(row=4, column=0, sticky="enw", padx=30, pady=5)
    
    # 5th Row Button Audio----------------------------------------------------------------------------
    Download_Audio = Button(pane, text="Audio", bg="thistle1", font="Arial", command=DownloadAudio, relief=GROOVE, pady=0)
    Download_Audio.grid(row=4, column=1, sticky="new", padx=60, pady=5)
    
    # 5th Row Button Playlist-------------------------------------------------------------------------
    Download_Playlist = Button(pane, text="Playlist", bg="thistle1", font="Arial", command=DownloadPlaylist, relief=GROOVE, pady=0)
    Download_Playlist.grid(row=4, column=2, sticky="enw", padx=30, pady=5)

def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    download_Path.set(download_Directory)


def DownloadVideo():
    
    os.system(
        'yt-dlp -f "bestvideo[height<=1080]+bestaudio[ext=m4a]/bestvideo+bestaudio" --merge-output-format mp4 -o "{}/{}.mp4" {}'.format(download_Path.get(), video_Name.get(), video_Link.get())
    )

    # os.system(
    #     'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio" --merge-output-format mp4 -o "{}/{}.mp4" {}'.format(download_Path.get(), video_Name.get(), video_Link.get())
    # )


def DownloadAudio():

    os.system(
        'yt-dlp --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "{}/{}.mp3" {}'.format(download_Path.get(), video_Name.get(), video_Link.get()))

def DownloadPlaylist():

    os.system(
        'yt-dlp --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "{}/%(title)s.%(ext)s" --yes-playlist {}'.format(download_Path.get(), video_Link.get()))

# Creating the tkinter Variables
video_Link = StringVar()
video_Name = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()