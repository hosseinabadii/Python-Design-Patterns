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
    def pay(self, order: Order, security_code: str):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def pay(self, order, security_code):
        print("Processing 'debit' payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
  
    def pay(self, order, security_code):
        print("Processing 'credit' payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
  
    def pay(self, order, security_code):
        print("Processing 'paypal' payment type")
        print(f"Verifying email address: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 3, 5)

print(f"total price = {order.total_price()}")
print("=" * 50)
payment = DebitPaymentProcessor()
payment.pay(order, "025448887")
print("=" * 50)
payment = CreditPaymentProcessor()
payment.pay(order, "025448887")
print("=" * 50)
payment = PaypalPaymentProcessor()
payment.pay(order, "msjdd@vmsmd.com")
print("=" * 50)