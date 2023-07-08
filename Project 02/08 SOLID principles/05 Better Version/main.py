from order import Order
from authorizers import SMSAuth, EmailAuth
from processors import (
    DebitPaymentProcessor,
    CreditPaymentProcessor,
    PaypalPaymentProcessor,
)
## SOLID principles
# S --> Single responsibility
# O --> Open for extension /Closed for modification
# L --> Liskov subtitution:
# I --> Interface Segregation: several specific interfaces better than one general interface
# D --> Dependency inversion

def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 3, 5)

    print("=" * 50)
    print(f"total price = {order.total_price()}")
    print("=" * 50)

    processor = DebitPaymentProcessor(SMSAuth())
    processor.authorizer.verify("4545444")
    processor.pay(order)
    print("=" * 50)
    
    processor = PaypalPaymentProcessor(EmailAuth())
    processor.authorizer.verify("name@name.com")
    processor.pay(order)
    print("=" * 50)

    processor = CreditPaymentProcessor()
    processor.pay(order)
    

if __name__ == "__main__":
    main()
