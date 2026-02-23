import customtkinter as tk
from customtkinter import *

class LibraryManagement():
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management")
        self.root.geometry('1166x718')
        self.root.resizable(0,0)

root = tk.CTk()
obj = LibraryManagement(root)


root.mainloop()
