from support.app import CustomerSupport, FIFOOrderingStrategy, FILOOrderingStrategy, RandomOrderingStrategy
from support.ticket import SupportTicket


def main():
    # create the application
    app = CustomerSupport()

    # create a few tickets
    app.add_ticket(SupportTicket("John Smith", "My computer makes strange sounds!"))
    app.add_ticket(
        SupportTicket("Linus Sebastian", "I can't upload any videos, please help.")
    )
    app.add_ticket(
        SupportTicket("Arjan Codes", "VSCode doesn't automatically solve my bugs.")
    )

    # process the tickets
    app.process_tickets(FIFOOrderingStrategy())


if __name__ == "__main__":
    main()
