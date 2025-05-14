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
root.title("Apps")
root.configure(bg="#222222")
root.bind("<Escape>", lambda x: root.destroy())

def Widgets():

    #    pane = Frame(root, bg="black")
    pane = Frame(root)    
    pane.pack(fill=X, expand=True)

    # 1st Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="   Firefox", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=firefox, relief=GROOVE, pady=0)
    Download_B.grid(row=2, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 2nd Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="󰇰   Mail_Evolution", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=evolution, relief=GROOVE, pady=0)
    Download_B.grid(row=3, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 3rd Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="   Steam", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=steam, relief=GROOVE, pady=0)
    Download_B.grid(row=4, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 4th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="   Discord", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=discord, relief=GROOVE, pady=0)
    Download_B.grid(row=5, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 5th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="   Gimp", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=gimp, relief=GROOVE, pady=0)
    Download_B.grid(row=6, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 6th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="   Blender", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=blender, relief=GROOVE, pady=0)
    Download_B.grid(row=7, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 6th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="   Terminal_Kitty", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=kitty, relief=GROOVE, pady=0)
    Download_B.grid(row=8, column=0, columnspan=2, sticky="ew", pady=0, padx=0)

#-----------------------------------------------------------------------------------------------------

def quit():
    global root
    root.quit()
    
def firefox():
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window &')
    root.quit()

def evolution():
    os.system('evolution 1>/dev/null &')
    root.quit()

def steam():
    os.system('steam 1>/dev/null &')
    root.quit()

def discord():
    os.system('discord 1>/dev/null &')
    root.quit()

def gimp():
    os.system('gimp 1>/dev/null &')
    root.quit()

def blender():
    os.system('blender 1>/dev/null &')
    root.quit()

def kitty():
    os.system('kitty 1>/dev/null &')
    root.quit()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()