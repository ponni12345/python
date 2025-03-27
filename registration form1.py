name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
filename = "registration_data.txt"
with open(filename, 'w') as file:
        file.write("Name: " + name + "\n")
        file.write("Email: " + email + "\n")
        file.write("Password: " + password + "\n")

import sqlite3

conn = sqlite3.connect('registration.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT
        )
    ''')

cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
conn.commit()
conn.close()
