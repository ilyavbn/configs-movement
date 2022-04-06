import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import ImageTk, Image

username = os.environ.get('SUDO_USER', os.environ.get('USERNAME'))
HOME = os.path.expanduser(f'~{username}')
ROOT = os.path.expanduser('~')

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        ##Basic window configuration
        self.title("Configs_demo")
        self.geometry("390x360")
        self.resizable(False, False)
        self.iconphoto(False, tk.PhotoImage(file="../res/img/auto_replace.png"))
        self.configure(bg="#E0E0E0")


        ##Auto add configs button settings
        auto_add_img = PhotoImage(file = "../res/img/auto_replace.png")
        auto_add_configs_button = Button(self, image=auto_add_img, borderwidth=0,
                                         bg="#E0E0E0")
        auto_add_configs_button.image = auto_add_img
        auto_add_configs_button.pack()
        auto_add_configs_button.place(x=48, y=56)

        ##Manual add configs button settings
        manual_add_img = PhotoImage(file = "../res/img/manual_replace.png")
        manual_add_configs_button = Button(self, image=manual_add_img, borderwidth=0,
                                           command=self.open_window, bg="#E0E0E0")
        manual_add_configs_button.image = manual_add_img
        manual_add_configs_button.pack()
        manual_add_configs_button.place(x=219, y=56)

        ##Help button 
        help_image = PhotoImage(file = "../res/img/help_1.png")
        help_button = Button(self, image=help_image, borderwidth=0,
                             bg="#E0E0E0",highlightbackground="#E0E0E0")
        help_button.image = help_image
        help_button.pack()
        help_button.place(x=77, y=246)

        ##Dump configs button
        backup_image = PhotoImage(file = "../res/img/backup_1.png")
        backup_button = Button(self, image=backup_image,borderwidth=0,
                               bg="#E0E0E0",highlightbackground="#E0E0E0")
        backup_button.image = backup_image
        backup_button.pack()
        backup_button.place(x=248, y=246)



    def open_window(self):
        manual_window = ManualWindow(self)
        manual_window.grab_set()



class ManualWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Manual_configuration")
        self.iconphoto(False, tk.PhotoImage(file="../res/img/manual_replace.png"))
        self.geometry("644x514")
        self.resizable(False, False)
        self.configure(bg="#E0E0E0")

        ##Images
        nvim_img=PhotoImage(file="../res/img/neovim.png")
        alacritty_img=PhotoImage(file="../res/img/alacritty.png")
        dhclient_img=PhotoImage(file="../res/img/dhclient.png")
        mime_img=PhotoImage(file="../res/img/mime.png")
        ssh_img=PhotoImage(file="../res/img/ssh.png")
        vim_img=PhotoImage(file="../res/img/vimrc.png")
        fstab_img=PhotoImage(file="../res/img/fstab.png")
        hostname_img=PhotoImage(file="../res/img/hostname.png")
        sudoers_img=PhotoImage(file="../res/img/sudoers.png")
        x11_img=PhotoImage(file="../res/img/x11.png")
        gitconfig_img=PhotoImage(file="../res/img/gitconfig.png")
        hosts_img=PhotoImage(file="../res/img/hosts.png")
        profile_img=PhotoImage(file="../res/img/profile.png")
        sysconfig_img=PhotoImage(file="../res/img/sysconfig.png")
        xinitrc_img=PhotoImage(file="../res/img/xinitrc.png")
        bashrc_img=PhotoImage(file="../res/img/bashrc.png")
        grub_img=PhotoImage(file="../res/img/grub.png")
        resolv_img=PhotoImage(file="../res/img/resolv.png")
        timezone_img=PhotoImage(file="../res/img/timezone.png")
        editor_img = PhotoImage(file="../res/img/editor.png")

        ## Nvim
        nvim_btn = Button(self, image=nvim_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        nvim_btn.image=nvim_img
        nvim_btn.pack()
        nvim_btn.place(x=24,y=24)

        ## Alacritty
        alacritty_btn = Button(self, image=alacritty_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        alacritty_btn.image=alacritty_img
        alacritty_btn.pack()
        alacritty_btn.place(x=272,y=24)

        ## Dhclient
        dhclient_btn = Button(self, image=dhclient_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        dhclient_btn.image=dhclient_img
        dhclient_btn.pack()
        dhclient_btn.place(x=148, y=142)

        ## Mime
        mime_btn = Button(self, image=mime_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        mime_btn.image=mime_img
        mime_btn.pack()
        mime_btn.place(x=24, y=266)

        ## SSH
        ssh_btn = Button(self, image=ssh_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        ssh_btn.image=ssh_img
        ssh_btn.pack()
        ssh_btn.place(x=272, y=266)

        ## Vimrc
        vimrc_btn = Button(self, image=vim_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        vimrc_btn.image=vim_img
        vimrc_btn.pack()
        vimrc_btn.place(x=396, y=24)

        ## Fstab
        fstab_btn = Button(self, image=fstab_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        fstab_btn.image=fstab_img
        fstab_btn.pack()
        fstab_btn.place(x=272, y=142)

        ## Hostname
        hostname_btn = Button(self, image=hostname_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        hostname_btn.image=hostname_img
        hostname_btn.pack()
        hostname_btn.place(x=396, y=142)

        ## Sudoers
        sudoers_btn = Button(self, image=sudoers_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        sudoers_btn.image=sudoers_img
        sudoers_btn.pack()
        sudoers_btn.place(x=20, y=390)

        ## x11
        x11_btn = Button(self, image=x11_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        x11_btn.image=x11_img
        x11_btn.pack()
        x11_btn.place(x=396, y=266)

        ## Gitconfig
        gitconfig_btn = Button(self, image=gitconfig_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        gitconfig_btn.image=gitconfig_img
        gitconfig_btn.pack()
        gitconfig_btn.place(x=516, y=390)

        ## Hosts
        hosts_btn = Button(self, image=hosts_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        hosts_btn.image=hosts_img
        hosts_btn.pack()
        hosts_btn.place(x=520, y=142)

        ## Profile
        profile_btn = Button(self, image=profile_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        profile_btn.image=profile_img
        profile_btn.pack()
        profile_btn.place(x=24, y=142)

        ## Sysconfig
        sysconfig_btn = Button(self, image=sysconfig_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        sysconfig_btn.image=sysconfig_img
        sysconfig_btn.pack()
        sysconfig_btn.place(x=520, y=266)

        ## Xinitrc
        xinitrc_btn = Button(self, image=xinitrc_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        xinitrc_btn.image=xinitrc_img
        xinitrc_btn.pack()
        xinitrc_btn.place(x=268, y=390)

        ## Bashrc
        bashrc_btn = Button(self, image=bashrc_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        bashrc_btn.image=bashrc_img
        bashrc_btn.pack()
        bashrc_btn.place(x=148, y=24)

        ## Grub
        grub_btn = Button(self, image=grub_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        grub_btn.image=grub_img
        grub_btn.pack()
        grub_btn.place(x=144, y=390)

        ## Resolv
        resolv_btn = Button(self, image=resolv_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0")
        resolv_btn.image=resolv_img
        resolv_btn.pack()
        resolv_btn.place(x=520, y=24)

        ## Timezone
        timezone_btn = Button(self, image=timezone_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0",
                            command=lambda: changeFile("timezone"))
        timezone_btn.image=timezone_img
        timezone_btn.pack()
        timezone_btn.place(x=148, y=266)

        ## editor
        editor_btn = Button(self, image=editor_img, borderwidth=0,
                                         bg="#E0E0E0",highlightbackground="#E0E0E0",
                            command=lambda: changeFile("editor"))
        editor_btn.image=editor_img
        editor_btn.pack()
        editor_btn.place(x=392, y=390)

        ## FILES WORKING FUNCS
        def changeFile(btn_name):

            src = fd.askopenfilename()

            match btn_name:
                case "editor":
                    dst = HOME+"/.editor"
                    shutil.copy(src, dst)
                case "timezone":
                    dst = "/etc/timezone"
                    shutil.copy(src, dst)
                case "resolv":
                    dst ="/etc/resolv.conf"
                    shutil.copy(src, dst)
                case "neovim":
                    dst =HOME + "/.config/nvim/init.vim"
                    shutil.copy(src, dst)
                case "bashrc":
                    dst =HOME + "/.bashrc"
                    shutil.copy(src, dst)
                case "alacritty":
                    dst =HOME + "/.config/alacritty/alacritty.yml"
                    shutil.copy(src, dst)
                case "vimrc":
                    dst =HOME + "/.vimrc"
                    shutil.copy(src, dst)
                case "profile":
                    dst ="/etc/profile"
                    shutil.copy(src, dst)
                case "dhclient":
                    dst ="/etc/dhcp/dhclient.conf"
                    shutil.copy(src, dst)
                case "fstab":
                    dst ="/etc/fstab"
                    shutil.copy(src, dst)
                case "hostname":
                    dst ="/etc/hostname"
                    shutil.copy(src, dst)
                case "hosts":
                    dst ="/etc/hosts"
                    shutil.copy(src, dst)
                case "mime":
                    dst ="/etc/mime.types"
                    shutil.copy(src, dst)
                case "ssh":
                    dst =HOME + "/.ssh/config"
                    shutil.copy(src, dst)
                case "x11":
                    dst ="/etc/X11/xorg.conf"
                    shutil.copy(src, dst)
                case "sysconfig":
                    # dst ="/etc/fstab"
                    # shutil.copy(src, dst)
                    print("Я не сделал")
                case "sudoers":
                    dst ="/etc/sudoers"
                    shutil.copy(src, dst)
                case "grub":
                    dst ="/etc/default/grub"
                    shutil.copy(src, dst)
                case "xinitrc":
                    dst =HOME + "/.xinitrc"
                    shutil.copy(src, dst)
                case "gitconfig":
                    dst =HOME + "/gitconfig"
                    shutil.copy(src, dst)















app = App()
app.mainloop()
