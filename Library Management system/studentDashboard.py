from tkinter import Frame
import customtkinter as tk
from tkinter import Frame
class StudentDashboard():
    def __init__(self, root, username ,logout_callback):
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

        self.User = tk.CTkLabel(self.menus, text=username,font=('yu gothic ui', 20, 'bold'), bg_color='Green',text_color='White')
        self.User.place(x=50, y=40)

        self.Dashboard = tk.CTkLabel(self.menus,
                                text='Dashboard',
                                font=('yu gothic ui', 20, 'bold'),
                                bg_color='Green',

                                text_color="#D3D3D3")

        self.Dashboard.place(x=50, y=180)
        self.Dashboard.bind("<Enter>", lambda e: self.Dashboard.configure(text_color="white"))
        self.Dashboard.bind("<Leave>", lambda e: self.Dashboard.configure(text_color="#D3D3D3"))
        self.Books = tk.CTkLabel(self.menus,
                                text='Books',
                                font=('yu gothic ui', 20, 'bold'),
                                bg_color='Green',

                                text_color="#D3D3D3")
        self.Books.place(x=50, y=260)
        self.Books.bind("<Enter>", lambda e: self.Books.configure(text_color="white"))
        self.Books.bind("<Leave>", lambda e: self.Books.configure(text_color="#D3D3D3"))
        self.Returned = tk.CTkLabel(self.menus,
                                 text="Returned",
                                 font=('yu gothic ui', 20, 'bold'),
                                 bg_color='Green',

                                 text_color="#D3D3D3")
        self.Returned.place(x=50, y=340)
        self.Returned.bind("<Enter>", lambda e: self.Returned.configure(text_color="white"))
        self.Returned.bind("<Leave>", lambda e: self.Returned.configure(text_color="#D3D3D3"))
        self.NOTReturned = tk.CTkLabel(self.menus,
                                    text="Unreturned Books",
                                    font=('yu gothic ui', 20, 'bold'),
                                    bg_color='Green',

                                    text_color="#D3D3D3")
        self.NOTReturned.place(x=50, y=420)
        self.NOTReturned.bind("<Enter>", lambda e: self.NOTReturned.configure(text_color="white"))
        self.NOTReturned.bind("<Leave>", lambda e: self.NOTReturned.configure(text_color="#D3D3D3"))
        self.logout = tk.CTkLabel(self.menus,
                                       text="LOGOUT",
                                       font=('yu gothic ui', 20, 'bold'),
                                       bg_color='Green',

                                       text_color="#D3D3D3")
        self.logout.place(x=50, y=600)
        self.logout.bind("<Enter>", lambda e: self.logout.configure(text_color="white"))
        self.logout.bind("<Leave>", lambda e: self.logout.configure(text_color="#D3D3D3"))
        self.logout_callback = logout_callback

        self.logout.bind("<Button-1>", lambda e: self.do_logout())

    def do_logout(self):
        self.menus.place_forget()
        self.heading.place_forget()
        self.logout_callback()