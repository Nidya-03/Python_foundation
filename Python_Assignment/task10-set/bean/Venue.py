class Venue:
    def __init__(self, venue_name=None, address=None):
        self.venue_name = venue_name
        self.address = address

    def display_venue_details(self):
        print("Venue Name:", self.venue_name)
        print("Address:", self.address)

    
    def get_venue_name(self):
        return self.venue_name

    def set_venue_name(self, venue_name):
        self.venue_name = venue_name

    
    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address


