
# Online Python - IDE, Editor, Compiler, Interpreter
import sqlite3

# -------------------------------
# Database Connection & Setup
# -------------------------------
conn = sqlite3.connect("payroll.db")
cursor = conn.cursor()

# Employee Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT,
    base_salary REAL
)
""")

# Attendance Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_id INTEGER,
    days_worked INTEGER,
    FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)
""")

conn.commit()

# -------------------------------
# Functions
# -------------------------------

def add_employee(name, role, base_salary):
    cursor.execute("INSERT INTO employees (name, role, base_salary) VALUES (?, ?, ?)",
                   (name, role, base_salary))
    conn.commit()
    print(f"✅ Employee {name} added successfully.")

def record_attendance(emp_id, days_worked):
    cursor.execute("INSERT INTO attendance (emp_id, days_worked) VALUES (?, ?)",
                   (emp_id, days_worked))
    conn.commit()
    print(f"✅ Attendance recorded for Employee ID {emp_id}.")

def calculate_salary(emp_id):
    cursor.execute("SELECT base_salary FROM employees WHERE emp_id=?", (emp_id,))
    emp = cursor.fetchone()
    
    cursor.execute("SELECT SUM(days_worked) FROM attendance WHERE emp_id=?", (emp_id,))
    days = cursor.fetchone()[0]

    if emp and days:
        daily_salary = emp[0] / 30  # assume 30 days in month
        gross_salary = daily_salary * days
        tax = gross_salary * 0.1  # 10% tax
        net_salary = gross_salary - tax
        print(f"💰 Salary for Employee {emp_id}: Gross={gross_salary:.2f}, Tax={tax:.2f}, Net={net_salary:.2f}")
    else:
        print("⚠ Employee or attendance not found.")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    add_employee("Alice", "Developer", 60000)
    add_employee("Bob", "Manager", 90000)

    record_attendance(1, 22)
    record_attendance(2, 26)

    view_employees()

    calculate_salary(1)
    calculate_salary(2)

    conn.close()