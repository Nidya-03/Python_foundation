import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
from dao.TaxService import TaxService
import pyodbc
from exception.Customexceptions import TaxCalculationException,EmployeeNotFoundException
from exception.Customexceptions import DatabaseConnectionException
from util.DBConn import DBConn

class ITaxService(TaxService):
    def __init__(self):
        self.conn = DBConn.get_db_conn()
        self.taxes = {}

    def CalculateTax(self, employee_id, Taxyear):
        try:
            
            taxable_income = 60000  
            tax_amount = taxable_income * 0.2 

            cursor = self.conn.cursor()
            cursor.execute("""
                insert into tax (employee_id, Taxyear, TaxableIncome, TaxAmount)
                values (?, ?, ?, ?)
            """, (employee_id, Taxyear, taxable_income, tax_amount))
            self.conn.commit()
            print("Tax calculated successfully")
        except Exception as e:
            print(f"Error while calculating tax: {e}")
            raise TaxCalculationException("Error in tax calculation")
    
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
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"tax_id :{row[0]},employee_id:{row[1]},Taxyear:{row[2]},TaxableIncome:{row[3]},TaxAmount:{row[4]}")
               
            else:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def GetTaxesForYear(self, Taxyear):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Tax WHERE Taxyear = ?", Taxyear)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"tax_id :{row[0]},employee_id:{row[1]},Taxyear:{row[2]},TaxableIncome:{row[3]},TaxAmount:{row[4]}")
                
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

