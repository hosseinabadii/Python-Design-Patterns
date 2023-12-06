import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person:
    def __init__(self, name: str, age: int, address: str, phone: int) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"name:{self.name}, age:{self.age}, address: {self.address}, phone number: {self.phone}"


def main() -> None:
    person = Person("Khosro", 31, "Iran Mashhad", 9357896541)
    print(person)


if __name__ == "__main__":
    main()
