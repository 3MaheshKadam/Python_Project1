#sign_up page
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
import bcrypt
import re

class Sign_Up:
    def __init__(self):
        self.window = Tk()
        self.window.title("SignUp")
        self.window.geometry('1480x1480')
        self.window.configure(bg='#fff')
        self.window.resizable(False, False)

        self.stored_hashed_pass = None

        self.signup_page()
    
    def sign_in(self):
        username = self.user.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()

        password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%*?&]{8,}$')

        if not password_regex.match(password) or password != confirm_password:
            messagebox.showerror("Invalid","Password must be at least 8 characters long and contain at least one uppercase letter, one numeric value, and one symbol.")
            return
            
        if self.stored_hashed_pass is None:
            self.stored_hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        entered_password = password.encode('utf-8')

        if username and bcrypt.checkpw(entered_password, self.stored_hashed_pass):
            # Authentication successful, proceed with login
            self.screen = tk.Toplevel(self.window)
            self.screen.title('App')
            self.screen.geometry('500x300')
            self.screen.config(bg='white')
        else:
            # Authentication failed, show error message
            messagebox.showerror("Invalid", "Invalid username or password")


    def signup_page(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_directory, "D:\\yz\\asset\\images\\login.jpg")
        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        self.label = tk.Label(self.window, image=img, bg='white')
        self.label.image = img 
        self.label.place(x=50, y=80, anchor='nw')
        

        self.frame = Frame(self.window, width=350, height=390, bg='#fff')
        self.frame.place(x=420, y=80)
        self.frame.place(relx=0.3,rely=0)

        self.heading = tk.Label(self.frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        def on_enter(e):
            self.user.delete(0,'end')
        def on_leave(e):
            if self.user.get()=='':
                self.user.insert(0,'Username')

        self.user = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind("<FocusIn>", on_enter)
        self.user.bind("<FocusOut>",on_leave)

        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            self.password.delete(0,'end')
        def on_leave(e):
            if self.password.get()=='':
                self.password.insert(0,'Password')

        self.password = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.password.place(x=30, y=150)
        self.password.insert(0, 'Password')
        self.password.bind("<FocusIn>", on_enter)
        self.password.bind("<FocusOut>",on_leave)

        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        def on_enter(e):
            self.confirm_password.delete(0,'end')
        def on_leave(e):
            if self.confirm_password.get()=='':
                self.confirm_password.insert(0,'Confirm Password')

        self.confirm_password = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.confirm_password.place(x=30, y=220)
        self.confirm_password.insert(0, 'Confirm Password')
        self.confirm_password.bind("<FocusIn>", on_enter)
        self.confirm_password.bind("<FocusOut>",on_leave)

        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=247)

        self.style = ttk.Style()
        self.style.configure('Square.TButton', bg='#57a1f8', fg='white', borderwidth=0)

        self.button_label=ttk.Button(self.frame, text="Sign Up",  width=45, command=self.sign_in)
        self.button_label.pack()
        self.button_label.place(x=35, y=280)

        self.label = tk.Label(self.frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        self.label.place(x=90, y=340)
        
        self.style.configure('Square.TButton', bg='white', fg='#57a1f8', borderwidth=0)

        self.sign_up = ttk.Button(self.frame, width=8, text='Sign in',cursor='hand2', style='Square.TButton')
        self.sign_up.pack()
        self.sign_up.place(x=200, y=340)



    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    signup = Sign_Up()
    signup.run()
