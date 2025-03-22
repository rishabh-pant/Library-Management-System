import csv
import Admin

def return_book(title,user):
    books = []
    returned = False
    with open(Admin.library_file,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            if title == row[0] and row[2]=="No":
                row[2]="Yes"
                returned = True
            books.append(row)
    if returned:
        with open(Admin.library_file,"w",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(books)
        print(f"User:{user}has returned {title} book")
        Admin.record_trans(title,"Returned",user)
    else:
        print(f"The book {title} was not borrowed or is already returned")

def check_my_trans(user):
    with open(Admin.trans_file,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == user:
                print(f"Date:{row[0]},Title:{row[1]},Operation:{row[2]},By:{row[3]}")
    
def user_menu(user):
    while True:
        print("""---User Menu---
1. Check Inventory
2. Borrow a book
3. Return a book
4. Check My Transactions
5. Exit
""")
        try:
            choice = int(input("Enter the choice from menu:").strip())
            if choice ==1:
                Admin.check_inventory()
            elif choice==2:
                title = input("Enter the title of book:")
                Admin.borrow_book(title,user)
            elif choice==3:
                title = input("Enter the title of book:")
                return_book(title,user)
            elif choice==4:
                check_my_trans(user)
            elif choice==5:
                print("---Thank you---")
                break
            else:
                raise IndentationError
        except Exception as e:
            print(e)
            print("Invalid Input!! please Try again\n")
            user_menu()