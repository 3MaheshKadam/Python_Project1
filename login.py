#login page
import tkinter as tk
from tkinter import ttk, messagebox
from task_completion import TaskComplete  # Import TaskComplete class from task_completion.py
from task_manager import TaskManagerApp  # Importing TaskManagerApp class from task_manager.py
from sign_up import Sign_Up
import os
from PIL import Image, ImageTk
import re

class AdminLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Admin Login')
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.configure(bg="#f0f0f0")  # Background color
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")

        # Placeholder for the stored hashed password
        self.stored_hashed_password = None
        
        self.setup_ui()

    def open_sign_up_page(self):
        self.root.destroy()

        signup_window = Sign_Up()
        signup_window.run()

    def login(self):
        username = self.user.get()
        password = self.password.get()

        # Define regex patterns for password complexity requirements
        password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%*?&]{8,}$')

        # Check if password meets complexity requirements
        if not password_regex.match(password):
            messagebox.showerror("Invalid", "Password must be at least 8 characters long and contain at least one uppercase letter, one numeric value, and one symbol.")
            return

        # Check if the username and password are correct
        if username == "admin" and password == "Admin@1234":
            self.root.destroy()  # Close the login window
            root = tk.Tk()
            app = TaskManagerApp(root)  # Open the Task Manager app
            root.mainloop()
        else:
            # Authentication failed, open TaskComplete window directly
            self.root.destroy()  # Close the login window
            root = tk.Tk()
            app = TaskComplete(root, [])  # Open the Task Complete window
            root.mainloop()

    def setup_ui(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        # img_path = Image.open('D:\\core2web\\Projects\\final\\asset\\images\\login.jpg')
        img_path = os.path.join(script_directory, "asset\images\login.jpg")
        # img_path = os.path.join(script_directory, "D:\\yz\\asset\\images\\login.jpg")
        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        self.label = tk.Label(self.root, image=img, bg='white')
        self.label.image = img 
        self.label.place(x=10, y=50, anchor='nw')

        self.frame = tk.Frame(self.root, width=350, height=400, bg='white', bd=2, relief=tk.SOLID)  # Add border and relief
        self.frame.place(x=900, y=150)

        self.heading = tk.Label(self.frame, text='Login', fg="black", bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        def on_enter(e):
            self.user.delete(0,'end')

        def on_leave(e):
            name = self.user.get()
            if name == '':
                self.user.insert(0,'Username')

        self.user = tk.Entry(self.frame, width=25, fg='black',border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>',on_enter)
        self.user.bind('<FocusOut>',on_leave)

        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            self.password.delete(0,'end')

        def on_leave(e):
            name = self.password.get()
            if name == '':
                self.password.insert(0,'Password')

        self.password = tk.Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        self.password.place(x=30, y=150)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', on_enter)
        self.password.bind('<FocusOut>',on_leave)

        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        self.style = ttk.Style()
        self.style.configure('Rounded.TButton', background='#57a1f8', foreground='white', borderwidth=0, font=('Arial', 10, 'bold'))  # Adjust button style

        self.button_label=ttk.Button(self.frame, text="Login",  width=40, command=self.login, style='Rounded.TButton')  # Apply style
        self.button_label.pack()
        self.button_label.place(x=35, y=210)

        self.label1 = tk.Label(self.frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        self.label1.place(x=70, y=250)

        self.style.configure('Rounded.TButton', background='white', foreground='#57a1f8', border=0, font=('Arial', 10, 'bold'))  # Adjust button style

        self.sign_up = ttk.Button(self.frame, width=8, text='Sign up', cursor='hand2', command=self.open_sign_up_page, style='Rounded.TButton')  # Apply style
        self.sign_up.pack()
        self.sign_up.place(x=215, y=250)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    admin_login = AdminLogin()
    admin_login.run()
