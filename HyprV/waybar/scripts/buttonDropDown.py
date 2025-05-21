# sudo apt-get install python3-tk

import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pathlib import Path

root = tk.Tk()
# root.geometry("600x140")
root.resizable(height = None, width = None)
root.resizable(0, 0)
# root.resizable(10, 10)
root.title("dropDown")
# root.configure(bg="#222222")
# root.bind("<Escape>", exit)
root.bind("<Escape>", lambda x: exit())
# root.bind("<FocusOut>", exit)

# root.bind("<Escape>", lambda x: root.destroy())
# root.bind("<FocusOut>", lambda x: root.destroy())
# root.bind("<FocusIn>", lambda x: root.destroy())
# root.bind("<Button-1>", lambda x: root.destroy())

os.system('hyprctl keyword bind , mouse:273, exec, bash Hyprland2.0/Bash/killDropdowns')

def Widgets():
    pane = Frame(root, bg="#ffbb00")
    # pane = Frame(root)  
    pane.pack(fill=X, expand=True)

    # 1st Row----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="Jellyfin", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=jellyfin, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=2, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 2nd Row----------------------------------------------------------------------------------
    File_2 = Button (
        pane, 
        text="Recipes", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=recipes, 
        relief=GROOVE, 
        pady=0
    )
    File_2.grid (
        row=3, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 3rd Row----------------------------------------------------------------------------------
    File_3 = Button (
        pane, 
        text="Google", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=google, 
        relief=GROOVE, 
        pady=0
    )
    File_3.grid (
        row=4, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 4th Row----------------------------------------------------------------------------------
    File_4 = Button (
        pane, 
        text="Google Maps", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=maps, 
        relief=GROOVE, 
        pady=0
    )
    File_4.grid (
        row=5, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 5th Row----------------------------------------------------------------------------------
    File_5 = Button (
        pane, 
        text="Weather Networks", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=weather, 
        relief=GROOVE, 
        pady=0
    )
    File_5.grid (
        row=6, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 6th Row----------------------------------------------------------------------------------
    File_6 = Button (
        pane, 
        text="Play Music", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=music, 
        relief=GROOVE, 
        pady=0
    )
    File_6.grid (
        row=7, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )

#-----------------------------------------------------------------------------------------------------

def quit():
    global root
    root.quit()

def exit():
    os.system('hyprctl keyword unbind , mouse:273')
    root.destroy()
    
def jellyfin():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window http://192.168.111.100:8097/web/#/home.html &')
    root.quit()

def recipes():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window http://192.168.111.100:8090/search/ &')
    root.quit()

def google():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window https://www.google.com &')
    root.quit()

def maps():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window https://www.google.com/maps &')
    root.quit()

def weather():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window https://www.theweathernetwork.com/en/city/ca/ontario/ottawa/hourly &')
    root.quit()

def music():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('./.config/HyprV/waybar/scripts/mediaSwitch')
    root.quit()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()