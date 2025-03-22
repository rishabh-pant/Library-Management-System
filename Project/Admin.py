"""
username : ADMIN
password : Admin@2000
"""
import csv
import datetime

library_file = "library.csv"
trans_file = "transactions.csv"

fine_per_day = 2.0

def check_inventory():
    print("\n---Inventory---\n")
    s_no = 1
    with open(library_file,'r') as file:
        file.readline()
        reader = csv.reader(file)
        for row in reader:
            print(f"{s_no}. Title:{row[0]}  Author:{row[1]}    Availability:{row[2]}")
            s_no+=1
        print()

def add_book(title, author):
    with open(library_file,"a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title,author,"Yes"])
    print("\nBook have been added\n")

def check_faulty_books():
    print("\nOverdue Books with fine:\n")
    with open(trans_file,"r") as f: 
        reader = csv.reader(f)
        for row in reader:
            operation = row[2]
            if operation=="Borrowed":
                borrow_date = datetime.datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S.%f")
                title = row[1]
                user = row[3]
                due_date = borrow_date+datetime.timedelta(days=7)

            if due_date<datetime.datetime.now():
                    overdue_days = (datetime.datetime.now()-due_date).days
                    fine = overdue_days*fine_per_day
                    print(f"Title:{title},User:{user},Fine:{fine}")

def record_trans(title, operation, user): 
    with open(trans_file,"a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([str(datetime.datetime.now()),title,operation,user])
    print("\nTransaction Successful!\n")

def check_trans(): 
    print("\nTransactions histroy:")
    with open(trans_file,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Date:{row[0]},Title:{row[1]},Operation:{row[2]},By:{row[3]}")
        print()

def borrow_book(title,user): 
    books =[]
    borrowed = False
    with open(library_file,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]==title and row[2]=="Yes":
                row[2]="No"
                borrowed = True
            books.append(row)
    if borrowed:
        with open(library_file,"w",newline='') as file:
            writer = csv.writer(file)
            writer.writerows(books)
        print(f"User:{user} has borrowed {title}")
        record_trans(title,"Borrowed",user)
    else:
        print(f"The book {title} is either not available or already borrowed")

def admin_menu():
    while True:
        print("""\n---Admin Menu----
1. Check Inventory
2. Add a New Book
3. Check Overdue Books
4. Check Transactions
5. Exit""")
        try:
            choice = int(input("Enter the choice from menu:").strip())
            if choice ==1:
                check_inventory()
            elif choice==2:
                title = input("Enter the title of book:")
                Author = input("Enter the Author of book:")
                add_book(title,Author)
            elif choice==3:
                check_faulty_books()
            elif choice==4:
                check_trans()
            elif choice==5:
                print("---Thank you---")
                break
            else:
                raise IndentationError
        except Exception as e:
            print(e)
            print("Invalid Input!! please Try again\n")
            admin_menu()
        


