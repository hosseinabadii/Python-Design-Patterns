import random
import string
from typing import List

def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer: str, issue: str):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: str = "fifo"):
        # If it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickects to process. Well done.")
            return
        
        # "fifo" stands for: first in, first out
        if processing_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)

        # "filo" stands for: first in, last out
        elif processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)

        # "random": randomly processing
        elif processing_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("=" * 50)
        print(f"{'Processing ticket id':20} : {ticket.id}")
        print(f"{'Customer':20} : {ticket.customer}")
        print(f"{'Issue':20} : {ticket.issue}")
        print("=" * 50)


# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")
app.create_ticket("Khosro HosseinAbadi", "My strategy pattern not working.")

# process the tickets
app.process_tickets("random")
