### Project Summary for GitHub Repository

**Library Management System**

This project is a simple **Library Management System** built using Python. It allows administrators to manage books, track transactions, and check overdue books, while users can borrow, return, and view their transaction history.

#### **Features**
1. **Admin Features**
   - Check book inventory.
   - Add new books to the library.
   - Track overdue books and calculate fines.
   - View transaction history.

2. **User Features**
   - Browse available books.
   - Borrow and return books.
   - View personal transaction history.

3. **Authentication System**
   - Secure login using hashed passwords.
   - Separate access control for Admin and Users.

#### **Technology Stack**
- **Python**
- **CSV files** for data storage (books, transactions, users)
- **Hashlib** for password encryption

#### **File Structure**
- `Admin.py` - Admin functionalities (book management, fines, transactions)
- `user.py` - User functionalities (borrow, return, transaction history)
- `login.py` - Authentication system (signup, login, password hashing)
- `library.csv` - Book database
- `transactions.csv` - Records of borrowing/returning books
- `Admin.txt` & `users.txt` - Stores login credentials

#### **How to Run**
1. Run `login.py` to access the main menu.
2. Create a new user or log in as admin.
3. Admins can manage books; users can borrow/return books.

This project is useful for small libraries or personal book collections. Future improvements could include a database backend, GUI, or web integration.
