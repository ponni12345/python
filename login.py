
#saample user data
user={
    "user1":"password1",
    "user2":"password2",
    }
def login():
    username=input("enter your usernae:")
    password=input("enter your password:")

    if username in users and users[username]==password:
        print("login successful!")
    else:
        print("login failed.please check your username and password")

def register():
    username=input("choose a user:")
    password=input("choose a password:")
    if username in users:
        print("username already exists please choose different username")
    else:   
        user[username]=password
        print("registration successful!")

def main():
    while true:
        choice=input("do you want to(login/register)")
        lower()
        if choice=="login":
            login()
        elif choice=="register":
            register()
        elif choice=="exit":
            print("exiting the system.")
            break
        else:
            print("invalid choice pleasechoose'login','register',or,'exit'.")
        if__name__=="__main__";
        mani()
        
    #sample user data
    user={
        "user1":"password1",
        "user2":"password2",
        }

    

        
