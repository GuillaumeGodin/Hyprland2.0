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
root.title("Privado")
root.config(background="black")

def Widgets():

    #    pane = Frame(root, bg="black")
    pane = Frame(root)    
    pane.pack(fill=X, expand=True)

    # 1st Row Header---------------------------------------------------------------------------------
    head_label = Label(pane, text="Privado", bg="yellow", font="SegoeUI 14", fg="black", width=85)
    head_label.grid(row=0, column=0, columnspan=4, sticky="n")

    # 2nd Row origin----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Download Configs", font="Arial", bg="thistle1", command=downloadConfigs, relief=GROOVE, pady=0)
    Download_B.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5, padx=20)
    Download_B = Button(pane, text="See Configs", font="Arial", bg="thistle1", command=seeConfigs, relief=GROOVE, pady=0)
    Download_B.grid(row=2, column=2, columnspan=2, sticky="we", pady=5, padx=20)

    # 3rd Row--------------------------------------------------------------------------------
    origin_label = Label(pane, text=".ovpn", bg="white", font="Arial")
    origin_label.grid(row=3, column=0, sticky="enw")
    root.originText = Entry(pane, textvariable=from_Path, font="Arial", width=45)
    root.originText.grid(row=3, column=1, columnspan=2, sticky="new")
    browse_B = Button(pane, text="Browse", bg="bisque", font="Arial", command=Browse_From, relief=GROOVE, pady=0)
    browse_B.grid(row=3, column=3, sticky="wne")

    # 4th Row--------------------------------------------------------------------------------
    origin_label = Label(pane, text="Rename :", bg="white", font="Arial")
    origin_label.grid(row=4, column=0, sticky="enw")
    root.originText = Entry(pane, textvariable=rename, font="Arial", width=45)
    root.originText.grid(row=4, column=1, columnspan=3, sticky="new")

    # 5th Row--------------------------------------------------------------------------------
    origin_label = Label(pane, text="Sudo :", bg="white", font="Arial")
    origin_label.grid(row=5, column=0, sticky="enw")
    root.originText = Entry(pane, textvariable=password, show='-', font="Arial", width=45)
    root.originText.grid(row=5, column=1, columnspan=3, sticky="new")

    # 5th Row--------------------------------------------------------------------------------
    root.privadoUser = Entry(pane, textvariable=privadoUser, font="Arial", width=45)
    root.privadoUser.grid(row=6, column=0, columnspan=2, sticky="ew", pady=5, padx=20)
    root.privadoUser.insert(0, "privado username")
    root.privadoPass = Entry(pane, textvariable=privadoPass, font="Arial", width=45)
    root.privadoPass.grid(row=6, column=2, columnspan=2, sticky="we", pady=5, padx=20)
    root.privadoPass.insert(0, "privado password")

    # 7th Row----------------------------------------------------------------------------------
    Download_B = Button(pane, text="Add Config", font="Arial", bg="thistle1", command=addConfig, relief=GROOVE, pady=0)
    Download_B.grid(row=7, column=0, columnspan=2, sticky="ew", pady=5, padx=20)
    Download_B = Button(pane, text="Restart Network Manager", font="Arial", bg="thistle1", command=restartNetworkManager, relief=GROOVE, pady=0)
    Download_B.grid(row=7, column=2, columnspan=2, sticky="we", pady=5, padx=20)

#-----------------------------------------------------------------------------------------------------
def Browse_From():
    download_Directory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH", title="From Folder")
    from_Path.set(download_Directory)


def downloadConfigs():
    os.system('rm -r /home/$USER/privadovpn')
    os.system("mkdir ~/privadovpn && wget -q -O ~/privadovpn/configs.zip https://privadovpn.com/apps/ovpn_configs.zip && unzip -q ~/privadovpn/configs.zip -d ~/privadovpn && rm ~/privadovpn/configs.zip && rename 's/default/udp/' ~/privadovpn/*default* && rename 's/tcp-scramble/tcp/' ~/privadovpn/*scramble* && sed -i 's/scramble/#scramble/g' ~/privadovpn/*tcp* && sed -i 's/3074/443/g' ~/privadovpn/*tcp* && sudo mv ~/privadovpn /etc/openvpn/")

def seeConfigs():
    os.system('firefox https://app.privadovpn.com/en/server-list')

def addConfig():
    #make copy and rename file
    os.system('cp {} /home/$USER/privadovpn/{}.default.ovpn'.format(from_Path.get(), rename.get()))
    #modify line 15, 19 & 20
    os.system('sed -i "/route 0.0.0.0 0.0.0.0 vpn_gateway/c #route 0.0.0.0 0.0.0.0 vpn_gateway" /home/$USER/privadovpn/{}.default.ovpn'.format(rename.get()))
    os.system('sed -i "/# data-ciphers AES-256-CBC/c data-ciphers AES-256-CBC" /home/$USER/privadovpn/{}.default.ovpn'.format(rename.get()))
    os.system('sed -i "/# data-ciphers-fallback AES-256-CBC/c data-ciphers-fallback AES-256-CBC" /home/$USER/privadovpn/{}.default.ovpn'.format(rename.get()))
    #add conf to NetworkManager
    os.system('nmcli connection import type openvpn file /home/$USER/privadovpn/{}.default.ovpn'.format(rename.get()))
    #modify NetworkManager entry
    os.system('echo {} | sudo -S sed -i "/password-flags=1/c password-flags=0" /etc/NetworkManager/system-connections/{}.default.nmconnection'.format(password.get(), rename.get()))
    os.system('echo {} | sudo -S sed -i "/data-ciphers=AES-256-CBC/c #data-ciphers=AES-256-CBC" /etc/NetworkManager/system-connections/{}.default.nmconnection'.format(password.get(), rename.get()))
    os.system('echo {} | sudo -S sed -i "/type=vpn/c type=vpn\\nautoconnect=false" /etc/NetworkManager/system-connections/{}.default.nmconnection'.format(password.get(), rename.get()))
    os.system('echo {} | sudo -S sed -i "/service-type=org.freedesktop.NetworkManager.openvpn/c service-type=org.freedesktop.NetworkManager.openvpn\\nusername={}\\n\\n[vpn-secrets]\\npassword={}" /etc/NetworkManager/system-connections/{}.default.nmconnection'.format(password.get(), privadoUser.get(), privadoPass.get(), rename.get()))
    #delete privado folder
    os.system('rm -r /home/$USER/privadovpn')
    #clear history
    #os.system('history -c')

def restartNetworkManager():
    os.system('systemctl restart NetworkManager')

from_Path = StringVar()
rename = StringVar()
password = StringVar()
privadoUser = StringVar()
privadoPass = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()