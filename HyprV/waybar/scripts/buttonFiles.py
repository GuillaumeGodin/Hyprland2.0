import tkinter as tk
import os
import subprocess
from tkinter import *
from tkinter import messagebox, filedialog
from pathlib import Path

root = tk.Tk()
root.title("Files")
root.geometry('+225+731')
root.resizable(height = None, width = None)
root.resizable(0, 0)
root.bind("<Escape>", lambda x: exit())
root.bind("<Alt_L>", lambda x: exit())

# Key names
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html

# os.system('hyprctl dispatch killwindow class:Tk')
os.system('bash Hyprland2.0/Bash/killDropdowns')

# os.system('hyprctl keyword unbind , mouse:273')
os.system('hyprctl keyword bind , mouse:273, exec, bash Hyprland2.0/Bash/killDropdowns')

os.system('hyprctl keyword unbind ALT, ALT_L')
os.system('hyprctl keyword bindr ALT, ALT_L, exec, bash Hyprland2.0/Bash/killDropdowns')

# os.system('hyprctl keyword unbind , escape')
os.system('hyprctl keyword bind , escape, exec, bash Hyprland2.0/Bash/killDropdowns')

class ButtonSelectorWidget(tk.Frame):
    def __init__(self, parent, button_labels=None, command=None, **kwargs):
        super().__init__(parent, bg="#ffbb00", **kwargs)
        self.command = command
        self.buttons = []
        self.selected_index = 4

        if button_labels is None:
            button_labels = [f"Button {i+1}" for i in range(10)]
            button_labels[0] = "md0_ET"
            button_labels[1] = "md0_GG"
            button_labels[2] = "md0_Media"
            button_labels[3] = "   Desktop"
            button_labels[4] = "󰈙   Documents"
            button_labels[5] = "   Downloads"
            button_labels[6] = "   Music"
            button_labels[7] = "   Pictures"
            button_labels[8] = "   Videos"
            button_labels[9] = "   Trash"

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
                width=12,
                anchor="sw",
                bg="#222222",  # unselected background color
                fg="#FFFFFF",  # unselected writing color
                highlightthickness=0, 
                activebackground="#ffbb00", 
                activeforeground="#000000",
                relief=GROOVE,
            )
            
            # Apply custom padding for specific buttons
            if label == "   Desktop" or label == "   Trash":
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

# md0_ET-------------------------------------------------------------------------------
        if label == "md0_ET":
            os.system('thunar /home/$USER/mnt/md0/ET/ 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()
# md0_GG-------------------------------------------------------------------------------
        if label == "md0_GG":
            os.system('thunar /home/$USER/mnt/md0/Guillaume/ 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()
# md0_Media-------------------------------------------------------------------------------
        if label == "md0_Media":
            os.system('thunar /home/$USER/mnt/md0/Media/ 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()
# Desktop-------------------------------------------------------------------------------
        if label == "   Desktop":
            os.system('thunar /home/$USER/Desktop 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()
# Documents-------------------------------------------------------------------------------
        if label == "󰈙   Documents":
            os.system('thunar /home/$USER/Documents 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()
# Downloads-------------------------------------------------------------------------------
        if label == "   Downloads":
            os.system('thunar /home/$USER/Downloads 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()
# Music-------------------------------------------------------------------------------
        if label == "   Music":
            os.system('thunar /home/$USER/Music 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()
# Pictures-------------------------------------------------------------------------------
        if label == "   Pictures":
            os.system('thunar /home/$USER/Pictures 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()
# Videos-------------------------------------------------------------------------------
        if label == "   Videos":
            os.system('thunar /home/$USER/Videos 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()
# Trash-------------------------------------------------------------------------------
        if label == "   Trash":
            os.system('thunar trash:/// 1>/dev/null &')
            os.system('bash Hyprland2.0/Bash/killDropdowns')
            exit()

        if self.command:
            self.command(label)

    def on_mouse_click(self, index):
        self.selected_index = index
        self.highlight_selected()
        self.press_selected()
    
    def exit():
        # os.system('hyprctl keyword unbind SUPER, SUPER_L')
        os.system('bash Hyprland2.0/Bash/killDropdowns')
        root.destroy()

# --- Example usage ---
def on_button_pressed(label):
    print(f"Callback: {label}")

selector = ButtonSelectorWidget(root, command=on_button_pressed)
selector.pack(padx=0, pady=0)

root.mainloop()