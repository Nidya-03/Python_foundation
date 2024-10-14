import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
import unittest
from unittest.mock import MagicMock
from dao.IPayrollService import IPayrollService
from dao.ITaxService import ITaxService
from dao.IEmployeeService import IEmployeeService
from entity.Payroll import Payroll
from exception.Customexceptions import PayrollGenerationException
from datetime import datetime


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
    def tearDown(self):
        # Clean up resources if necessary
        self.payroll_service = None
        
    
    def test_verify_error_handling_for_invalid_employee_data(self):
        self.payroll_service=IPayrollService()
        # Prepare invalid employee data (non-existent employee_id)
        invalid_payroll = Payroll(
            Payroll_id=888, #invalid 
            employee_id=9999,  # Assuming 9999 is an invalid ID
            PayPeriodStartDate=datetime(2024, 10, 1),
            PayPeriodEndDate=datetime(2024, 10, 31),
            Basicsalary=50000,
            OvertimePay=5000,
            Deductions=2000
        )

        with self.assertRaises(PayrollGenerationException) as context:
            self.payroll_service.generate_payroll(invalid_payroll)

        self.assertEqual(
            str(context.exception), "Payroll not generated properly",
            "Error message did not match the expected output."
        )

if __name__ == '__main__':
    unittest.main()


