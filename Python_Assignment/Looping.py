available_tickets = int(input("Enter the number of tickets available: "))
no_booked_tickets = int(input("Enter the number of tickets booked: "))

if available_tickets > no_booked_tickets:
    remaining_tickets = available_tickets - no_booked_tickets
    print(f"Hooray!! {remaining_tickets} tickets available")
else:
    print("Sorry :( No tickets available")
    exit()

print("Welcome to Ticket Booking System")
print("Ticket types: Silver=200 \nGold=500 \nDiamond=1000")

while True:
    ticket_type = input("Enter ticket type (Silver/Gold/Diamond) or type 'Exit' to quit: ").strip()
    
    if ticket_type == "Exit":
        print("Thank you for using the Ticket Booking System!!!")
        break
    
    if ticket_type in ["Silver", "Gold", "Diamond"]:
        no_tickets_needed = int(input("Enter the number of tickets needed: "))
        
        if no_tickets_needed > remaining_tickets:
            print("Not enough tickets available.")
            continue
        if ticket_type == 'Silver':
            base_price = 200
        elif ticket_type == 'Gold':
            base_price = 500
        elif ticket_type == 'Diamond':
            base_price = 1000
        
        total_cost = base_price * no_tickets_needed
        print(f"Total cost for {no_tickets_needed} {ticket_type} tickets: {total_cost}")
        remaining_tickets -= no_tickets_needed
        print(f"Remaining tickets: {remaining_tickets}")
        if remaining_tickets == 0:
            print("All tickets are sold out!")
            break
    else:
        print("Invalid ticket type. Please enter a valid ticket type (Silver/Gold/Diamond).")


