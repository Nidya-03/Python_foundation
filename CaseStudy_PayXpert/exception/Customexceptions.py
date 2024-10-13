
class EmployeeNotFoundException(Exception):
    
    def __init__(self, message="Employee not found."):
        self.message = message
        super().__init__(self.message)

class PayrollGenerationException(Exception):
    
    def __init__(self, message="Error generating payroll."):
        self.message = message
        super().__init__(self.message)

class TaxCalculationException(Exception):
    
    def __init__(self, message="Error calculating taxes."):
        self.message = message
        super().__init__(self.message)

class FinancialRecordException(Exception):
    
    def __init__(self, message="Error managing financial records."):
        self.message = message
        super().__init__(self.message)

class InvalidInputException(Exception):
    
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(Exception):
    
    def __init__(self, message="Database connection error."):
        self.message = message
        super().__init__(self.message)

class PayrollNotFoundException(Exception):
    def __init__(self, message="Pay roll not found."):
        self.message = message
        super().__init__(self.message)
