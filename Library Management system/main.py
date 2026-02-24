from tkinter import Frame, Label

import customtkinter as tk
from PIL import Image
import os

LibraryIMG = os.path.join("images","LibraryIMG.jpg")
class LibraryManagement():
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management")
        self.root.geometry('1166x718')
        self.root.resizable(0,0)
        self.img = tk.CTkImage(
            light_image=Image.open(LibraryIMG),
            dark_image=Image.open(LibraryIMG),
            size=(583, 718)
        )

        self.label = tk.CTkLabel(
            self.root,
            image=self.img,
            text=""
        )
        self.label.place(x=0, y=0)

        #Login Frame#
        self.lgn_frame = Frame(self.root,width=800, height=980)
        self.lgn_frame.place(x=730, y=0)

        self.txt = 'WELCOME'
        self.heading = tk.CTkLabel(self.lgn_frame,text=self.txt, font=('yu gothic ui', 55,'bold'))
        self.heading.place(x=155,y=30)

        self.UserName = tk.CTkLabel(self.lgn_frame, text='Username', font=('yu gothic ui', 20, ))
        self.UserName.place(x=140, y=200)

        self.UserEntry = tk.CTkEntry(
            master=self.lgn_frame,
            width=300,
            height=35,
            border_width=0,
            fg_color="transparent",  # removes box background
            text_color="black"
        )
        self.UserEntry.place(x=140, y=230)

        # bottom line
        self.bottom_line = tk.CTkFrame(
            master=self.lgn_frame,
            width=300,
            height=2,
            fg_color="black"
        )
        self.bottom_line.place(x=140, y=265)

        #Password
        self.PasswordLabel = tk.CTkLabel(self.lgn_frame, text='Password', font=('yu gothic ui', 20,))
        self.PasswordLabel.place(x=140, y=300)

        self.PasswordEntry = tk.CTkEntry(
            master=self.lgn_frame,
            width=300,
            height=35,
            show="•",
            border_width=0,
            fg_color="transparent",  # removes box background

        )
        self.PasswordEntry.place(x=140, y=330)

        # bottom line
        self.bottom_line = tk.CTkFrame(
            master=self.lgn_frame,
            width=300,
            height=2,
            fg_color="black"
        )
        self.bottom_line.place(x=140, y=365)

        self.Loginbutton = tk.CTkButton(self.lgn_frame, text='LOGIN', font=("", 20,), height=40, width=300)
        self.Loginbutton.place(x=140, y=420)

        self.CreateACClabel = tk.CTkLabel(self.lgn_frame, text="Don't have an account?", font=('yu gothic ui', 16,))
        self.CreateACClabel.place(x=213, y=480)

        self.create_account = tk.CTkLabel(
            self.lgn_frame,
            text="CREATE AN ACCOUNT",
            font=("yu gothic ui", 10, "bold"),
            text_color="#3A7FF6",
            cursor="hand2"
        )
        self.create_account.place(x=250, y=515)

        # click event
        self.create_account.bind(
            "<Button-1>",
            lambda e: self.open_register()
        )

    def open_register(self):
        print("CREATE ACC")
root = tk.CTk()
obj = LibraryManagement(root)


root.mainloop()
