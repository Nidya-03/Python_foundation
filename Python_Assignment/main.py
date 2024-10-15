import functools
from datetime import *
import pyodbc
from dbutil import DBConnection
from abstractrepo import BookingSystemRepositoryImpl

class EventNotFoundException(Exception):
    pass

class InvalidBookingIDException(Exception):
    pass

con = DBConnection.getConnection()
cur = con.cursor()

class BookingSystemRepository(BookingSystemRepositoryImpl):

    def create_event(self):
        eventcount=101
        
        event_name = input("Enter event name: ")

        
        event_date = self.get_current_date().strftime('%Y-%m-%d')
        event_time = self.get_current_time().strftime('%H:%M:%S')

        total_seats = int(input("Enter total seats: "))
        ticket_price = float(input("Enter ticket price: "))
        event_type = input("Enter event type (movie, sport, concert): ")

       
        query = """
        INSERT INTO event( event_name, event_date, event_time, total_seats, 
        ticket_price, event_type)
        VALUES ( ?, ?, ?, ?, ?, ?)
        """
        values=(event_name,event_date,event_time,total_seats,ticket_price,event_type)

        # Execute the query and commit
        try:
            cur.execute(query, values)
            con.commit()
            print("Event created successfully.")
        except pyodbc.Error as e:
            print(f"Error: {e}")
        finally:
            cur.execute("SELECT * FROM event")
            events = cur.fetchall()
            for event in events:
                print(event)

    def get_current_date(self):
        return date.today()

    def get_current_time(self):
        return datetime.now().time()

    def get_event_details(self):
        return self.all_events()

    def all_events(self):
        query = "SELECT * FROM event"
        cur.execute(query)
        events = cur.fetchall()
        for event in events:
            print(event)

    def get_available_tickets(self):
        query = "SELECT available_seats, event_name FROM event"
        cur.execute(query)
        events = cur.fetchall()
        for event in events:
            print(event)

    def create_customer(self):
        
        customer_name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        

        query = "INSERT INTO customer( customer_name, email, phone_number) VALUES(?,?,?)"
        values = ( customer_name, email, phone)

        cur.execute(query, values)
        con.commit()
        print("Customer created successfully.")
          

    def get_all_customers(self):
        query = "SELECT * FROM customer"
        cur.execute(query)
        return cur.fetchall()


    def unique_customer_id(self):
        query = "SELECT ISNULL(MAX(customer_id), 0) FROM customer"
        cur.execute(query)
        max_id = cur.fetchone()[0]
        return max_id + 1  # Increment to get a new unique ID

    def book_tickets(self, num_tickets: int):
        self.all_events()
        event_name = input("Enter the event name: ")

       
        query = "SELECT event_id, total_seats, ticket_price FROM event WHERE event_name = ?"
        cur.execute(query, (event_name,))
        event = cur.fetchone()
        if not event:
            print(f"Error: Event '{event_name}' not found.")
            return None

        event_id, total_seats, ticket_price = event

        # Check if enough seats are available
        if num_tickets > total_seats:
            print("Not enough available seats for the requested number of tickets.")
            return None

        customer_id = int(input("Customer id :")) # Get newly created customer ID
        total_cost = float(num_tickets) * float(ticket_price)  # Ensure float conversion
        booking_date = self.get_current_date().strftime('%Y-%m-%d')  # Convert to correct format
        

       
        values = (
            int(customer_id), 
            int(event_id), 
            int(num_tickets),  
            float(total_cost),  
            booking_date  
        )

        
        query2 = """
        INSERT INTO booking( customer_id, event_id, num_tickets, total_cost, booking_date)
        VALUES ( ?, ?, ?, ?, ?)
        """
        cur.execute(query2, values)

       
        new_seat_count = total_seats - num_tickets
        update_query = "UPDATE event SET total_seats = ? WHERE event_id = ?"
        cur.execute(update_query, (new_seat_count, event_id))

        con.commit()
        print(f"Successfully booked {num_tickets} tickets for {event_name}. Remaining seats: {new_seat_count}")

    def get_all_bookings(self):
        query = "SELECT * FROM booking"
        cur.execute(query)
        return cur.fetchall()

    def unique_booking_id(self):
        return len(self.get_all_bookings()) + 1


    def cancel_tickets(self):
        booking_id = int(input("Enter the booking_id: "))

        query = "SELECT booking_id FROM booking WHERE booking_id = ?"
        cur.execute(query, (booking_id,))
        booking = cur.fetchone()
        if not booking:
            print(f"Error: {booking_id} not found")
            return

        query = "SELECT num_tickets FROM booking WHERE booking_id = ?"
        cur.execute(query, (booking_id,))
        num_tickets = cur.fetchone()[0]

        query = "DELETE FROM booking WHERE booking_id = ?"
        cur.execute(query, (booking_id,))
        con.commit()

        print(f"Successfully canceled {num_tickets} tickets.")


b = BookingSystemRepository()

class TicketBookingSystem:
    while True:
        print("")
        print("1. Create Event")
        print("2. Book tickets")
        print("3. Cancel tickets")
        print("4. Get available tickets")
        print("5. Get event details")
        print("6. Exit")

        choice = input("Select from above options: ")
        if choice == "1":
            b.create_event()
        elif choice == "2":
            num_tickets = int(input("Enter the number of tickets: "))
            b.book_tickets(num_tickets)
        elif choice == "3":
            b.cancel_tickets()
        elif choice == "4":
            b.get_available_tickets()
        elif choice == "5":
            b.get_event_details()
        elif choice == "6":
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid option, choose from the options above.")







