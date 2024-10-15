

from IBookingSystemServiceProvider import IBookingSystemServiceProvider
from IEventServiceProvider import IEventServiceProvider
from Event import Event
from Booking import Booking
from EventServiceProviderImpl import EventServiceProviderImpl
from datetime import datetime

from EventServiceProviderImpl import EventNotFoundException

class InvalidBookingIDException(Exception):
    def __init__(self, message="Invalid booking ID."):
        self.message = message
        super().__init__(self.message)


class BookingSystemServiceProviderImpl(EventServiceProviderImpl,IBookingSystemServiceProvider):
    def __init__(self, EventImpl):
        super().__init__()
        self.events = EventImpl.events 
        self.bookings = set()
        
    def sort_events(self):
        
        self.events = sorted(self.events, key=lambda event: (event.event_name, event.venue.name))
        
    def calculate_booking_cost(self, num_tickets, ticket_price):
        
        return num_tickets * ticket_price

    def book_tickets(self, event_name: str, num_tickets, array_of_customers):
        
        for event in self.events:
            print("True")
            if event.event_name == event_name:
                print("True")
                if event.available_seats >= num_tickets:
                    print("True")
                    event.book_tickets(num_tickets)
                    booking_date = datetime.now()
                    booking = Booking(array_of_customers, event, num_tickets, booking_date)
                    event.bookings.append(booking)
                    self.bookings.add(booking)  
                    print(f"{num_tickets} tickets booked for {event_name}.")
                    return  
                    
        print("Event not found or tickets sold out.")

    def cancel_booking(self, booking_id):
        try:
            booking_id = int(booking_id)  
            for event in self.events:
                for booking in event.bookings:
                    if booking.bookingId == booking_id:
                        event.cancel_booking(booking.num_tickets)
                        event.bookings.remove(booking)
                        self.bookings.remove(booking)
                        print(f"Booking with ID {booking_id} cancelled.")
                        return
            raise InvalidBookingIDException()  
        except ValueError:
            raise InvalidBookingIDException()  

    def get_booking_details(self, booking_id):
        try:
            booking_id = int(booking_id)  
            for event in self.events:
                for booking in event.bookings:
                    if booking.bookingId == booking_id:
                        
                        print("Booking ID:", booking.bookingId)
                        print("Event Name:", event.event_name)
                        print("Event Date:", event.event_date)
                        print("Number of Tickets:", booking.num_tickets)

                        
                        return
            raise InvalidBookingIDException()  
        except ValueError:
            raise InvalidBookingIDException() 
