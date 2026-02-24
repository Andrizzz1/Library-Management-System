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
        self.lgn_frame = Frame(self.root,width=800, height=800)
        self.lgn_frame.place(x=730, y=10)

        self.txt = 'WELCOME'
        self.heading = tk.CTkLabel(self.lgn_frame,text=self.txt, font=('yu gothic ui', 55,'bold'))
        self.heading.place(x=155,y=30)
root = tk.CTk()
obj = LibraryManagement(root)


root.mainloop()
