
class Customer:
    def __init__(self, customer_id, name, email, phone_number, address, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.credit_score = credit_score

    def get_customer_id(self):
        return self.customer_id
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_phone_number(self):
        return self.phone_number
    def get_address(self):
        return self.address
    def get_credit_score(self):
        return self.credit_score

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    def set_name(self, name):
        self.name = name
    def set_email(self, email):
        self.email = email
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    def set_address(self, address):
        self.address = address
    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    def __str__(self):
        return (f"Customer ID: {self.customer_id}\nName: {self.name}\nEmail: {self.email}\n"
                f"Phone Number: {self.phone_number}\nAddress: {self.address}\nCredit Score: {self.credit_score}")


