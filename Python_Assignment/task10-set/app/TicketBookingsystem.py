
from IBookingSystemServiceProvider import IBookingSystemServiceProvider
from IEventServiceProvider import IEventServiceProvider
from Event import Event
from Customer import Customer
from Booking import Booking 
from EventServiceProviderImpl import EventServiceProviderImpl
from BookingSystemServiceProviderImpl import BookingSystemServiceProviderImpl
from EventServiceProviderImpl import EventNotFoundException
from BookingSystemServiceProviderImpl import InvalidBookingIDException





if __name__ == "__main__":
    EventImpl = EventServiceProviderImpl()
    BookingImpl = BookingSystemServiceProviderImpl(EventImpl)

    
    if id(EventImpl) == id(BookingImpl):
        print("EventImpl and BookingImpl are the same instances.")
    else:
        print("EventImpl and BookingImpl are different instances.")


    while True:
        print("\nAvailable Commands:")
        print("1. create_event")
        print("2. book_tickets")
        print("3. cancel_booking")
        print("4. get_available_seats")
        print("5. get_event_details")
        print("6. calculate_booking_cost")
        print("7. get_booking_details")
        print("8. exit")

        command = input("Enter a command: ").strip()
        try:
            if command == "create_event":
                event_name = input("Enter event name: ")
                date = input("Enter event date (YYYY-MM-DD): ")
                time = input("Enter event time (HH:MM): ")
                total_seats = int(input("Enter total seats: "))
                ticket_price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (Movie/Sports/Concert): ")
                venue_name = input("Enter venue name: ")
                venue_address = input("Enter venue address: ")

                venue = Venue(venue_name, venue_address)
                event = EventImpl.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)

                print(f"Event Name: {event.event_name}")
                print(f"Event Date: {event.event_date}")
                print(f"Event Time: {event.event_time}")
                print(f"Total Seats: {event.total_seats}")
                event_type = event.event_type.value
                print("EventType: ", event_type)
                print(f"Ticket Price: ${event.ticket_price}")
                print(f"Venue: {event.venue.venue_name}")

                

            elif command == "book_tickets":
                # event_name = input("Enter event name: ")
                # date = input("Enter event date (YYYY-MM-DD): ")
                # time = input("Enter event time (HH:MM): ")
                # total_seats = int(input("Enter total seats: "))
                # ticket_price = float(input("Enter ticket price: "))
                # event_type = input("Enter event type (Movie/Sports/Concert): ")
                # venue_name = input("Enter venue name: ")
                # venue_address = input("Enter venue address: ")

                # venue = Venue(venue_name, venue_address)
                # EventImpl.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)

                event_name = input("Enter event name: ")
                num_tickets = int(input("Enter number of tickets to book: "))
                array_of_customers = set()
                for i in range(num_tickets):
                    customer_name = input("Enter customer name: ")
                    email = input("Enter customer email: ")
                    phone_number = input("Enter customer phone number: ")
                    customer = Customer(customer_name, email, phone_number)
                    array_of_customers.add(customer)
                BookingImpl.book_tickets(event_name, num_tickets, array_of_customers)

            elif command == "cancel_booking":
                # event_name = input("Enter event name: ")
                # date = input("Enter event date (YYYY-MM-DD): ")
                # time = input("Enter event time (HH:MM): ")
                # total_seats = int(input("Enter total seats: "))
                # ticket_price = float(input("Enter ticket price: "))
                # event_type = input("Enter event type (Movie/Sports/Concert): ")
                # venue_name = input("Enter venue name: ")
                # venue_address = input("Enter venue address: ")

                # venue = Venue(venue_name, venue_address)
                # EventImpl.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)

                # event_name = input("Enter event name: ")
                # num_tickets = int(input("Enter number of tickets to book: "))
                # array_of_customers = []
                # for i in range(num_tickets):
                #     customer_name = input("Enter customer name: ")
                #     email = input("Enter customer email: ")
                #     phone_number = input("Enter customer phone number: ")
                #     customer = Customer(customer_name, email, phone_number)
                #     array_of_customers.append(customer)
                # BookingImpl.book_tickets(event_name, num_tickets, array_of_customers)



                booking_id = int(input("Enter booking ID: "))
                BookingImpl.cancel_booking(booking_id)

            elif command == "get_available_seats":
                print("Total Available Seats:", EventImpl.getAvailableNoOfTickets())

            elif command == "get_event_details":
                EventImpl.getEventDetails()

            elif command == "calculate_booking_cost":
                # event_name = input("Enter event name: ")
                # date = input("Enter event date (YYYY-MM-DD): ")
                # time = input("Enter event time (HH:MM): ")
                # total_seats = int(input("Enter total seats: "))
                ticket_price = float(input("Enter ticket price: "))
                # event_type = input("Enter event type (Movie/Sports/Concert): ")
                # venue_name = input("Enter venue name: ")
                # venue_address = input("Enter venue address: ")

                # venue = Venue(venue_name, venue_address)
                # EventImpl.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)

                # event_name = input("Enter event name: ")
                num_tickets = int(input("Enter number of tickets to book: "))
                # array_of_customers = []
                # for i in range(num_tickets):
                #     customer_name = input("Enter customer name: ")
                #     email = input("Enter customer email: ")
                #     phone_number = input("Enter customer phone number: ")
                #     customer = Customer(customer_name, email, phone_number)
                #     array_of_customers.append(customer)
                # BookingImpl.book_tickets(event_name, num_tickets, array_of_customers)

                print(BookingImpl.calculate_booking_cost(num_tickets, ticket_price))  

            elif command == "get_booking_details":

                # event_name = input("Enter event name: ")
                # date = input("Enter event date (YYYY-MM-DD): ")
                # time = input("Enter event time (HH:MM): ")
                # total_seats = int(input("Enter total seats: "))
                # ticket_price = float(input("Enter ticket price: "))
                # event_type = input("Enter event type (Movie/Sports/Concert): ")
                # venue_name = input("Enter venue name: ")
                # venue_address = input("Enter venue address: ")

                # venue = Venue(venue_name, venue_address)
                # EventImpl.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)

                # event_name = input("Enter event name: ")
                # num_tickets = int(input("Enter number of tickets to book: "))
                # array_of_customers = []
                # for i in range(num_tickets):
                #     customer_name = input("Enter customer name: ")
                #     email = input("Enter customer email: ")
                #     phone_number = input("Enter customer phone number: ")
                #     customer = Customer(customer_name, email, phone_number)
                #     array_of_customers.append(customer)
                # BookingImpl.book_tickets(event_name, num_tickets, array_of_customers)

                booking_id = input()
                
                BookingImpl.get_booking_details(booking_id)


            elif command == "exit":
                print("Exiting program.")
                break

            else:
                print("Invalid command.")


        except EventNotFoundException as e:
            print("Error:", e)
            print("Please make sure to enter a valid event.")
        except InvalidBookingIDException as e:
            print("Error:", e)
            print("Please make sure to enter a valid booking ID.")
        except Exception as e:
            print(f"An error occurred: {e}")