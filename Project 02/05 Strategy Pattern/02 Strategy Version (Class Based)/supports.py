import random
import string
from typing import List


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class TicketSupport:

    def __init__(self, customer: str, issue: str):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:

    tickets: List[TicketSupport] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(TicketSupport(customer, issue))

    def process_tickets(self, processing_strategy):

        ticket_list = processing_strategy.create_ordering(self.tickets)
        # If it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickects to process. Well done.")
            return
        
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: TicketSupport):
        print("=" * 50)
        print(f"{'Processing ticket id':20} : {ticket.id}")
        print(f"{'Customer':20} : {ticket.customer}")
        print(f"{'Issue':20} : {ticket.issue}")
        print("=" * 50)
