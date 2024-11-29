# Hyprland2.0

1) Update Keys:

        pacman-key --init
        pacman-key --populate archlinux

2) Installing Arch:

        archinstall

        Archinstall language			English (100%)
        Mirrors
            Mirror region	                Canada
            Back				
        Locales
            Keyboard layout		        us
            Locale language		        en_US
            Locale encoding		        UTF-8
        Disk configuration                      Use a best-effort default partition layout
                                                    (Select main drive)
                                                        ext4
                                                            no
        Disk encryption                       (Leave Blank)
        Bootloader		                Grub or systemd-bootctl
        Unified Kernel Images		        True (for secure boot)
        swap					True
        Hostname			        archlinux
        Root password                          password
                                               password
        User account                           Add a user
                                                    user
                                                    password
                                                    password
                                               yes (make superuser)
                                               Confirm and exit
        Profile                                 Type
                                               Minimal
        Audio                                  pipewire
        Kernels			        linux (Dont change anything)
        Additional packages                    git vim nano
        Network configuration                   Use NetworkManager
        Timezone                               Canada/Estern
        Automatic time sync (NTP)		True
        Optional repositories                  multilib
        Install

Unplug the USB drive and select no (no post installation configurations)

        reboot

3) Instal Hyprland:

        Login                       user
                                    password
        git clone https://github.com/GuillaumeGodin/Hyprland2.0.git
        cd Hyprland2.0
        ./install

4) Setup Script

        1: Would you like to continue with the install? (y.n)
        (enter password)

        2: Would you like to disable WIFI powersave? (y.n)
        (turns off wifi powersave)

        3: Would you like to install packages? (y.n)
        (kitty, mako, waybar, thunar, ect...)

        4: Would you like to install office softwares? (y.n)
        (libreoffice, zim, blender, gimp, vscode, okular, timeshift, gparted, easyeffects, ect...)

        5: Would you like to install gaming softwares? (y.n)
        (steam, webcord, obs-studio, mangohud) 

        6: Would you like to copy config files? (y.n)
        (Copy configs and theming)

        7: Select measurement units, (m) for metric or (i) for imperial? (m.i)
        (Metric or Imperial)

        8: Select a background manager, (s) for swww or (h) for hyprpaper? (s.h)
        (swww is nicer but long downoad, hyprpaper works on most computers and is a short download)

        9: Would you like to activate the starship shell? (y.n)
        (for laptops)

        10: for Asus laptops – Would you like to install Asus software support? (y.n)
        (for asus laptops gpu profiles)

        11: Would you like to start Hyprland now? (y.n)
        (starts Hyprland)