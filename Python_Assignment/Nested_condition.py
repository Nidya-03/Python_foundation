print("Welcome to Ticket Booking System")
print("Ticket types: Silver=200 \n Gold=500 \n Diamond=1000")

while True:
    ticket_type = input("Enter ticket type (Silver/Gold/Diamond): ")
    if ticket_type in ["Silver", "Gold", "Diamond"]:
        no_tickets_needed = int(input("Enter the number of tickets needed: "))
        if ticket_type == 'Silver':
            base_price = 200
        elif ticket_type == 'Gold':
            base_price = 500
        elif ticket_type == 'Diamond':
            base_price = 1000
        total_cost = base_price * no_tickets_needed
        print(f"Total cost for {no_tickets_needed} {ticket_type} tickets: {total_cost}")
        break  
    else:
        print("Invalid ticket type. Please enter a valid ticket type (Silver/Gold/Diamond).")
