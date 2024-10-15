

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
        self.bookings = {}
        
    def sort_events(self):
        
        self.events = sorted(self.events, key=lambda event: (event.event_name, event.venue.name))
        
    def calculate_booking_cost(self, num_tickets, ticket_price):
        
        return num_tickets * ticket_price

    def book_tickets(self, event_name: str, num_tickets, array_of_customers):
        for event in self.events.values():
            if event.event_name == event_name and event.available_seats >= num_tickets:
                event.book_tickets(num_tickets)
                booking_date = datetime.now()
                booking = Booking(array_of_customers, event, num_tickets, booking_date)
                self.bookings[booking.bookingId] = booking  
                print(f"{num_tickets} tickets booked for {event_name}.")
                return
        print("Event not found or tickets sold out.")


    def cancel_booking(self, booking_id):
        try:
            booking_id = int(booking_id)
            booking = self.bookings.get(booking_id)
            if booking:
                event = booking.event
                event.cancel_booking(booking.num_tickets)
                del self.bookings[booking_id]  
                print(f"Booking with ID {booking_id} cancelled.")
            else:
                raise InvalidBookingIDException()
        except ValueError:
            raise InvalidBookingIDException()

    def get_booking_details(self, booking_id):
        try:
            booking_id = int(booking_id)
            booking = self.bookings.get(booking_id)
            if booking:
                print("Booking ID:", booking.bookingId)
                print("Event Name:", booking.event.event_name)
                print("Event Date:", booking.event.event_date)
                print("Number of Tickets:", booking.num_tickets)
            else:
                raise InvalidBookingIDException()
        except ValueError:
            raise InvalidBookingIDException()
