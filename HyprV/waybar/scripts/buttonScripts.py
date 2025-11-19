import tkinter as tk
import os
import subprocess
import sys
from tkinter import *
from tkinter import messagebox, filedialog
from pathlib import Path

root = tk.Tk()
root.title("Scripts")
root.geometry('+50+806')
root.resizable(0, 0)
root.bind_all("<Escape>", lambda event: clean_exit())
root.bind_all("<Control_L>", lambda x: clean_exit())

# Key names
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html

os.system('bash "/home/$USER/Hyprland2.0/HyprV/waybar/scripts/buttonsKill" kill')

class ButtonSelectorWidget(tk.Frame):
    def __init__(self, parent, button_labels=None, command=None, **kwargs):
        super().__init__(parent, bg="#69878E", **kwargs)
        self.command = command
        self.buttons = []
        self.selected_index = 5 #Change this for default selected

        if button_labels is None:
            button_labels = [f"Button {i+1}" for i in range(7)] #Make sure this matches the selected labels
            button_labels[0] = "Play_Music"
            button_labels[1] = "Youtube-DL"
            button_labels[2] = "Rsync"
            button_labels[3] = "WireguardConf"
            button_labels[4] = "PrivadoConf"
            button_labels[5] = "HyprlandHighlightColor"
            button_labels[6] = "Luks"

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
                if label == "HyprlandHighlightColor":  # Optional condition for Firefox button customization
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
            if label == "Youtube-DL":
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

# Play_Music-------------------------------------------------------------------------------
        if label == "Play_Music":
            os.system('./.config/HyprV/waybar/scripts/mediaSwitch')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Youtube-DL-------------------------------------------------------------------------------
        if label == "Youtube-DL":
            os.system('python3 Hyprland2.0/Scripts/Python/YouTube-DL.py 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Rsync-------------------------------------------------------------------------------
        if label == "Rsync":
            os.system('python3 Hyprland2.0/Scripts/Python/Rsync.py 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# WireguardConf-------------------------------------------------------------------------------
        if label == "WireguardConf":
            os.system('python3 Hyprland2.0/Scripts/Python/WireguardConf.py 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# PrivadoConf-------------------------------------------------------------------------------
        if label == "PrivadoConf":
            os.system('python3 Hyprland2.0/Scripts/Python/PrivadoConf.py 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# HyprlandHighlightColor-------------------------------------------------------------------------------
        if label == "HyprlandHighlightColor":
            os.system('python3 Hyprland2.0/Scripts/Python/HyprlandHighlightColor.py 1>/dev/null &')
            os.system('bash Hyprland2.0/HyprV/waybar/scripts/buttonsKill')
            # clean_exit()
# Luks-------------------------------------------------------------------------------
        if label == "Luks":
            os.system('python3 Hyprland2.0/Scripts/Python/Luks.py 1>/dev/null &')
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