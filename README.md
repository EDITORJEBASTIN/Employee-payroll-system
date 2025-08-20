---

Employee Payroll System

A Python + SQL-based project to manage employees, salary details, and tax calculations. This system provides an easy way to handle employee records, attendance tracking, and salary generation with tax deductions.


---

📌 Features

Add new employees with role and base salary

Record employee attendance (days worked)

Calculate gross salary, tax, and net salary

Store and retrieve employee details using SQL database

View all employees and their payroll data



---

🛠 Tech Stack

Programming Language: Python

Database: SQLite (can be extended to MySQL/PostgreSQL)

Libraries Used:

sqlite3 (for database connection)




---

📂 Database Schema

Employees Table

emp_id (Primary Key)

name

role

base_salary


Attendance Table

id (Primary Key)

emp_id (Foreign Key)

days_worked



---

⚙️ Installation & Setup

1. Clone the repository:

git clone https://github.com/your-username/employee-payroll-system.git
cd employee-payroll-system


2. Run the Python script:

python payroll.py




---

▶️ Example Usage

✅ Employee Alice added successfully.  
✅ Attendance recorded for Employee ID 1.  
💰 Salary for Employee 1: Gross=44000.00, Tax=4400.00, Net=39600.00


---

🚀 Future Enhancements

Add a GUI (Tkinter / Flask Web App)

Export payroll reports to PDF/Excel

Add authentication for secure access

Support multiple tax slabs



---

📜 License

This project is open-source and available under the MIT License.


---
