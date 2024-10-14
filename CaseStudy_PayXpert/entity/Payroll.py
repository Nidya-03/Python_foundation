import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
from util.DBConn import DBConn
class Payroll(DBConn):
    def __init__(self, Payroll_id, employee_id, PayPeriodStartDate, 
                 PayPeriodEndDate, Basicsalary, OvertimePay, 
                 Deductions):
        # Private Variables
        self.Payroll_id = Payroll_id
        self.employee_id = employee_id
        self.PayPeriodStartDate = PayPeriodStartDate
        self.PayPeriodEndDate = PayPeriodEndDate
        self.Basicsalary = Basicsalary
        self.OvertimePay = OvertimePay
        self.Deductions = Deductions
        self.Netsalary = self.Basicsalary + self.OvertimePay - self.Deductions


    # Getters and Setters
    def get_PayrollID(self):
        return self.Payroll_id

    def set_PayrollID(self, Payroll_id):
        self.Payroll_id = Payroll_id

    def get_EmployeeID(self):
        return self.employee_id

    def set_EmployeeID(self, employee_id):
        self.employee_id = employee_id
    def get_PayPeriodStartDate(self):
        return self.PayPeriodStartDate

    def set_PayPeriodStartDate(self, PayPeriodStartDate):
        self.PayPeriodStartDate = PayPeriodStartDate

    def get_PayPeriodEndDate(self):
        return self.PayPeriodEndDate

    def set_PayPeriodEndDate(self, PayPeriodEndDate):
        self.PayPeriodEndDate = PayPeriodEndDate

    def get_BasicSalary(self):
        return self.Basicsalary

    def set_BasicSalary(self, Basicsalary):
        self.Basicsalary = Basicsalary
        self.Netsalary = self.Basicsalary + self.OvertimePay - self.Deductions 

    def get_OvertimePay(self):
        return self.OvertimePay

    def set_OvertimePay(self, OvertimePay):
        self.OvertimePay = OvertimePay
        self.Netsalary = self.Basicsalary + self.OvertimePay - self.Deductions 

    def get_Deductions(self):
        return self.Deductions

    def set_Deductions(self, Deductions):
        self.Deductions = Deductions
        self.Netsalary = self.Basicsalary + self.OvertimePay - self.Deductions  # Recalculate Net Salary

    def get_NetSalary(self):
        return self.Netsalary

    # Overriding __str__ method to display object information
    def __str__(self):
        return (f"PayrollID: {self.Payroll_id}, EmployeeID: {self.employee_id}, "
                f"PayPeriodStartDate: {self.PayPeriodStartDate}, PayPeriodEndDate: {self.PayPeriodEndDate}, "
                f"BasicSalary: {self.Basicsalary}, OvertimePay: {self.OvertimePay}, "
                f"Deductions: {self.Deductions}, NetSalary: {self.Netsalary}")