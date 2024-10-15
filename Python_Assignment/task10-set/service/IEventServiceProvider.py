from abc import ABC, abstractmethod
import sys
sys.path.append('C:/Users/deebi/OneDrive/Desktop/TicketBookingSystem/task10-set/bean')
from Venue import Venue 
class IEventServiceProvider(ABC):
    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                     event_type: str, venue: Venue):
        pass

    @abstractmethod
    def getEventDetails(self):
        pass

    @abstractmethod
    def getAvailableNoOfTickets(self):
        pass