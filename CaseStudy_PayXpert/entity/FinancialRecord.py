import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
from util.DBConn import DBConn
class FinancialRecord(DBConn):
    def __init__(self, record_id, employee_id, RecordDate, 
                 Description, Amount, RecordType):
        self.record_id = record_id
        self.employee_id = employee_id
        self.RecordDate = RecordDate
        self.Description = Description
        self.Amount = Amount
        self.RecordType = RecordType

    def get_RecordID(self):
        return self.record_id

    def set_RecordID(self, record_id):
        self.record_id = record_id

    def get_EmployeeID(self):
        return self.employee_id

    def set_EmployeeID(self, employee_id):
        self.employee_id = employee_id

    def get_RecordDate(self):
        return self.RecordDate

    def set_RecordDate(self, RecordDate):
        self.RecordDate = RecordDate

    def get_Description(self):
        return self.Description

    def set_Description(self, Description):
        self.Description = Description

    def get_Amount(self):
        return self.Amount

    def set_Amount(self, Amount):
        self.Amount = Amount

    def get_RecordType(self):
        return self.RecordType

    def set_RecordType(self, RecordType):
        self.RecordType = RecordType

    def __str__(self):
        return (f"RecordID: {self.record_id}, EmployeeID: {self.employee_id}, "
                f"RecordDate: {self.RecordDate}, Description: {self.Description}, "
                f"Amount: {self.Amount}, RecordType: {self.RecordType}")
