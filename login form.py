import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
# You can add your own validation logic here
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Successful", "Welcome Admin!")
    
# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Create and place the username label and entry
username_label = tk.Label(parent, text="Username:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()
# Show asterisks for password
password_entry = tk.Entry(parent, show="*")  
password_entry.pack()

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
parent.mainloop()
