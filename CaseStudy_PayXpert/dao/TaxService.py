from abc import ABC, abstractmethod

class TaxService(ABC):
    @abstractmethod
    def CalculateTax(self, employee_id, tax_year):
        pass

    @abstractmethod
    def GetTaxById(self, tax_id):
        pass

    @abstractmethod
    def GetTaxesForEmployee(self, employee_id):
        pass

    @abstractmethod
    def GetTaxesForYear(self, tax_year):
        pass