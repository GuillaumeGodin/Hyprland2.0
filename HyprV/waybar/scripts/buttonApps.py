# sudo apt-get install python3-tk

import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pathlib import Path

root = tk.Tk()
# root.geometry("600x140")
root.geometry('+50+637')
root.resizable(height = None, width = None)
root.resizable(0, 0)
# root.resizable(10, 10)
root.title("Apps")
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
    # 15_Notes----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="Notes", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=zim,
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=19, 
        column=0, 
        columnspan=2, 
        sticky="ew",
        pady=0, 
        padx=0
    )
    # 14_Calculator----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="Calculator", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=galculator, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=20, 
        column=0, 
        columnspan=2, 
        sticky="ew",
        pady=0, 
        padx=0
    )
    # 13_LibreOffice----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="LibreOffice", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=libreoffice, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=45, 
        column=0, 
        columnspan=2, 
        sticky="ew",
        pady=(2,0),
        padx=0
    )
    # 12_Audacity----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="Audacity", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=audacity, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=46, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 11_Handbrake----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="Handbrake", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=handbrake, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=47, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 10_MediaInfo----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="Media_Info", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=mediainfo, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=48, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 9_MkvTool----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="MkvTool", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=mkvtool, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=49, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 8_MkvTool_Batch----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="MkvTool_Batch", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=mkvtool_batch, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=50, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=0, 
        padx=0
    )
    # 1st Row----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="Work_Mode", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=lambda: [lanmouse(), onedrivegui()],
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
    # 7_Firefox----------------------------------------------------------------------------------
    File_1 = Button (
        pane, 
        text="   Firefox", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
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
    # 6_Evolution----------------------------------------------------------------------------------
    File_2 = Button (
        pane, 
        text="󰇰   Mail_Evolution", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
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
    # 5_Steam----------------------------------------------------------------------------------
    File_3 = Button (
        pane, 
        text="   Steam", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
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
    # 4_Discord----------------------------------------------------------------------------------
    File_4 = Button (
        pane, 
        text="   Discord", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
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
    # 3_Gimp----------------------------------------------------------------------------------
    File_5 = Button (
        pane, text="   Gimp", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
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
    # 2_Blender----------------------------------------------------------------------------------
    File_6 = Button (
        pane, 
        text="   Blender", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
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
    # 1_Terminal----------------------------------------------------------------------------------
    File_7 = Button (
        pane, 
        text="   Terminal_Kitty", 
        font=("JetBrainsMono", 14), 
        anchor="sw",
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

def exit():
    os.system('hyprctl keyword unbind , mouse:273')
    root.destroy()
    
def zim():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('zim --geometry 1000x600+1280+720 1>/dev/null &')
    root.quit()
    
def galculator():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('galculator 1>/dev/null &')
    root.quit()
    
def libreoffice():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('libreoffice 1>/dev/null &')
    root.quit()
    
def audacity():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('audacity 1>/dev/null &')
    root.quit()
    
def handbrake():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('ghb 1>/dev/null &')
    root.quit()
    
def mediainfo():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('mediainfo-gui 1>/dev/null &')
    root.quit()
    
def mkvtool():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('mkvtoolnix-gui 1>/dev/null &')
    root.quit()

def mkvtool_batch():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('python Documents/MKV_Batch/main.py 1>/dev/null &')
    root.quit()
    
# def lanmouse():
#     os.system('hyprctl keyword unbind , mouse:273')
#     os.system('lan-mouse 1>/dev/null &')
#     root.quit()
    
# def onedrivegui():
#     os.system('hyprctl keyword unbind , mouse:273')
#     os.system('onedrivegui 1>/dev/null &')
#     root.quit()
    
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
    os.system('blender -p 1920 1080 1280 720 1>/dev/null &')
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