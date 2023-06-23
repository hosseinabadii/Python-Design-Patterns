from supports import CustomerSupport
from strategy import fifo_ordering, filo_ordering, random_ordering

def main(strategy):
    # create the application
    app = CustomerSupport()

    # register a few tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
    app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")
    app.create_ticket("Khosro HosseinAbadi", "My strategy pattern not working.")

    # process the tickets
    app.process_tickets(strategy)


if __name__ == "__main__":
    strategy = fifo_ordering
    main(strategy)
