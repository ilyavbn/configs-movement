import os
import tkinter as tk
import tkinter.filedialog as fd
import configparser

configpath = '../config.ini'
config = configparser.ConfigParser()
config.read(configpath)

filenames = []
final =[]



root = tk.Tk()
filez = fd.askopenfilenames(parent=root, title='Choose a file')
##print(filez)

# for name in filez:
    # filenames.append(os.path.basename(name))
for name in filez:
    os.path.basename(name)
    for key, value in config['CONFIGS_PATH'].items():
        if name == key:
            print(key, name)
