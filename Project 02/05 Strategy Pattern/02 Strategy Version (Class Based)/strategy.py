import random
from abc import ABC, abstractclassmethod
from typing import List
from supports import TicketSupport


class TicketOrderingStrategy(ABC):
    @abstractclassmethod
    def create_ordering(self, list: List[TicketSupport]) -> List[TicketSupport]:
        pass


class FIFOStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[TicketSupport]) -> List[TicketSupport]:
        return list.copy()

  
class FILOStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[TicketSupport]) -> List[TicketSupport]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy
    

class RandomStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[TicketSupport]) -> List[TicketSupport]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy
