from abc import ABC, abstractclassmethod

## SOLID principles
# S --> Single responsibility
# O --> Open for extension /Closed for modification
# L --> Liskov subtitution:
# I --> Interface Segregation: several specific interfaces better than one general interface
# D --> Dependency inversion

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):

    @abstractclassmethod
    def pay(self, order: Order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing 'debit' payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code
  
    def pay(self, order):
        print("Processing 'credit' payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
  
    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Processing 'paypal' payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 3, 5)

print("=" * 50)
print(f"total price = {order.total_price()}")
print("=" * 50)
payment = DebitPaymentProcessor("0366999")
payment.pay(order)
print("=" * 50)
payment = CreditPaymentProcessor("0568744")
payment.pay(order)
print("=" * 50)
payment = PaypalPaymentProcessor("andd@kdkdkd.com")
payment.pay(order)

