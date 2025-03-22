import os
import hashlib
import Admin
import user

ADMIN_DATA_FILE = "Admin.txt"
USER_DATA_FILE = 'users.txt'
def hash(password):
    return (hashlib.sha256(password.encode()).hexdigest())

def signup():
    username = input("Enter Username:")
    password = input("Enter Password:")

    if user_exists(username):
        print("user already exists!!  please try again\n")
        return
    us=0
    ls=0
    Sy=0
    di=0
    for i in password:
        if i.isdigit():
            di=1
        if i.isupper():
            us=1
        if i.islower():
            ls=1
        if not i.isalnum():
            Sy=1
    if len(password)>5 and len(password)>13:
        print("Invalid password. Length should from 6 to 12\n")
        signup()
    if ls and di and Sy and us:
        with open(USER_DATA_FILE,"a") as f:
            f.write(f"{username},{hash(password)}\n")
        print("SignUp successful\n")
    else:
        print("Invalid password. Criteria not matched\n")
        signup()
    

def login():
    username = input("Enter Username:")
    password = input("Enter Password:")

    if verify_user(username,hash(password))==(True,True):
        print("Login successfully for Admin!\n")
        Admin.admin_menu()
    elif verify_user(username,hash(password))==(True,False):
        print(f"Login successfully for user:{username}!\n")
        user.user_menu(username)
    else:
        print("Invalid username and password. Try again!!\n")
        login()

def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(ADMIN_DATA_FILE,'r') as f:
        for line in f:
            stored_username,_ = line.strip().split(',')
            if stored_username==username:
                return True
    with open(USER_DATA_FILE,'r') as f:
        for line in f:
            stored_username,_ = line.strip().split(',')
            if stored_username==username:
                return True
    return False

def verify_user(username, password):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(ADMIN_DATA_FILE,"r") as f:
        for line in f:
            stored_username, stored_password = line.strip().split(',')
            if stored_username==username and stored_password==password:
                return True,True
    with open(USER_DATA_FILE,"r") as f:
        for line in f:
            stored_username, stored_password = line.strip().split(',')
            if stored_username==username and stored_password==password:
                return True,False
        return False

def main():
    while True:
        print("""-----MAIN MENU----
1. Signup
2. Login
3. Exit
""")
        try:
            choice = int(input("Enter the choice from menu:").strip())
            if choice ==1:
                signup()
            elif choice==2:
                login()
            elif choice==3:
                print("---Thank You---\n")
                break
            else:
                raise IndentationError
        except Exception as e:
            print(e.__doc__,e)
            print("Invalid Input!! please Try again\n")
if __name__ == "__main__":
    main()