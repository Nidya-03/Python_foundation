from Event import Event
from datetime import datetime
class Booking:
    bookingId_counter = 1

    def __init__(self, customers, event, num_tickets, booking_date):
        self.bookingId = Booking.bookingId_counter
        Booking.bookingId_counter += 1
        self.customers = {}  
        for idx, customer in enumerate(customers, start=1):
            self.customers[idx] = customer 
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = event.ticket_price * num_tickets
        self.booking_date = booking_date

    def calculate_booking_cost(self):
        self.total_cost = self.event.ticket_price * self.num_tickets

    def book_tickets(self):
        if self.num_tickets <= self.event.available_seats:
            self.event.book_tickets(self.num_tickets)
            self.calculate_booking_cost()
            print(f"{self.num_tickets} tickets booked for {self.event.event_name} on {self.booking_date}.")
        else:
            print("Not enough available seats.")

    def cancel_booking(self):
        self.event.cancel_booking(self.num_tickets)
        print(f"{self.num_tickets} tickets cancelled for {self.event.event_name} on {self.booking_date}.")

    def getAvailableNoOfTickets(self):
        return self.event.available_seats

    def getEventDetails(self):
        return self.event.display_event_details()

