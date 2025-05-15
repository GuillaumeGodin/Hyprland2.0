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
root.title("Power")
root.configure(bg="#222222")
root.bind("<Escape>", lambda x: root.destroy())

def Widgets():

    # pane = Frame(root, bg="black")
    pane = Frame(root)    
    pane.pack(fill=X, expand=True)

    # 1st Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Logout", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=logout, relief=GROOVE, pady=0)
    Download_B.grid(row=2, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 2nd Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Restart", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=restart, relief=GROOVE, pady=0)
    Download_B.grid(row=3, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 3rd Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Shutdown", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=shutdown, relief=GROOVE, pady=0)
    Download_B.grid(row=4, column=0, columnspan=2, sticky="ew", pady=0, padx=0)
    # 4th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Update Packages", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=packages, relief=GROOVE, pady=0)
    Download_B.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(5,0), padx=0)
    # 5th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Update Configs", font=("JetBrainsMono", 14), anchor="w", bg="#222222", fg="#FFFFFF", highlightthickness=0, activebackground='#ffbb00', command=configs, relief=GROOVE, pady=0)
    Download_B.grid(row=6, column=0, columnspan=2, sticky="ew", pady=0, padx=0)

#-----------------------------------------------------------------------------------------------------

def quit():
    global root
    root.quit()
    
def logout():
    os.system('hyprctl dispatch exit 0')
    root.quit()

def restart():
    os.system('systemctl reboot')
    root.quit()

def shutdown():
    os.system('systemctl poweroff')
    root.quit()

def packages():
    root.quit()
    os.system('kitty --title update-sys sh -c "yay -Syu" && pkill -RTMIN+8 waybar 1>/dev/null &')

def configs():
    os.system('kitty --hold  bash /home/$USER/Hyprland2.0/Bash/hyprlandConfigUpdate 1>/dev/null &')
    root.quit()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()