import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
from dao.TaxService import TaxService
import pyodbc
from exception.Customexceptions import TaxCalculationException,EmployeeNotFoundException
from exception.Customexceptions import DatabaseConnectionException
from util.DBConn import DBConn
from decimal import Decimal
class ITaxService(TaxService):
    def __init__(self):
        self.conn = DBConn.get_db_conn()
        self.taxes = {}

    def CalculateTax(self, employee_id, Taxyear):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Tax WHERE employee_id = ? and Taxyear=?", (employee_id,Taxyear))
        cursor.fetchone()
        query = "SELECT SUM(p.NetSalary) AS TaxableIncome FROM Payroll p WHERE p.employee_id= ? AND YEAR(p.PayPeriodEndDate) = ?"
        cursor.execute(query, (employee_id,Taxyear))
        row = cursor.fetchone()

        if not row or row[0] is None:
            raise TaxCalculationException(f"No payroll records found for employee {employee_id} in the year {Taxyear}.")

        TaxableIncome = row[2]
        tax_rate = Decimal('0.2')  
        tax_amount = TaxableIncome * tax_rate  

        query = "INSERT INTO Tax (employee_id, TaxYear, TaxableIncome, TaxAmount) VALUES (?, ?, ?, ?)"
        values = (employee_id, Taxyear, TaxableIncome, tax_amount)
        cursor.execute(query, values)
        self.conn.commit()
        print("Tax calculated successfully")
        cursor.close()
    
    def GetTaxById(self, tax_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE Tax_id = ?", tax_id)
            row = cursor.fetchone()
            if row:
                print(f"Tax id :{row[0]},Employee id:{row[1]},Tax year:{row[2]},Taxable Income:{row[3]},Tax Amount:{row[4]}")
                
            else:
                raise EmployeeNotFoundException(f"Tax with ID {tax_id} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

   
    def GetTaxesForEmployee(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE employee_id = ?", employee_id)
            row = cursor.fetchone()
            if row:
                print(f"Tax id :{row[0]},Employee id:{row[1]},Tax year:{row[2]},Taxable Income:{row[3]},Tax Amount:{row[4]}")
               
            else:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def GetTaxesForYear(self, Taxyear):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE Taxyear = ?", Taxyear)
            row = cursor.fetchone()
            if row:
                print(f"Tax_id :{row[0]},employee_id:{row[1]},Tax_year:{row[2]},TaxableIncome:{row[3]},TaxAmount:{row[4]}")
                
            else:
                raise EmployeeNotFoundException(f"Tax with year {Taxyear} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    #For Unit testing
    def VerifyTaxCalculationForHighIncomeEmployee(self, TaxableIncome):

        if TaxableIncome <= 0:
            raise ValueError("Taxable income must be positive.")

        tax_amount = 0.1 * TaxableIncome
        return tax_amount

