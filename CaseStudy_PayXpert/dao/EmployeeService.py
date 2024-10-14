import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
from abc import ABC, abstractmethod
from exception.Customexceptions import EmployeeNotFoundException, InvalidInputException

class EmployeeService(ABC):
    @abstractmethod
    def get_employee_by_id(self, employee_id):
        raise EmployeeNotFoundException
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def add_employee(self, employee):
        raise InvalidInputException
        pass

    @abstractmethod
    def update_employee(self, employee):
        raise InvalidInputException
        pass

    @abstractmethod
    def remove_employee(self, employee_id):
        raise InvalidInputException
        pass

