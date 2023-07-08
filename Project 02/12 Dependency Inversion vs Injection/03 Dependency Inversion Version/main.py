import string
import random
from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_lowercase, k=6))
        self.status = "open"

    def set_status(self, status):
        self.status = status


class Authorizer(ABC):
    """
    Use Dependency Inversion:
    It means that introduce an exra layer between ojbect and it's parent from an abstract class.
    So they are less directly dependent on each other. You can replace the object with the subtype
    of another object. 
    (Add new Authorizer class)
    """
    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class Authorizer_SMS(Authorizer):

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

class Authorizer_Robot(Authorizer):

    def __init__(self):
        self.authorized = False

    def authorize(self):
        robot = ""
        while robot != "y" and robot != "n":
            robot = input("Are you a robot (y/n) ? ").lower()
        self.authorized = robot == "n"
        
    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor:

    def __init__(self, authorizer: Authorizer):  # Dependency inversion apply here
        self.authorizer = authorizer
    
    def pay(self, order):
        self.authorizer.authorize()
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print(f"Processing payment for order with id {order.id}")
        order.set_status("paid")


def main() -> None:
    order = Order()
    # auth = Authorizer_SMS()
    # auth.generate_sms_code()
    auth = Authorizer_Robot()
    payment_processor = PaymentProcessor(auth)
    payment_processor.pay(order)


if __name__ == "__main__":
    main()
