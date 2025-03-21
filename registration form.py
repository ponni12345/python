def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Add password confirmation for better security
    confirm_password = input("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    return username, password  # Return the data for storag

def store_user_data(username, password):
    with open("users.txt", "a") as file:  # Open in append mode
        file.write(f"{username}:{password}\n")  # Store username and password
    print("Registration successful!")
def main():
    username, password = register_user()
    store_user_data(username, password)

if __name__ == "__main__":
    main()

import hashlib
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Add password confirmation for better security
    confirm_password = input("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    return username, hashed_password, salt

def store_user_data(username, hashed_password, salt):
    with open("users.txt", "a") as file:  # Open in append mode
        file.write(f"{username}:{hashed_password}:{salt}\n")  # Store username and hashed password
    print("Registration successful!")
