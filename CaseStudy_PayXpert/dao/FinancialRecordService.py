from abc import ABC, abstractmethod

class FinancialRecordService(ABC):
    @abstractmethod
    def AddFinancialRecord(self, employee_id, Description, Amount, Recordtype):
        pass

    @abstractmethod
    def GetFinancialRecordById(self, record_id):
        pass

    @abstractmethod
    def GetFinancialRecordsForEmployee(self, employee_id):
        pass

    @abstractmethod
    def GetFinancialRecordsForDate(self, RecordDate):
        pass