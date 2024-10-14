from abc import ABC, abstractmethod

class PayrollService(ABC):
    @abstractmethod
    def generate_payroll(self, employee_id, PayPeriodStartDate, PayPeriodEndDate):
        pass

    @abstractmethod
    def GetPayrollById(self, Payroll_id):
        pass

    @abstractmethod
    def GetPayrollsForEmployee(self, employee_id):
        pass

    @abstractmethod
    def GetPayrollsForPeriod(self, PayPeriodStartDate, PayPeriodEndDate):
        pass