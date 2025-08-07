# Digital Food Ordering System

This is a simple console-based food ordering system developed using Python and MySQL. It allows users to browse a menu, place orders, and receive confirmation via the terminal. The project is intended for learning and practice.

---

## Features

- Menu browsing with item codes and prices
- Order placement with quantity selection
- Displays order summary and total cost
- Admin-side menu management (if implemented)
- MySQL database integration for persistent data

---

## Technologies Used

- Python
- MySQL
- MySQL Connector (`mysql-connector-python`)

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/kumaraguru1204/Digital-Food-Ordering-System.git
cd Digital-Food-Ordering-System
```

### 2. Set up the MySQL database
-> Create a new database in MySQL.
-> Create tables for menu items and orders.
-> You can write your own schema or refer to a setup.sql file (if added later).

### 3. Configure the database connection
-> Create a file named config.py in the root directory.
-> Add the following content:
```python
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "your_database_name"
```

### 4. Run the application
```python
python main.py
```

Note
  This is a basic terminal-based project meant for educational purposes.
  config.py is not included in the repository.
