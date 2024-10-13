import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
import pyodbc
from dao.PayrollService import PayrollService
from entity.Payroll import Payroll
from exception.Customexceptions import PayrollNotFoundException,PayrollGenerationException
from exception.Customexceptions import DatabaseConnectionException,EmployeeNotFoundException
from util.DBConn import DBConn
class IPayrollService(PayrollService):
    def __init__(self):
        self.conn = DBConn.get_db_conn()
        self.payrolls={}

   
    def generate_payroll(self, payroll: Payroll):
        try:
            payroll_id = len(self.payrolls) + 1
            cursor = self.conn.cursor()
            payroll.Netsalary = payroll.Basicsalary + payroll.OvertimePay - payroll.Deductions
        
            cursor.execute("""
                INSERT INTO Payroll (employee_id, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    payroll.employee_id,
                    payroll.PayPeriodStartDate,
                    payroll.PayPeriodEndDate,
                    payroll.Basicsalary,
                    payroll.OvertimePay,
                    payroll.Deductions,
               
                ))
            self.conn.commit()
            print("Payroll generated successfully")
        except:
            raise PayrollGenerationException(f"Payroll not generated properly")

    def GetPayrollById(self, payroll_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE Payroll_id = ?",payroll_id)
            row = cursor.fetchone()
            if row:
                print(f"employee_id:{row[0]},PayPeriodStartDate:{row[1]},PayPeriodEndDate:{row[2]},Basicsalary:{row[3]},OvertimePay:{row[4]},Deductions:{row[5]}")
                
            else:
                raise EmployeeNotFoundException(f"Payroll with ID {payroll_id} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def GetPayrollsForEmployee(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE employee_id= ?",employee_id)
            row = cursor.fetchone()
            if row:
                print(f"Payroll_id:{row[0]},employee_id:{row[1]},PayPeriodStartDate:{row[2]},PayPeriodEndDate:{row[3]},Basicsalary:{row[4]},OvertimePay:{row[5]},Deductions:{row[6]},Netsalary:{row[7]}")
                
            else:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")
   
    def GetPayrollsForPeriod(self, PayPeriodStartDate, PayPeriodEndDate):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            SELECT * FROM Payroll
            WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?
            """, (PayPeriodStartDate, PayPeriodEndDate))
        
            rows = cursor.fetchall()
        
            if rows:
                for row in rows:
                    print(f"PayrollID:{row[0]}, EmployeeID:{row[1]}, PayPeriodStartDate:{row[2]}, "
                      f"PayPeriodEndDate:{row[3]}, BasicSalary:{row[4]}, OvertimePay:{row[5]}, "
                      f"Deductions:{row[6]}, NetSalary:{row[7]}")
            else:
                raise PayrollNotFoundException(f"No payrolls found between {PayPeriodStartDate} and {PayPeriodEndDate}.")

        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")
        
     #For Unit testing
    def CalculateSalary(self,Basicsalary,Overtimepay,Deductions):
        NetSalary=Basicsalary+Overtimepay-Deductions
        return NetSalary
    
    def CalculateGrossSalaryForEmployee(self, Basicsalary, Overtimepay):
        
        if Basicsalary < 0 or Overtimepay < 0:
            raise ValueError("Salary components cannot be negative.")

        return Basicsalary + Overtimepay

