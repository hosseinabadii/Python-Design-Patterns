## SOLID principles
# S --> Single responsibility
# O --> Open for extension /Closed for modification
# L --> Liskov subtitution:
# I --> Interface Segregation: several specific interfaces better than one general interface
# D --> Dependency inversion.

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
        
class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing 'debit' payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
  
    def pay_credit(self, order, security_code):
        print("Processing 'credit' payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"



order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 3, 5)

print(f"total price = {order.total_price()}")
print("=" * 50)
payment = PaymentProcessor()
payment.pay_debit(order, "025448887")
print("=" * 50)
payment = PaymentProcessor()
payment.pay_credit(order, "025448887")
