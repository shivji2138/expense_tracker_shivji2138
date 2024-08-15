import mysql.connector
from datetime import datetime

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',       
    password='shivusql',
    database='expense_tracker'
)
cursor = conn.cursor()

# Function to add a new expense
def add_expense():
    try:
        amount = float(input("Enter the amount spent: "))
        category = input("Enter the category: ")
        description = input("Enter a description: ")
        cursor.execute("SELECT id FROM categories WHERE name = %s", (category,))
        category_id = cursor.fetchone()
        if category_id:
            category_id = category_id[0]
        else:
            # If the category does not exist, create a new category
            cursor.execute("INSERT INTO categories (name) VALUES (%s)", (category,))
            category_id = cursor.lastrowid

        # Insert the expense into the expenses table
        cursor.execute("""
            INSERT INTO expenses (amount, category_id, description, date)
            VALUES (%s, %s, %s, %s)
        """, (amount, category_id, description, datetime.now().strftime('%Y-%m-%d')))

        conn.commit()
        print("Expense added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to get expenses by category
def get_expenses_by_category():
    try:
        cursor.execute("""
            SELECT categories.name, SUM(expenses.amount) as total_amount
            FROM expenses
            JOIN categories ON expenses.category_id = categories.id
            GROUP BY categories.name
        """)
        
        rows = cursor.fetchall()
        print("\nExpenses by Category:")
        for row in rows:
            print(f"Category: {row[0]}, Total Spent:₹{row[1]:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main loop to add expenses and view reports
while True:
    print("\nOptions:")
    print("1. Add a new expense")
    print("2. View expenses by category")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        get_expenses_by_category()
    elif choice == '3':
        break
    else:
        print("Invalid choice, please try again.")

# Close the database connection when done
cursor.close()
conn.close()

