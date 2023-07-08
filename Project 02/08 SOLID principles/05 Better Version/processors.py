from abc import ABC, abstractclassmethod
from order import Order
from authorizers import Authorizer

class PaymentProcessor(ABC):

    @abstractclassmethod
    def pay(self, order: Order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing 'debit' payment type")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing 'paypal' payment type")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def pay(self, order):
        print("Processing 'credit' payment type")
        order.status = "paid"
