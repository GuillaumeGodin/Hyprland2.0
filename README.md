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
        Timezone                        Canada/Estern
        Automatic time sync (NTP)		True
        Optional repositories           multilib
        Install

Unplug the USB drive and select no (no post installation configurations)

reboot

3) Instalyprland
    Login                               user
                                        password
    git clone https://github.com/GuillaumeGodin/Hyprland2.0.git
    cd Hyprland2.0
    ./set-hypr

4) Setup Script
    (To be continued...)
