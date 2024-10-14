
import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
import pyodbc
from dao.EmployeeService import EmployeeService
from entity.Employee import Employee
from exception.Customexceptions import EmployeeNotFoundException,InvalidInputException
from exception.Customexceptions import DatabaseConnectionException
from util.DBConn import DBConn

class IEmployeeService(EmployeeService):
    def __init__(self):
        self.conn = DBConn.get_db_conn()

    def get_employee_by_id(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Employee WHERE employee_id = ?", employee_id)
            row = cursor.fetchone()
            if row:
                print(f"Employee id :{row[0]},first_name:{row[1]},last_name:{row[2]},dob:{row[3]},gender:{row[4]},email:{row[5]},phone:{row[6]},address:{row[7]},position:{row[8]},joining_date:{row[9]},termination_date:{row[10]}")
            else:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def get_all_employees(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Employee")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"Employee id :{row[0]},first_name:{row[1]},last_name:{row[2]},dob:{row[3]},gender:{row[4]},email:{row[5]},phone:{row[6]},address:{row[7]},position:{row[8]},joining_date:{row[9]},termination_date:{row[10]}")
            else:
                print("No Employees Found")
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def add_employee(self,employee:Employee):
        try:
            
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (employee.Firstname,employee.Lastname,employee.DateofBirth,employee.Gender,employee.Email,employee.Phonenumber,employee.Address,employee.Position,employee.Joiningdate,employee.Terminationdate))
            self.conn.commit()
            print("Employee added successfully!")
        except pyodbc.IntegrityError as e:
            raise InvalidInputException(f"Integrity error: {e}")
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def update_employee(self, employee: Employee):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE Employee
                SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ?
                WHERE employee_id = ?
            """, (employee.Firstname,employee.Lastname,employee.DateofBirth,employee.Gender,employee.Email,employee.Phonenumber,employee.Address,employee.Position,employee.Joiningdate,employee.Terminationdate,employee.employee_id))
            self.conn.commit()
            print("Employee updated successfully!")
            if cursor.rowcount == 0:
                raise EmployeeNotFoundException(f"Employee with ID {employee.employee_id} not found.")
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def remove_employee(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Employee WHERE employee_id = ?", employee_id)
            self.conn.commit()
            print(f"Employee with ID {employee_id} is removed successfully.")
            if cursor.rowcount == 0:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")
            self.conn.commit()
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")
