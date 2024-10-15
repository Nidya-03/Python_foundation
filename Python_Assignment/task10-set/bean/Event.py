from datetime import datetime

from enum import Enum

class EventType(Enum):
    Movie = 'Movie'
    Sports = 'Sports'
    Concert = 'Concert'

class Event:
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue = venue
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = EventType(event_type) 
        self.bookings = [] 

    def get_event_name(self):
        return self.event_name

    def set_event_name(self, event_name):
        self.event_name = event_name

    def get_event_date(self):
        return self.event_date

    def set_event_date(self, event_date):
        self.event_date = event_date

    def get_event_time(self):
        return self.event_time

    def set_event_time(self, event_time):
        self.event_time = event_time

    def get_venue_name(self):
        return self.venue_name

    def set_venue_name(self, venue_name):
        self.venue_name = venue_name

    def get_total_seats(self):
        return self.total_seats

    def set_total_seats(self, total_seats):
        self.total_seats = total_seats

    def get_available_seats(self):
        return self.available_seats

    def set_available_seats(self, available_seats):
        self.available_seats = available_seats

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price

    def get_event_type(self):
        return self.event_type

    def set_event_type(self, event_type):
        self.event_type = event_type
    

    
    def calculate_total_revenue(self):
        return self.ticket_price * (self.total_seats - self.available_seats)
    
    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats
    
    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked successfully for {self.event_name}.")
        else:
            print("Not enough seats available to book the requested number of tickets.")
    
    def cancel_booking(self, num_tickets):
        if num_tickets <= (self.total_seats - self.available_seats):
            self.available_seats += num_tickets
            print(f"{num_tickets} tickets cancelled successfully for {self.event_name}.")
        else:
            print("Invalid number of tickets to cancel.")
    
    def display_event_details(self):
        details = ""
        details += f"Event Name: {self.event_name}\n"
        details += f"Date: {self.event_date}\n"
        details += f"Time: {self.event_time}\n"
        details += f"Venue name: {self.venue.venue_name}\n"
        details += f"Total Seats: {self.total_seats}\n"
        details += f"Available Seats: {self.available_seats}\n"
        details += f"Ticket Price: {self.ticket_price}\n"
        details += f"Event Type: {self.event_type.value}\n"
        return details

class Movie(Event):
    def __init__(self, event_name=None, event_date=None, event_time=None, venue=None,
                 total_seats=None, ticket_price=None, event_type=None,
                 genre=None, actor_name=None, actress_name=None):
        super().__init__(event_name, event_date, event_time, venue, total_seats,
                         ticket_price, event_type)
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        print(super().display_event_details())
        print("Genre:", self.genre)
        print("Actor Name:", self.actor_name)
        print("Actress Name:", self.actress_name)

    
    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    
    def get_actor_name(self):
        return self.actor_name

    def set_actor_name(self, actor_name):
        self.actor_name = actor_name

    
    def get_actress_name(self):
        return self.actress_name

    def set_actress_name(self, actress_name):
        self.actress_name = actress_name



class Concert(Event):
    def __init__(self, event_name=None, event_date=None, event_time=None, venue=None,
                 total_seats=None, ticket_price=None, event_type=None,
                 artist=None, concert_type=None):
        super().__init__(event_name, event_date, event_time, venue, total_seats,
                         ticket_price, event_type)
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        print(super().display_event_details())
        print("Artist:", self.artist)
        print("Concert Type:", self.concert_type)

    
    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    
    def get_concert_type(self):
        return self.concert_type

    def set_concert_type(self, concert_type):
        self.concert_type = concert_type



class Sports(Event):
    def __init__(self, event_name=None, event_date=None, event_time=None, venue=None,
                 total_seats=None,ticket_price=None, event_type=None,
                 sport_name=None, teams_name=None):
        super().__init__(event_name, event_date, event_time, venue, total_seats,
                         ticket_price, event_type)
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        print(super().display_event_details())
        print("Sport Name:", self.sport_name)
        print("Teams Name:", self.teams_name)

    
    def get_sport_name(self):
        return self.sport_name

    def set_sport_name(self, sport_name):
        self.sport_name = sport_name

    
    def get_teams_name(self):
        return self.teams_name

    def set_teams_name(self, teams_name):
        self.teams_name = teams_name


