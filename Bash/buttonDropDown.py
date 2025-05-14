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
root.title("dropDown")
root.configure(bg="#222222")
root.bind("<Escape>", lambda x: root.destroy())

def Widgets():

    #    pane = Frame(root, bg="black")
    pane = Frame(root)    
    pane.pack(fill=X, expand=True)

    # 1st Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Jellyfin", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=jellyfin, relief=GROOVE, pady=0)
    Download_B.grid(row=2, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 2nd Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Recipes", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=recipes, relief=GROOVE, pady=0)
    Download_B.grid(row=3, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 3rd Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Google", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=google, relief=GROOVE, pady=0)
    Download_B.grid(row=4, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 4th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Google Maps", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=maps, relief=GROOVE, pady=0)
    Download_B.grid(row=5, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 5th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Weather Networks", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=weather, relief=GROOVE, pady=0)
    Download_B.grid(row=6, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 6th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Play Music", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#DFA27C', command=music, relief=GROOVE, pady=0)
    Download_B.grid(row=7, column=0, columnspan=2, sticky="ew", pady=0, padx=0)

#-----------------------------------------------------------------------------------------------------

def quit():
    global root
    root.quit()
    
def jellyfin():
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window http://192.168.111.100:8097/web/#/home.html &')
    root.quit()

def recipes():
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window http://192.168.111.100:8090/search/ &')
    root.quit()

def google():
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window https://www.google.com &')
    root.quit()

def maps():
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window https://www.google.com/maps &')
    root.quit()

def weather():
    os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window https://www.theweathernetwork.com/en/city/ca/ontario/ottawa/hourly &')
    root.quit()

def music():
    os.system('./.config/HyprV/waybar/scripts/mediaSwitch')
    root.quit()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()