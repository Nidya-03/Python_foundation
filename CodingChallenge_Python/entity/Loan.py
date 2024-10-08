class Loan:
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term_months, loan_type, loan_status):
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term_months = loan_term_months
        self.loan_type = loan_type
        self.loan_status = loan_status

    def get_loan_id(self):
        return self.loan_id
    def get_customer_id(self):
        return self.customer_id
    def get_principal_amount(self):
        return self.principal_amount
    def get_interest_rate(self):
        return self.interest_rate
    def get_loan_term_months(self):
        return self.loan_term_months
    def get_loan_type(self):
        return self.loan_type
    def get_loan_status(self):
        return self.loan_status
    
    def set_loan_id(self, loan_id):
        self.loan_id = loan_id
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    def set_principal_amount(self, principal_amount):
        self.principal_amount = principal_amount
    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate
    def set_loan_term_months(self, loan_term_months):
        self.loan_term_months = loan_term_months
    def set_loan_type(self, loan_type):
        self.loan_type = loan_type
    def set_loan_status(self, loan_status):
        self.loan_status = loan_status

class HomeLoan(Loan):
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term_months, property_address, property_value):
        super().__init__(loan_id, customer_id, principal_amount, interest_rate, loan_term_months, "HomeLoan", "Pending")
        self.property_address = property_address
        self.property_value = property_value

    def get_property_address(self):
        return self.property_address
    def get_property_value(self):
        return self.property_value

    def set_property_address(self, property_address):
        self.property_address = property_address
    def set_property_value(self, property_value):
        self.property_value = property_value

class CarLoan(Loan):
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term_months, car_model, car_value):
        super().__init__(loan_id, customer_id, principal_amount, interest_rate, loan_term_months, "CarLoan", "Pending")
        self.car_model = car_model
        self.car_value = car_value

    def get_car_model(self):
        return self.car_model
    def get_car_value(self):
        return self.car_value

    def set_car_model(self, car_model):
        self.car_model = car_model
    def set_car_value(self, car_value):
        self.car_value = car_value


    