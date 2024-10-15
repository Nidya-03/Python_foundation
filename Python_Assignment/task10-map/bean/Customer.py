class Customer:
    def __init__(self, customer_name=None, email=None, phone_number=None):
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number

    def display_customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)

    
    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    
    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

