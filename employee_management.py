### Firstly, set up your MySQL database and table in MySQL WORKBENCH:

# create database employee_management;

# use employee_management;

# create table employees (
# id int auto_increment primary key, 
# first_name varchar(100), 
# last_name varchar(100),
# job_role varchar(100),
# salary decimal(10,2),
# performance_review text
# );
import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Surya@1330",
            database="employee_management"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def add_employee(first_name, last_name, job_role, salary, performance_review):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO employees (first_name, last_name, job_role, salary, performance_review) VALUES (%s, %s, %s, %s, %s)",
                (first_name, last_name, job_role, salary, performance_review)
            )
            conn.commit()
            employee_id = cursor.lastrowid
            print(f"Employee added successfully with ID: {employee_id}")
            return employee_id
        except Error as e:
            print(f"Failed to add employee: {e}")
        finally:
            cursor.close()
            conn.close()
    return None

def update_employee(employee_id, first_name, last_name, job_role, salary, performance_review):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE employees SET first_name=%s, last_name=%s, job_role=%s, salary=%s, performance_review=%s WHERE id=%s",
                (first_name, last_name, job_role, salary, performance_review, employee_id)
            )
            conn.commit()
            if cursor.rowcount > 0:
                print("Employee updated successfully.")
            else:
                print("Employee not found.")
        except Error as e:
            print(f"Failed to update employee: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_employee(employee_id):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM employees WHERE id=%s", (employee_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")
        except Error as e:
            print(f"Failed to delete employee: {e}")
        finally:
            cursor.close()
            conn.close()

def view_employee(employee_id):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM employees WHERE id=%s", (employee_id,))
            employee = cursor.fetchone()
            if employee:
                print("Employee Details:", employee)
            else:
                print("Employee not found.")
        except Error as e:
            print(f"Failed to retrieve employee: {e}")
        finally:
            cursor.close()
            conn.close()
        return employee

def generate_performance_report():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT first_name, last_name, job_role, performance_review FROM employees")
            report = cursor.fetchall()
            print("Performance Report:")
            for record in report:
                print(record)
        except Error as e:
            print(f"Failed to generate performance report: {e}")
        finally:
            cursor.close()
            conn.close()

def generate_salary_distribution_report():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT job_role, AVG(salary) FROM employees GROUP BY job_role")
            report = cursor.fetchall()
            print("Salary Distribution Report:")
            for record in report:
                print(record)
        except Error as e:
            print(f"Failed to generate salary distribution report: {e}")
        finally:
            cursor.close()
            conn.close()

# Example usage
if __name__ == "__main__":
    # Add new employee
    employee_id = add_employee("John", "Doe", "Software Engineer", 75000, "Excellent")

    if employee_id:
        # Update employee details
        update_employee(employee_id, "John", "Doe", "Senior Software Engineer", 85000, "Outstanding")

        # View employee details
        view_employee(employee_id)

        # Generate performance report
        generate_performance_report()

        # Generate salary distribution report
        generate_salary_distribution_report()

        # Delete employee
        #delete_employee(employee_id)
