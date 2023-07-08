from abc import ABC, abstractclassmethod

class Authorizer(ABC):

    @abstractclassmethod
    def is_authorized(self) -> bool:
        return self.authorized


class SMSAuth(Authorizer):

    authorized = False

    def verify(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
    

class EmailAuth(Authorizer):

    authorized = False

    def verify(self, email_address):
        print(f"Verifying email address {email_address}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
