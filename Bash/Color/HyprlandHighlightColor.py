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
# from subprocess import Popen, PIPE
import subprocess as sp
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

    # 2nd Row Destination-----------------------------------------------------------------------------
    destination_label = Label(pane, text="Color Hex Code :", bg="white", font="Arial")
    destination_label.grid(row=3, column=0, sticky="enw")
    root.destinationText = Entry(pane, font="Arial", textvariable=hexColor)
    root.destinationText.insert(0, call)
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

call = sp.getoutput('echo "$(</home/$USER/Hyprland2.0/Bash/Color/currentColor)"')
print(call)

def hyprpickerColor():
    command = os.popen('hyprpicker | sed "s/^.\{1\}//"')
    output = command.read()
    print(output[:6])
    hexColor.set(output[:6])


def setColor():
    # Get current color
    command = os.popen('echo "$(</home/$USER/Hyprland2.0/Bash/Color/currentColor)"')
    currentColor1 = command.read()
    currentColor2 = currentColor1[:6]
    print(currentColor2)

    # Update Waybar
    # os.system('sed -i "/@define-color borderColor/c @define-color borderColor #{};" .config/HyprV/waybar/style/Tr3ble-Dark.css'.format(hexColor.get()))
    # os.system('sed -i "/@define-color highlightColor/c @define-color highlightColor #{};" .config/HyprV/waybar/style/Tr3ble-Dark.css'.format(hexColor.get()))

    os.system('sed -i "/{}/c {}" /home/$USER/Hyprland2.0/Bash/Color/currentColor'.format(currentColor2, hexColor.get()))
    #hyprland (border)
    os.system('sed -i "s/{}/{}/g" .config/hypr/hyprland.conf'.format(currentColor2, hexColor.get()))
    # gtk (thunar)
    os.system('sed -i "s/{}/{}/g" .config/gtk-3.0/gtk.css'.format(currentColor2, hexColor.get()))
    # wofi
    os.system('sed -i "s/{}/{}/g" .config/wofi/style.css'.format(currentColor2, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/wofi/style/Wofi-Tr3ble-Dark.css'.format(currentColor2, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/wofi/style/Wofi-Tr3ble-Light.css'.format(currentColor2, hexColor.get()))
    # waybar
    os.system('sed -i "s/{}/{}/g" .config/HyprV/waybar/style/Tr3ble-Dark.css'.format(currentColor2, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/waybar/style/Tr3ble-Light.css'.format(currentColor2, hexColor.get()))
    # wlogout
    os.system('sed -i "s/{}/{}/g" .config/HyprV/wlogout/style/dark_style.css'.format(currentColor2, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/wlogout/style/light_style.css'.format(currentColor2, hexColor.get()))
    # mako
    os.system('sed -i "s/{}/{}/g" .config/HyprV/mako/conf/dark_config'.format(currentColor2, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/mako/conf/light_config'.format(currentColor2, hexColor.get()))
    os.system('makoctl reload')
    # firefox
    os.system('sed -i "s/{}/{}/g" .mozilla/firefox/*.default-release/chrome/userChrome.css'.format(currentColor2, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .mozilla/firefox/*.default-release/chrome/userContent.css'.format(currentColor2, hexColor.get()))

    # Restart Waybar
    os.system('hyprctl reload')
    quit()

# Creating the tkinter Variables
hexColor = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()