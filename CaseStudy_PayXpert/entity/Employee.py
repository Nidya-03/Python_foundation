import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
from util.DBConn import DBConn
class Employee(DBConn):
    def __init__(self, employee_id, Firstname, Lastname, DateofBirth, Gender, Email, Phonenumber, Address, Position, Joiningdate, Terminationdate):
        self.employee_id = employee_id
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.DateofBirth = DateofBirth
        self.Gender = Gender
        self.Email = Email
        self.Phonenumber = Phonenumber
        self.Address = Address
        self.Position = Position
        self.Joiningdate = Joiningdate
        self.Terminationdate = Terminationdate

    def get_EmployeeID(self):
        return self.employee_id
    def set_EmployeeID(self, employee_id):
        self.employee_id = employee_id

    def get_firstname(self):
        return self.Firstname
    def set_firstname(self, Firstname):
        self.Firstname = Firstname

    def get_lastname(self):
        return self.Lastname
    def set_lastname(self, Lastname):
        self.Lastname = Lastname

    def get_dateofbirth(self):
        return self.DateofBirth
    def set_dateofbirth(self, DateofBirth):
        self.DateofBirth = DateofBirth

    def get_gender(self):
        return self.Gender
    def set_gender(self, Gender):
        self.Gender = Gender

    def get_email(self):
        return self.Email
    def set_email(self, Email):
        self.Email = Email

    def get_Phonenumber(self):
        return self.Phonenumber
    def set_Phonenumber(self, Phonenumber):
        self.Phonenumber = Phonenumber

    def get_address(self):
        return self.Address
    def set_address(self, Address):
        self.Address = Address

    def get_position(self):
        return self.Position
    def set_position(self, Position):
        self.Position = Position

    def get_joiningdate(self):
        return self.Joiningdate
    def set_joiningdate(self, Joiningdate):
        self.Joiningdate = Joiningdate

    def get_Terminationdate(self):
        return self.Terminationdate
    def set_Terminationdate(self, Terminationdate):
        self.Terminationdate = Terminationdate

    def calculate_age(self):
        from datetime import date
        return date.today().year - self.DateofBirth.year
