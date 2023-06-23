import random 
from typing import List

from supports import TicketSupport

def fifo_ordering(list: List[TicketSupport]) -> List[TicketSupport]:
    return list.copy()

def filo_ordering(list: List[TicketSupport]) -> List[TicketSupport]:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy
    
def random_ordering(list: List[TicketSupport]) -> List[TicketSupport]:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy

