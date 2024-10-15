from Venue import Venue
from Event import Event 
from Event import EventType
from IEventServiceProvider import IEventServiceProvider
from Event import Movie
from Event import Sports 
from Event import Concert 

class EventNotFoundException(Exception):
    def __init__(self, message="Event not found."):
        self.message = message
        super().__init__(self.message)

class EventServiceProviderImpl(IEventServiceProvider):
    def __init__(self):
        self.events = set()

    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                        event_type: str, venue: Venue) -> Event:
        
        if event_type == "Movie":
            genre = input('Enter genre: ')
            actor_name = input("Enter actor name: ")
            actress_name = input("Enter actress name: ")
            event = Movie(event_name, date, time, venue, total_seats, ticket_price, EventType.Movie, genre, actor_name, actress_name)
        elif event_type == "Sport":
            sport_name = input("sport name: ")
            teams_name = input("teams name: ")
            event = Sports(event_name, date, time, venue, total_seats, ticket_price, EventType.Sports, sport_name, teams_name)
        elif event_type == "Concert":
            artist = input("artist name: ")
            concert_type = input("enter concert type: ")
            event = Concert(event_name, date, time, venue, total_seats, ticket_price, EventType.Concert, artist, concert_type)
        else:
            raise ValueError("Invalid event type. Supported types are: movie, sport, concert")

        if event not in self.events:
            self.events.add(event)
            print(self.events)
            print("Event created successfully")
            return event
        else:
            raise EventNotFoundException("Event already exists.")

    def getAvailableNoOfTickets(self):
        total_available_tickets = 0
        for event in self.events:
            total_available_tickets += event.available_seats
        return total_available_tickets

    def getEventDetails(self):
        for event in self.events:
            event.display_event_details()
