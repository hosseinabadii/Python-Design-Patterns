import string
import random

class Order:

    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_lowercase, k=6))
        self.status = "open"

    def set_status(self, status):
        self.status = status

class Authorizer_SMS:

    def __init__(self):
        self.authorized = False
        self.code = None

    def generate_sms_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))
        print(f"code: {self.code}")

    def authorize(self):
        code = input("Enter SMS code: ")
        self.authorized = code == self.code

    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor:
    """
    Use Dependency Injection:

    It is a pattern where you split creating the object from using the object.
    You can create the object somewhere else and then pass it as a parameter.
    If you pass the object to the __init__ method, you can use the object everywhere in the class.
    If you just want to use the object in a specific method, you can only pass it to that method.  
    """

    def __init__(self, authorizer: Authorizer_SMS):
        self.authorizer = authorizer
    
    def pay(self, order):
        self.authorizer.authorize()
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print(f"Processing payment for order with id {order.id}")
        order.set_status("paid")


def main() -> None:
    order = Order()
    auth = Authorizer_SMS()   # creating authorizer move to here
    auth.generate_sms_code()  # generating sms code move to here
    payment_processor = PaymentProcessor(auth)
    payment_processor.pay(order)


if __name__ == "__main__":
    main()
