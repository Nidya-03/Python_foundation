import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
import unittest
from dao.IPayrollService import IPayrollService
from dao.ITaxService import ITaxService


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



if __name__ == '__main__':
    unittest.main()


