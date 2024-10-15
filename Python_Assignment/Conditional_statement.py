available_tickets=int(input("Enter no of tickets available: "))
no_bookedtickets=int(input("Enter no of tickets booked: "))

if available_tickets>no_bookedtickets:
    remaining_tickets=available_tickets-no_bookedtickets
    print(f"Hooray!! {remaining_tickets} tickets available")
else:
    print("Sorry :( No tickets available")
