import os
# from subprocess import Popen, PIPE
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

root = tk.Tk()
#root.geometry("600x140")
root.resizable(height = None, width = None)
root.resizable(0, 0)
root.title("Hyprland Highlight Color")
root.config(background="black")

def Widgets():

#    pane = Frame(root, bg="black")
    pane = Frame(root)    
    pane.pack(fill=X, expand=True)

    # 1st Row Header----------------------------------------------------------------------------------
    head_label = Label(pane, text="Hyprland Highlight Color", bg="orange", fg="white", font="SegoeUI 14", width=55)
#    head_label.pack(fill=X, expand=False, side=TOP)
    head_label.grid(row=0, column=0, columnspan=3, sticky="n")

    # 2nd Row Destination-----------------------------------------------------------------------------
    destination_label = Label(pane, text="Color Hex Code :", bg="white", font="Arial")
    destination_label.grid(row=3, column=0, sticky="enw")
    root.destinationText = Entry(pane, font="Arial", textvariable=hexColor)
    root.destinationText.insert(0, call)
    root.destinationText.grid(row=3, column=1, sticky="new")
    browse_B = Button(pane, text="Hyprpicker", bg="bisque", font="Arial", command=hyprpickerColor, pady=0, relief=GROOVE)
    browse_B.grid(row=3, column=2, sticky="wne")
    
    # 5th Row Button Audio----------------------------------------------------------------------------
    Download_Audio = Button(pane, text="Set Color", bg="thistle1", font="Arial", command=setColor, relief=GROOVE, pady=0)
    Download_Audio.grid(row=4, column=1, sticky="new", padx=60, pady=5)

# Source the bash script and echo the variable
def get_current_color():
    cmd = 'source /home/$USER/.config/hypr/currentVariables && echo $currentColor'
    result = subprocess.run(['bash', '-c', cmd], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

currentColor = get_current_color()
print(currentColor)

call = currentColor
print(call)

def hyprpickerColor():
    command = os.popen('hyprpicker | tail -c 7') #Selects the last 6 characters
    output = command.read()
    print(output[:6])
    hexColor.set(output[:6])

def setColor():
    
    os.system('sed -i "s/{}/{}/g" /home/$USER/.config/hypr/currentVariables'.format(currentColor, hexColor.get()))
    #hyprland (border)
    os.system('sed -i "s/{}/{}/g" .config/HyprV/hypr/hyprland.conf'.format(currentColor, hexColor.get()))
    # gtk (thunar)
    os.system('sed -i "s/{}/{}/g" .config/gtk-3.0/gtk.css'.format(currentColor, hexColor.get()))
    # wofi
    os.system('sed -i "s/{}/{}/g" .config/wofi/style.css'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/wofi/style/wofi_dark.css'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/wofi/style/wofi_light.css'.format(currentColor, hexColor.get()))
    # starship shell
    os.system('sed -i "s/{}/{}/g" .config/HyprV/starship/starship.toml'.format(currentColor, hexColor.get()))
    # waybar
    os.system('sed -i "s/{}/{}/g" .config/HyprV/waybar/style/waybar_dark.css'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/waybar/style/waybar_light.css'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/waybar/buttonApps.py'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/waybar/buttonScripts.py'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/waybar/buttonFiles.py'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/waybar/buttonPower.py'.format(currentColor, hexColor.get()))
    # wlogout
    os.system('sed -i "s/{}/{}/g" .config/HyprV/wlogout/style/wlogout_dark.css'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/wlogout/style/wlogout_light.css'.format(currentColor, hexColor.get()))
    # mako
    os.system('sed -i "s/{}/{}/g" .config/HyprV/mako/conf/mako_dark'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .config/HyprV/mako/conf/mako_light'.format(currentColor, hexColor.get()))
    os.system('makoctl reload')
    # firefox
    os.system('sed -i "s/{}/{}/g" .mozilla/firefox/*.default-release/chrome/userChrome.css'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .mozilla/firefox/*.default-release/chrome/userContent.css'.format(currentColor, hexColor.get()))
    # librewolf
    os.system('sed -i "s/{}/{}/g" .librewolf/*.default-default/chrome/userChrome.css'.format(currentColor, hexColor.get()))
    os.system('sed -i "s/{}/{}/g" .librewolf/*.default-default/chrome/userContent.css'.format(currentColor, hexColor.get()))

    # Restart Waybar
    os.system('hyprctl reload')
    quit()

# Creating the tkinter Variables
hexColor = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()