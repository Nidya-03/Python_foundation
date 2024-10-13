import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
from util.DBConn import DBConn
class Tax(DBConn):
    def __init__(self, tax_id, employee_id, Taxyear, 
                 TaxableIncome, TaxAmount):
        self.tax_id = tax_id
        self.employee_id = employee_id
        self.Taxyear = Taxyear
        self.TaxableIncome = TaxableIncome
        self.TaxAmount = TaxAmount

    def get_TaxID(self):
        return self.tax_id

    def set_TaxID(self,tax_id):
        self.tax_id= tax_id

    def get_EmployeeID(self):
        return self.employee_id 

    def set_EmployeeID(self, employee_id ):
        self.employee_id  = employee_id 

    def get_TaxYear(self):
        return self.Taxyear

    def set_TaxYear(self, Taxyear):
        self.Taxyear = Taxyear

    def get_TaxableIncome(self):
        return self.TaxableIncome

    def set_TaxableIncome(self, TaxableIncome):
        self.TaxableIncome = TaxableIncome

    def get_TaxAmount(self):
        return self.TaxAmount

    def set_TaxAmount(self, TaxAmount):
        self.TaxAmount = TaxAmount
        
    def __str__(self):
        return (f"TaxID: {self.tax_id}, EmployeeID: {self.employee_id}, "
                f"TaxYear: {self.Taxyear}, TaxableIncome: {self.TaxableIncome}, "
                f"TaxAmount: {self.TaxAmount}")
