import os
import shutil
from tkinter import filedialog as fd

username = os.environ.get('SUDO_USER', os.environ.get('USERNAME'))
HOME = os.path.expanduser(f'~{username}')

sources =   [HOME+"/.editor",  "/etc/timezone", HOME+"/.config/nvim/init.vim",
            HOME+"/.bashrc", "/etc/default/grub",
           "/etc/resolv.conf", HOME+"/.config/alacritty/alacritty.yml",
            HOME+"/.vimrc","/etc/profile", "/etc/dhcp/dhclient.conf",
            "/etc/fstab", "/etc/hostname","/etc/hosts",
            "/etc/mime.types", "/etc/mime.types","/etc/X11/xorg.conf",
            "/etc/sudoers", HOME+"/.xinitrc", HOME+"/gitconfig",
            HOME+"/Documents/tested1.log" ]
def changeFile(name):
    src = HOME+"/testdisk.log"
    filenames = []
    for i in sources:
        filenames.append(os.path.basename(i))
        for j in filenames:
                if j == name:
                    shutil.copy(src,i)


def dumpFiles(sources):
    dst = fd.askdirectory()
    for i in sources:
        try:
            shutil.copy(i,dst)
        except FileNotFoundError:
            print("File {0} not found".format(i))
dumpFiles(sources)
##changeFile("tested1.log")



            # match btn_name:
                # case "editor":
                    # dst = HOME+"/.editor"
                    # shutil.copy(src, dst)
                # case "timezone":
                    # dst = "/etc/timezone"
                    # shutil.copy(src, dst)
                # case "resolv":
                    # dst ="/etc/resolv.conf"
                    # shutil.copy(src, dst)
                # case "neovim":
                    # dst =HOME + "/.config/nvim/init.vim"
                    # shutil.copy(src, dst)
                # case "bashrc":
                    # dst =HOME + "/.bashrc"
                    # shutil.copy(src, dst)
                # case "alacritty":
                    # dst =HOME + "/.config/alacritty/alacritty.yml"
                    # shutil.copy(src, dst)
                # case "vimrc":
                    # dst =HOME + "/.vimrc"
                    # shutil.copy(src, dst)
                # case "profile":
                    # dst ="/etc/profile"
                    # shutil.copy(src, dst)
                # case "dhclient":
                    # dst ="/etc/dhcp/dhclient.conf"
                    # shutil.copy(src, dst)
                # case "fstab":
                    # dst ="/etc/fstab"
                    # shutil.copy(src, dst)
                # case "hostname":
                    # dst ="/etc/hostname"
                    # shutil.copy(src, dst)
                # case "hosts":
                    # dst ="/etc/hosts"
                    # shutil.copy(src, dst)
                # case "mime":
                    # dst ="/etc/mime.types"
                    # shutil.copy(src, dst)
                # case "ssh":
                    # dst =HOME + "/.ssh/config"
                    # shutil.copy(src, dst)
                # case "x11":
                    # dst ="/etc/X11/xorg.conf"
                    # shutil.copy(src, dst)
                # case "sysconfig":
                    # # dst ="/etc/fstab"
                    # # shutil.copy(src, dst)
                    # print("Я не сделал")
                # case "sudoers":
                    # dst ="/etc/sudoers"
                    # shutil.copy(src, dst)
                # case "grub":
                    # dst ="/etc/default/grub"
                    # shutil.copy(src, dst)
                # case "xinitrc":
                    # dst =HOME + "/.xinitrc"
                    # shutil.copy(src, dst)
                # case "gitconfig":
                    # dst =HOME + "/gitconfig"
                    # shutil.copy(src, dst)
