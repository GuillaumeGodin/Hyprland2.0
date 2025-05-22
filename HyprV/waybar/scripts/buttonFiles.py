# sudo apt-get install python3-tk

import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pathlib import Path

root = tk.Tk()
# root.geometry("600x140")
root.geometry('+125+855')
root.resizable(height = None, width = None)
root.resizable(0, 0)
# root.resizable(10, 10)
root.title("Files")
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
    pane = Frame (
        root, 
        bg="#ffbb00"
    )
    pane.pack (
        fill=X, 
        expand=True
    )
    # 1st Row----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="md0_Media", 
        font=("JetBrainsMono", 14),
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=media, 
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
    # 1st Row----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="   Desktop", 
        font=("JetBrainsMono", 14),
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=desktop, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=74, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=(2,0),
        padx=0
    )
    # 2nd Row----------------------------------------------------------------------------------
    File_2 = Button (
        pane, 
        text="󰈙   Documents", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=documents, 
        relief=GROOVE, 
        pady=0
    )
    File_2.grid ( 
        row=75, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 3rd Row----------------------------------------------------------------------------------
    File_3 = Button (
        pane, 
        text="   Downloads", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=downloads, 
        relief=GROOVE, 
        pady=0
    )
    File_3.grid (
        row=76, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 4th Row----------------------------------------------------------------------------------
    File_4 = Button (
        pane, 
        text="   Music", 
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
    File_4.grid (
        row=77, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 5th Row----------------------------------------------------------------------------------
    File_5 = Button (
        pane, 
        text="   Pictures", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=pictures, 
        relief=GROOVE, 
        pady=0
    )
    File_5.grid (
        row=78, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 6th Row----------------------------------------------------------------------------------
    File_6 = Button (
        pane, 
        text="   Videos", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=videos, 
        relief=GROOVE, 
        pady=0
    )
    File_6.grid (
        row=79, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )

# print ("Download_A")

# os.system('hyprctl keyword bind , mouse:272, movefocus, l')

#-----------------------------------------------------------------------------------------------------

def quit():
    global root
    root.quit()

def exit():
    os.system('hyprctl keyword unbind , mouse:273')
    root.destroy()
    
def media():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('thunar /home/$USER/mnt/md0/Media/Media_Arr/Deluge/ 1>/dev/null &')
    root.quit()
    
def desktop():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('thunar /home/$USER/Desktop 1>/dev/null &')
    root.quit()

def documents():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('thunar /home/$USER/Documents 1>/dev/null &')
    root.quit()

def downloads():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('thunar /home/$USER/Downloads 1>/dev/null &')
    root.quit()

def music():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('thunar /home/$USER/Music 1>/dev/null &')
    root.quit()

def pictures():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('thunar /home/$USER/Pictures 1>/dev/null &')
    root.quit()

def videos():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('thunar /home/$USER/Videos 1>/dev/null &')
    root.quit()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()