import tkinter as tk
import os
import subprocess
import sys
from tkinter import *
from tkinter import messagebox, filedialog
from pathlib import Path

root = tk.Tk()
root.title("Apps")
root.geometry("+150+557")
# root.resizable(height = None, width = None)
root.resizable(0, 0)
root.bind_all("<Escape>", lambda event: clean_exit())
root.bind_all("<Super_L>", lambda x: clean_exit())

# Key names
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html

os.system('bash "/home/$USER/Hyprland2.0/Bash/killDropdowns" kill')

# os.system('hyprctl keyword unbind , mouse:273')
os.system('hyprctl keyword bind , mouse:273, exec, bash "/home/$USER/Hyprland2.0/Bash/killDropdowns" kill')

os.system('hyprctl keyword unbind SUPER, SUPER_L')
os.system('hyprctl keyword bind SUPER, SUPER_L, exec, bash "/home/$USER/Hyprland2.0/Bash/killDropdowns" kill')

# os.system('hyprctl keyword unbind , escape')
# os.system('hyprctl keyword bind , escape, exec, bash "/home/$USER/Hyprland2.0/Bash/killDropdowns" kill')

class ButtonSelectorWidget(tk.Frame):
    def __init__(self, parent, button_labels=None, command=None, **kwargs):
        super().__init__(parent, bg="#ffbb00", **kwargs)
        self.command = command
        self.buttons = []
        self.selected_index = 9

        if button_labels is None:
            button_labels = [f"Button {i+1}" for i in range(16)]
            button_labels[0] = "Notes"
            button_labels[1] = "Calculator"
            button_labels[2] = "LibreOffice"
            button_labels[3] = "Audacity"
            button_labels[4] = "Handbrake"
            button_labels[5] = "MediaInfo"
            button_labels[6] = "MkvTool"
            button_labels[7] = "MkvToolBatch"
            button_labels[8] = "Work_Mode"
            button_labels[9] = "   Firefox"
            button_labels[10] = "󰇰   Mail_Evolution"
            button_labels[11] = "   Steam"
            button_labels[12] = "   Discord"
            button_labels[13] = "   Gimp"
            button_labels[14] = "   Blender"
            button_labels[15] = "   Terminal_Kitty"

        self.create_buttons(button_labels)
        self.highlight_selected()

        self.bind_all("<Up>", self.move_up)
        self.bind_all("<Down>", self.move_down)
        self.bind_all("<Return>", self.press_selected)
        self.bind_all("<KP_Enter>", self.press_selected)
        

    def highlight_selected(self):
        for i, btn in enumerate(self.buttons):
            label = btn.cget("text")
            if i == self.selected_index:
                if label == "   Firefox":  # Optional condition for Firefox button customization
                    btn.configure(bg="#ffbb00", fg="#000000")  # Text black for Firefox
                else:
                    btn.configure(bg="#ffbb00", fg="#000000")  # Text black for other selected buttons
            else:
                btn.configure(bg="#222222", fg="#FFFFFF")  # Default white text for unselected buttons

    def create_buttons(self, labels):
        for i, label in enumerate(labels):
            btn = tk.Button(
                self,
                text=label,
                font=("JetBrainsMono", 12),
                width=20,
                anchor="sw",
                bg="#222222",  # unselected background color
                fg="#FFFFFF",  # unselected writing color
                highlightthickness=0, 
                activebackground="#ffbb00", 
                activeforeground="#000000",
                relief=GROOVE,
            )
            
            # Apply custom padding for specific buttons
            if label == "LibreOffice" or label == "   Firefox":
                btn.pack(pady=(2, 0))
            else:
                btn.pack(pady=0)
            
            btn.bind("<Button-1>", lambda e, idx=i: self.on_mouse_click(idx))
            self.buttons.append(btn)

    def move_up(self, event=None):
        if self.selected_index > 0:
            self.selected_index -= 1
            self.highlight_selected()

    def move_down(self, event=None):
        if self.selected_index < len(self.buttons) - 1:
            self.selected_index += 1
            self.highlight_selected()

    def press_selected(self, event=None):
        label = self.buttons[self.selected_index].cget("text")
        print(f"You pressed {label}")
# Notes-------------------------------------------------------------------------------
        if label == "Notes":
            os.system('zim --geometry 1000x600 1>/dev/null &')
            clean_exit()
# Calculator-------------------------------------------------------------------------------
        if label == "Calculator":
            os.system('galculator 1>/dev/null &')
            clean_exit()
# LibreOffice-------------------------------------------------------------------------------
        if label == "LibreOffice":
            os.system('libreoffice 1>/dev/null &')
            clean_exit()
# Audacity-------------------------------------------------------------------------------
        if label == "Audacity":
            os.system('audacity 1>/dev/null &')
            clean_exit()
# Handbrake-------------------------------------------------------------------------------
        if label == "Handbrake":
            os.system('ghb 1>/dev/null &')
            clean_exit()
# MediaInfo-------------------------------------------------------------------------------
        if label == "MediaInfo":
            os.system('mediainfo-gui 1>/dev/null &')
            clean_exit()
# MkvTool-------------------------------------------------------------------------------
        if label == "MkvTool":
            os.system('mkvtoolnix-gui 1>/dev/null &')
            clean_exit()
# MkvToolBatch-------------------------------------------------------------------------------
        if label == "MkvToolBatch":
            os.system('python Documents/MKV_Batch/main.py 1>/dev/null &')
            clean_exit()
# Work_Mode-------------------------------------------------------------------------------
        if label == "Work_Mode":
            os.system('lan-mouse 1>/dev/null &')
            os.system('onedrivegui 1>/dev/null &')
            clean_exit()
# Firefox-------------------------------------------------------------------------------
        if label == "   Firefox":
            os.system('firefox --no-terminal 2&>1 1>/dev/null --new-window &')
            clean_exit()
# Mail_Evolution-------------------------------------------------------------------------------
        if label == "󰇰   Mail_Evolution":
            os.system('evolution 1>/dev/null &')
            clean_exit()
# Steam-------------------------------------------------------------------------------
        if label == "   Steam":
            os.system('steam 1>/dev/null &')
            clean_exit()
# Discord-------------------------------------------------------------------------------
        if label == "   Discord":
            os.system('discord 1>/dev/null &')
            clean_exit()
# Gimp-------------------------------------------------------------------------------
        if label == "   Gimp":
            os.system('gimp 1>/dev/null &')
            clean_exit()
# Blender-------------------------------------------------------------------------------
        if label == "   Blender":
            os.system('blender -p 1920 1080 1280 720 1>/dev/null &')
            clean_exit()
# Terminal_Kitty-------------------------------------------------------------------------------
        if label == "   Terminal_Kitty":
            os.system('kitty 1>/dev/null &')
            clean_exit()

        if self.command:
            self.command(label)

    def on_mouse_click(self, index):
        self.selected_index = index
        self.highlight_selected()
        self.press_selected()
    
def clean_exit():
    # os.system('bash Hyprland2.0/Bash/killDropdowns bind')
    # os.system('hyprctl dispatch killwindow class:Tk')
    root.destroy()
    # sys.exit()

# --- Example usage ---
def on_button_pressed(label):
    print(f"Callback: {label}")

selector = ButtonSelectorWidget(root, command=on_button_pressed)
selector.pack(padx=0, pady=0)

root.mainloop()