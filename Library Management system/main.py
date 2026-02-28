from tkinter import Frame, Label
import psycopg2
import customtkinter as tk
from PIL import Image
import os
from tkinter import messagebox
from studentDashboard import StudentDashboard
from dotenv import load_dotenv
load_dotenv()
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()
#database
cur.execute('''
        CREATE TABLE IF NOT EXISTS person (
            id SERIAL PRIMARY KEY,
            Username VARCHAR(255),
            password VARCHAR(255)
        );
''')

conn.commit()


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

        self.Loginbutton.bind(
            "<Button-1>",
            lambda e: self.studentDashboard()
        )

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
        self.lgn_frame.place_forget()
        self.show_register_frame()

    def show_register_frame(self):
        self.Rgs_frame = Frame(self.root, width=800, height=980)
        self.Rgs_frame.place(x=730, y=0)

        self.txt = 'Register An Account'
        self.heading = tk.CTkLabel(self.Rgs_frame, text=self.txt, font=('yu gothic ui', 55, 'bold'))
        self.heading.place(x=45, y=30)

        self.UserName = tk.CTkLabel(self.Rgs_frame, text='Username', font=('yu gothic ui', 20,))
        self.UserName.place(x=140, y=200)

        self.UserRegister = tk.CTkEntry(
            master=self.Rgs_frame,
            width=300,
            height=35,
            border_width=0,
            fg_color="transparent",  # removes box background
            text_color="black"
        )
        self.UserRegister.place(x=140, y=230)

        # bottom line
        self.bottom_line = tk.CTkFrame(
            master=self.Rgs_frame,
            width=300,
            height=2,
            fg_color="black"
        )
        self.bottom_line.place(x=140, y=265)

        # Password
        self.PasswordLabel = tk.CTkLabel(self.Rgs_frame, text='Password', font=('yu gothic ui', 20,))
        self.PasswordLabel.place(x=140, y=300)

        self.RegisterPassword = tk.CTkEntry(
            master=self.Rgs_frame,
            width=300,
            height=35,
            show="•",
            border_width=0,
            fg_color="transparent",  # removes box background

        )
        self.RegisterPassword.place(x=140, y=330)

        # bottom line
        self.bottom_line = tk.CTkFrame(
            master=self.Rgs_frame,
            width=300,
            height=2,
            fg_color="black"
        )
        self.bottom_line.place(x=140, y=365)

        self.Registerbutton = tk.CTkButton(self.Rgs_frame, text='Register Account', font=("", 20,), height=40, width=300)
        self.Registerbutton.place(x=140, y=420)

        self.Registerbutton.bind(
            "<Button-1>",
            lambda e: self.register_user()
        )

        self.backToLogin = tk.CTkLabel(
            self.Rgs_frame,
            text="back to Login",
            font=("yu gothic ui", 15, "bold"),
            text_color="#3A7FF6",
            cursor="hand2",

        )
        self.backToLogin.place(x=235, y=500)

        # click event
        self.backToLogin.bind(
            "<Button-1>",
            lambda e: self.BackToLogin()
        )

    def register_user(self):
        username = self.UserRegister.get()
        password = self.RegisterPassword.get()

        cur.execute("SELECT * FROM person WHERE Username = %s", (username,))
        existing_user = cur.fetchone()

        if username == "" or password == "":
            messagebox.showinfo(title="Warning", message="Please don't Leave any fields empty")

        elif existing_user:
            messagebox.showinfo(title="Warning", message="Username already exist")

        else:
            cur.execute("INSERT INTO person (Username, password) VALUES (%s, %s)", (username, password))
            conn.commit()

            self.UserRegister.delete(0,'end')
            self.RegisterPassword.delete(0,'end')

            messagebox.showinfo(title="confirmation", message="information registered, Go back to Login Page")

    def BackToLogin(self):
        self.Rgs_frame.place_forget()
        self.lgn_frame.place(x=730, y=0)
    def studentDashboard(self):
        username = self.UserEntry.get()
        password = self.PasswordEntry.get()

        cur.execute("SELECT * FROM person WHERE Username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        if user:
            self.lgn_frame.place_forget()
            self.label.place_forget()
            StudentDashboard(self.root, username, self.BackToLoginFromDashboard)
        else:
            messagebox.showinfo(title="Warning", message="Invalid username or password!" )

    def BackToLoginFromDashboard(self):
        self.lgn_frame.place(x=730, y=0)
        self.label.place(x=0, y=0)  # bring back the left side image
root = tk.CTk()
obj = LibraryManagement(root)



root.mainloop()

cur.close()
conn.close()


