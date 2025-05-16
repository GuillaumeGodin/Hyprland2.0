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
root.title("Apps")
# root.configure(bg="#222222")
root.bind("<Escape>", exit)
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
        text="Lan-Mouse", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=lanmouse, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=92, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )

    # 1st Row----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="   Firefox", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=firefox, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=93, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=(2,0),
        padx=0
    )
    # 2nd Row----------------------------------------------------------------------------------
    File_2 = Button (
        pane, 
        text="󰇰   Mail_Evolution", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=evolution, 
        relief=GROOVE, 
        pady=0
    )
    File_2.grid (
        row=94, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 3rd Row----------------------------------------------------------------------------------
    File_3 = Button (
        pane, 
        text="   Steam", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=steam, 
        relief=GROOVE, 
        pady=0
    )
    File_3.grid (
        row=95, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 4th Row----------------------------------------------------------------------------------
    File_4 = Button (
        pane, 
        text="   Discord", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=discord, 
        relief=GROOVE, 
        pady=0
    )
    File_4.grid (
        row=96, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 5th Row----------------------------------------------------------------------------------
    File_5 = Button (
        pane, text="   Gimp", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=gimp, 
        relief=GROOVE, 
        pady=0
    )
    File_5.grid (
        row=97, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 6th Row----------------------------------------------------------------------------------
    File_6 = Button (
        pane, 
        text="   Blender", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=blender, 
        relief=GROOVE, 
        pady=0
    )
    File_6.grid (
        row=98, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 7th Row----------------------------------------------------------------------------------
    File_7 = Button (
        pane, 
        text="   Terminal_Kitty", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=kitty, 
        relief=GROOVE, 
        pady=0
    )
    File_7.grid (
        row=99, 
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

def exit(e):
    root.destroy()
    
def lanmouse():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('lan-mouse 1>/dev/null &')
    root.quit()
    
def firefox():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window &')
    root.quit()

def evolution():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('evolution 1>/dev/null &')
    root.quit()

def steam():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('steam 1>/dev/null &')
    root.quit()

def discord():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('discord 1>/dev/null &')
    root.quit()

def gimp():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('gimp 1>/dev/null &')
    root.quit()

def blender():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('blender 1>/dev/null &')
    root.quit()

def kitty():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('kitty 1>/dev/null &')
    root.quit()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()