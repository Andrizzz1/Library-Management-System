from tkinter import Frame
import customtkinter as tk
from tkinter import Frame
class StudentDashboard():
    def __init__(self, root):
        self.root = root
        self.root.geometry('1166x718')


        self.heading = tk.CTkLabel(self.root,text='STUDENT DASHBOARD', font=('yu gothic ui', 55,'bold'))
        self.heading.place(x=450, y=30)

        self.menus = tk.CTkLabel(
            self.root,
            text="",
            bg_color='Green',
            width= int(1166/4),
            height=718

        )

        self.menus.place(x=0,y=0)