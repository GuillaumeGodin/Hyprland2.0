import tkinter as tk
import os
import subprocess
import sys
from tkinter import *
from tkinter import messagebox, filedialog
from pathlib import Path

root = tk.Tk()
root.title("Apps")
root.geometry('+150+587')
root.resizable(0, 0)
root.bind_all("<Escape>", lambda event: clean_exit())
root.bind_all("<Super_L>", lambda x: clean_exit())

# Key names
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html

os.system('bash "/home/$USER/Hyprland2.0/HyprV/waybar/scripts/buttonsKill" kill')

class ButtonSelectorWidget(tk.Frame):
    def __init__(self, parent, button_labels=None, command=None, **kwargs):
        super().__init__(parent, bg="#69878E", **kwargs)
        self.command = command
        self.buttons = []
        self.selected_index = 7 #Change this for default selected

        if button_labels is None:
            button_labels = [f"Button {i+1}" for i in range(14)] #Make sure this matches the selected labels
            button_labels[0] = "Notes"
            button_labels[1] = "Calculator"
            button_labels[2] = "LibreOffice"
            button_labels[3] = "Audacity"
            button_labels[4] = "Handbrake"
            button_labels[5] = "MediaInfo"
            button_labels[6] = "MkvTool"
            button_labels[7] = "   Firefox"
            button_labels[8] = "󰇰   Mail_Evolution"
            button_labels[9] = "   Steam"
            button_labels[10] = "   Discord"
            button_labels[11] = "   Gimp"
            button_labels[12] = "   Blender"
            button_labels[13] = "   Terminal_Kitty"

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
                    btn.configure(bg="#69878E", fg="#000000")  # Text black for Firefox
                else:
                    btn.configure(bg="#69878E", fg="#000000")  # Text black for other selected buttons
            else:
                btn.configure(bg="#222222", fg="#EEEEFF")  # Default white text for unselected buttons

    def create_buttons(self, labels):
        for i, label in enumerate(labels):
            btn = tk.Button(
                self,
                text=label,
                font=("JetBrainsMono", 12),
                width=20,
                anchor="sw",
                bg="#222222",  # unselected background color
                fg="#EEEEFF",  # unselected writing color
                highlightthickness=0, 
                activebackground="#69878E", 
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
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Calculator-------------------------------------------------------------------------------
        if label == "Calculator":
            os.system('galculator 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# LibreOffice-------------------------------------------------------------------------------
        if label == "LibreOffice":
            os.system('libreoffice 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Audacity-------------------------------------------------------------------------------
        if label == "Audacity":
            os.system('audacity 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Handbrake-------------------------------------------------------------------------------
        if label == "Handbrake":
            os.system('ghb 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# MediaInfo-------------------------------------------------------------------------------
        if label == "MediaInfo":
            os.system('mediainfo-gui 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# MkvTool-------------------------------------------------------------------------------
        if label == "MkvTool":
            os.system('mkvtoolnix-gui 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Firefox-------------------------------------------------------------------------------
        if label == "   Firefox":
            os.system('firefox --no-terminal 2>/dev/null 1>/dev/null --new-window &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Mail_Evolution-------------------------------------------------------------------------------
        if label == "󰇰   Mail_Evolution":
            os.system('evolution 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Steam-------------------------------------------------------------------------------
        if label == "   Steam":
            os.system('steam 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Discord-------------------------------------------------------------------------------
        if label == "   Discord":
            os.system('discord 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Gimp-------------------------------------------------------------------------------
        if label == "   Gimp":
            os.system('gimp 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Blender-------------------------------------------------------------------------------
        if label == "   Blender":
            os.system('blender -p 1920 1080 1280 720 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Terminal_Kitty-------------------------------------------------------------------------------
        if label == "   Terminal_Kitty":
            os.system('kitty 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()

        if self.command:
            self.command(label)

    def on_mouse_click(self, index):
        self.selected_index = index
        self.highlight_selected()
        self.press_selected()
    
def clean_exit():
    root.destroy()

# --- Example usage ---
def on_button_pressed(label):
    print(f"Callback: {label}")

selector = ButtonSelectorWidget(root, command=on_button_pressed)
selector.pack(padx=0, pady=0)

root.mainloop()