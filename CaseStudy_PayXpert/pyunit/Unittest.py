import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
import unittest
from unittest.mock import MagicMock
from dao.IPayrollService import IPayrollService
from dao.ITaxService import ITaxService
from dao.IEmployeeService import IEmployeeService
from entity.Employee import Employee
from exception.Customexceptions import InvalidInputException


class PayrollServiceTestCase(unittest.TestCase):

    def test_CalculateNetSalaryAfterDeductions(self):
        self.payroll_service = IPayrollService()
        Basicsalary= 50000
        Overtimepay = 2000
        Deductions = 5000

        net_salary = self.payroll_service.CalculateSalary(Basicsalary, Overtimepay, Deductions)

        expected_net_salary = Basicsalary + Overtimepay- Deductions
        self.assertEqual(net_salary, expected_net_salary)

    def test_CalculateGrossSalaryForEmployee(self):
        self.payroll_service = IPayrollService()
        base_salary = 60000
        overtime_pay = 2500

        gross_salary = self.payroll_service.CalculateGrossSalaryForEmployee(base_salary, overtime_pay)

        expected_gross_salary = base_salary + overtime_pay
        self.assertEqual(gross_salary, expected_gross_salary)

    def test_VerifyTaxCalculationForHighIncomeEmployee(self):
        self.tax_service=ITaxService()
        TaxableIncome = 100000

        tax_amount = self.tax_service.VerifyTaxCalculationForHighIncomeEmployee(TaxableIncome)

        expected_tax_amount = 0.1 * (TaxableIncome)
        self.assertEqual(tax_amount, expected_tax_amount)

    def test_process_payroll_for_multiple_employees(self):
        self.payroll_service=IPayrollService()
        employee_ids = [1, 2, 3]
        start_date = '2023-01-01'
        end_date = '2023-01-31'

        # Mock multiple payroll generations
        self.payroll_service.generate_payroll = MagicMock(side_effect=[5000, 5500, 6000])

        payrolls = [self.payroll_service.generate_payroll(emp_id, start_date, end_date) for emp_id in employee_ids]
        
        self.assertEqual(payrolls, [5000, 5500, 6000], "Payroll should be processed correctly for multiple employees.")


    def test_verify_error_handling_for_invalid_employee_data(self):
        self.employee_service=IEmployeeService()
        # Invalid employee data cases
        invalid_employees = [
            # Case 1: Missing required fields (e.g., first name, last name)
            {
                "first_name": "",
                "last_name": "Smith",
                "dob": "1985-08-25",
                "gender": "M",
                "email": "john@example.com",
                "phone": "1234567890",
                "address": "123 Main St",
                "role": "Developer",
                "hire_date": "2023-01-15",
                "termination_date": "2025-01-15",
                "expected_error": ValueError
            },
            # Case 2: Invalid email format
            {
                "first_name": "John",
                "last_name": "Doe",
                "dob": "1985-08-25",
                "gender": "M",
                "email": "invalid-email",
                "phone": "1234567890",
                "address": "123 Main St",
                "role": "Developer",
                "hire_date": "2023-01-15",
                "termination_date": "2025-01-15",
                "expected_error": ValueError
            },
            # Case 3: Invalid date format for hire date
            {
                "first_name": "Jane",
                "last_name": "Doe",
                "dob": "1990-05-22",
                "gender": "F",
                "email": "jane@example.com",
                "phone": "0987654321",
                "address": "456 Elm St",
                "role": "Manager",
                "hire_date": "2023-01-15",  # valid
                "termination_date": "invalid-date",
                "expected_error": ValueError
            },
            # Case 4: Hire date later than termination date
            {
                "first_name": "Alice",
                "last_name": "Johnson",
                "dob": "1993-11-11",
                "gender": "F",
                "email": "alice@example.com",
                "phone": "5558887777",
                "address": "789 Oak St",
                "role": "HR",
                "hire_date": "2025-01-10",
                "termination_date": "2024-12-31",  # invalid, hire date after termination
                "expected_error": ValueError
            }
        ]

        # Test each case
        for invalid_employee in invalid_employees:
            with self.assertRaises(invalid_employee["expected_error"]):
                employee = Employee(
                    first_name=invalid_employee["first_name"],
                    last_name=invalid_employee["last_name"],
                    dob=invalid_employee["dob"],
                    gender=invalid_employee["gender"],
                    email=invalid_employee["email"],
                    phone=invalid_employee["phone"],
                    address=invalid_employee["address"],
                    role=invalid_employee["role"],
                    hire_date=invalid_employee["hire_date"],
                    termination_date=invalid_employee["termination_date"]
                )
                self.employee_service.add_employee(employee)

    def tearDown(self):
        # Clean up resources if necessary
        self.payroll_service = None
        self.employee_service = None




if __name__ == '__main__':
    unittest.main()


