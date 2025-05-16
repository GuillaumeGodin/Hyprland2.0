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
root.title("Power")
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
        text="Update Packages", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=packages, 
        relief=GROOVE, 
        pady=0
    )
    File_1.grid (
        row=2, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=(0,0), 
        padx=0
    )
    # 2nd Row----------------------------------------------------------------------------------
    File_2 = Button (
        pane, 
        text="Update Configs", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=configs, 
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
        text="Logout", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=logout, 
        relief=GROOVE, 
        pady=0
    )
    File_3.grid (
        row=4, 
        column=0, 
        columnspan=2, 
        sticky="ew", 
        pady=(2,0),
        padx=0
    )
    # 4th Row----------------------------------------------------------------------------------
    File_4 = Button (
        pane, 
        text="Restart", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=restart, 
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
        text="Shutdown", 
        font=("JetBrainsMono", 14), 
        anchor="w", 
        bg="#222222", 
        fg="#FFFFFF", 
        highlightthickness=0, 
        activebackground='#ffbb00', 
        command=shutdown, 
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

#-----------------------------------------------------------------------------------------------------

def quit():
    global root
    root.quit()

def exit(e):
    os.system('hyprctl keyword unbind , mouse:273')
    root.destroy()

def packages():
    os.system('hyprctl keyword unbind , mouse:273')
    root.quit()
    os.system('kitty --title update-sys sh -c "yay -Syu" && pkill -RTMIN+8 waybar 1>/dev/null &')

def configs():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('kitty --hold  bash /home/$USER/Hyprland2.0/Bash/hyprlandConfigUpdate 1>/dev/null &')
    root.quit()
    
def logout():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('hyprctl dispatch exit 0')
    root.quit()

def restart():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('systemctl reboot')
    root.quit()

def shutdown():
    os.system('hyprctl keyword unbind , mouse:273')
    os.system('systemctl poweroff')
    root.quit()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()