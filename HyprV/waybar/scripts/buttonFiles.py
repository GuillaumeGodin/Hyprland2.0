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
root.title("Files")
root.configure(bg="#222222")
root.bind("<Escape>", lambda x: root.destroy())
# root.bind("<Button-1>", lambda x: root.destroy())

def Widgets():

    # pane = Frame(root, bg="black")
    pane = Frame(root)    
    pane.pack(fill=X, expand=True)

    # 1st Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Desktop", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=desktop, relief=GROOVE, pady=0)
    Download_B.grid(row=2, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 2nd Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Documents", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=documents, relief=GROOVE, pady=0)
    Download_B.grid(row=3, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 3rd Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Downloads", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=downloads, relief=GROOVE, pady=0)
    Download_B.grid(row=4, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 4th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Music", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=music, relief=GROOVE, pady=0)
    Download_B.grid(row=5, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 5th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Pictures", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=pictures, relief=GROOVE, pady=0)
    Download_B.grid(row=6, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 6th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Videos", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=videos, relief=GROOVE, pady=0)
    Download_B.grid(row=7, column=0, columnspan=2, sticky="ew", pady=0, padx=0)

#-----------------------------------------------------------------------------------------------------

def quit():
    global root
    root.quit()
    
def desktop():
    os.system('thunar /home/$USER/Desktop 1>/dev/null &')
    root.quit()

def documents():
    os.system('thunar /home/$USER/Documents 1>/dev/null &')
    root.quit()

def downloads():
    os.system('thunar /home/$USER/Downloads 1>/dev/null &')
    root.quit()

def music():
    os.system('thunar /home/$USER/Music 1>/dev/null &')
    root.quit()

def pictures():
    os.system('thunar /home/$USER/Pictures 1>/dev/null &')
    root.quit()

def videos():
    os.system('thunar /home/$USER/Videos 1>/dev/null &')
    root.quit()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()