
from entity.Employee import Employee
from entity.Payroll import Payroll
from entity.FinancialRecord import FinancialRecord
from dao.IEmployeeService import IEmployeeService
from dao.IPayrollService import IPayrollService
from dao.ITaxService import ITaxService
from dao.IFinancialRecordService import IFinancialRecordService
from exception.Customexceptions import *


class PayXpert:
    def print_menu():
        print("1. Add Employee")
        print("2. Get Employee by ID")
        print("3. Get All Employees")
        print("4. Update Employee")
        print("5. Remove Employee")
        print("6. Get Payroll by ID")
        print("7. Add Payroll")
        print("8. Get Payrolls for Employee")
        print("9. Get Payrolls for Period")
        print("10. Calculate Tax")
        print("11. Get Tax By Id")
        print("12. Get Tax for Employee")
        print("13. Get Tax for Year")
        print("14. Get Financial Record by ID")
        print("15. Add Financial Record")
        print("16. Get Financial Records for Employee")
        print("17. Get Financial Records for Date")
        print("18. Exit")

    def main():
        employee_service = IEmployeeService()
        payroll_service = IPayrollService()
        tax_service = ITaxService()
        financial_record_service = IFinancialRecordService()

        while True:
            print("\nPayXpert Payroll Management System")
            PayXpert.print_menu()
            employeecount=1
            choice = input("Enter your choice (1-18): ")
            if choice == "1":
           
            
                Firstname = input("Enter first name: ")
                Lastname = input("Enter last name: ")
                Dateofbirth = input("Enter date of birth (YYYY-MM-DD): ")
                Gender = input("Enter gender: ")
                Email = input("Enter email: ")
                Phonenumber = input("Enter phone number: ")
                Address = input("Enter address: ")
                Position = input("Enter position: ")
                Joiningdate = input("Enter joining date (YYYY-MM-DD): ")
                Terminationdate = input("Enter termination date (YYYY-MM-DD): ")

                employee =Employee(str(employeecount),Firstname,Lastname,Dateofbirth,Gender,Email,Phonenumber,Address,Position,Joiningdate,Terminationdate)

                employee_service.add_employee(employee)

            elif choice == "2":

                employee_id = input("Enter employee ID: ")

                employee_service.get_employee_by_id(employee_id)

            elif choice == "3":
          
                employee_service.get_all_employees()

            elif choice == "4":

                try:
                    employee_id = int(input("Enter employee ID to update: "))
                    Firstname = input("Enter first name: ")
                    Lastname = input("Enter last name: ")
                    Dateofbirth = input("Enter date of birth (YYYY-MM-DD): ")
                    Gender = input("Enter gender: ")
                    Email = input("Enter email: ")
                    Phonenumber = input("Enter phone number: ")
                    Address = input("Enter address: ")
                    Position = input("Enter position: ")
                    Joiningdate = input("Enter joining date (YYYY-MM-DD): ")
                    Terminationdate = input("Enter termination date (YYYY-MM-DD): ")
                    employee =Employee(employee_id,Firstname,Lastname,Dateofbirth,Gender,Email,Phonenumber,Address,Position,Joiningdate,Terminationdate)
                    employee_service.update_employee(employee)

                except ValueError:

                    print("Invalid input. Please enter a valid employee ID.")


            elif choice == "5":
        
                employee_id = int(input("Enter employee ID to remove: "))
                employee_service.remove_employee(employee_id)

            elif choice == "6":

                payroll_id = int(input("Enter payroll ID: "))
                payroll = payroll_service.GetPayrollById(payroll_id)

            elif choice == "7":
           
                payrollcount=101
                employee_id=input("Enter the employee id: ")
                PayPeriodStartDate = input("Enter Pay period start date (YYYY-MM-DD): ")
                PayPeriodEndDate = input("Enter Pay period end date (YYYY-MM-DD): ")
                Basicsalary = int(input("Enter Basic salary: "))
                OvertimePay = int(input("Enter Overtime Pay: "))
                Deductions = int(input("Enter Deductions: "))
                payroll =Payroll(str(payrollcount),employee_id,PayPeriodStartDate,PayPeriodEndDate,Basicsalary,OvertimePay,Deductions)
                payroll_service.generate_payroll(payroll)

            elif choice == "8":

                employee_id = int(input("Enter employee ID: "))
                payroll_service = IPayrollService()
                payroll_service.GetPayrollsForEmployee(employee_id)
                
            elif choice == "9":
           
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                payroll_service.GetPayrollsForPeriod(start_date, end_date)

            elif choice == "10":
           
                employee_id = int(input("Enter employee ID: "))
                Taxyear = (input("Enter tax year: "))
                tax_service.CalculateTax(employee_id, Taxyear)

            elif choice=="11":
                tax_id = int(input("Enter Tax ID: "))
                tax_service.GetTaxById(tax_id)

            elif choice=="12":
                employee_id = int(input("Enter employee ID: "))
                tax_service.GetTaxesForEmployee(employee_id)
            
            elif choice=="13":
                Taxyear = input("Enter Tax year: ")
                tax_service.GetTaxesForYear(Taxyear)

            elif choice == "14":
           
                record_id = int(input("Enter record ID: "))
                financial_record_service.GetFinancialRecordById(record_id)

            elif choice == "15":
            
                financialcount=301
                employee_id= int(input("Enter employee ID: "))
                Recorddate= input("Enter record date (YYYY-MM-DD): ")
                Description= input("Enter description: ")
                Amount= float(input("Enter the amount: " ))
                Recordtype= input("Enter record type: ")
                financialrecord =FinancialRecord(str(financialcount),employee_id,Recorddate,Description,Amount,Recordtype)
                financial_record_service.AddFinancialRecord(financialrecord)

            elif choice == "16":
            
                employee_id = int(input("Enter employee ID: "))
                financial_record_service.GetFinancialRecordsForEmployee(employee_id)

            elif choice == "17":
          
                record_date = input("Enter record date (YYYY-MM-DD): ")
                financial_record_service.GetFinancialRecordsForDate(record_date)

            elif choice == "18":
                print("Exiting PayXpert.")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 15.")

if __name__ == "__main__":
    px=PayXpert.main()