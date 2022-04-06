import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from PIL import ImageTk, Image


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()

        ## Initial params
        self.title("configs_demo")
        self.geometry("390x360")
        self.resizable(False, False)
        self.iconphoto(False, tk.PhotoImage(file="../res/img/auto_replace.png"))


        ##Containers setting
        container = tk.Frame(self, bg="#E0E0E0")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        ##Frames init and work
        self.frames = {}
        self.HomePage = HomePage
        self.ManualPage = ManualPage

        for F in {HomePage, ManualPage}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0,column=0, sticky="nsew")
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        ##Auto add configs button settings
        auto_add_img = PhotoImage(file = "../res/img/auto_replace.png")
        auto_add_configs_button = Button(self, image=auto_add_img, borderwidth=0)
        auto_add_configs_button.image = auto_add_img
        auto_add_configs_button.pack()
        auto_add_configs_button.place(x=48, y=56)

        ##Manual add configs button settings
        manual_add_img = PhotoImage(file = "../res/img/manual_replace.png")
        manual_add_configs_button = Button(self, image=manual_add_img, borderwidth=0,
                                           command = lambda : container.show_frame(ManualPage))
        manual_add_configs_button.image = manual_add_img
        manual_add_configs_button.pack()
        manual_add_configs_button.place(x=219, y=56)

        ##Help button 
        help_image = PhotoImage(file = "../res/img/help_1.png")
        help_button = Button(self, image=help_image, borderwidth=0)
        help_button.image = help_image
        help_button.pack()
        help_button.place(x=77, y=246)

        ##Dump configs button
        backup_image = PhotoImage(file = "../res/img/backup_1.png")
        backup_button = Button(self, image=backup_image, borderwidth=0)
        backup_button.image = backup_image
        backup_button.pack()
        backup_button.place(x=248, y=246)


class ManualPage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)
        label = tk.Label(self, text="manual Page", font=('Times', '20'))
        label.pack(pady=0,padx=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()
