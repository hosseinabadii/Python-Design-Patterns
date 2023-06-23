"""
@dataclass decorator create automatically __init__() and __repr__() dunder methods.
It is useful for data oriented classses.
"""
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Person:

    name: str
    age: int
    address: str
    phone: int = 000000000                                   # default
    active: bool = field(repr=False, default=True)           # default: is not included in __repr__ and __str__
    email_addresses: list[str] = field(default_factory=list) # default: get a function to generate default value
    id: str = field(init=False, default_factory=generate_id) # default: can not be used in initialization
    _search_string: str = field(init=False, repr=False)      # default: is not included in __repr__ and __str__

    def __post_init__(self) -> None:                         # generate this attribute when initialization
        self._search_string = f"{self.name} {self.address}"
    

@dataclass(frozen=True)
class FrozenPerson:
    name: str


def main() -> None:
    person = Person("Khosro", 31, "Iran Mashhad", 9357896541)
    print("=" * 30)
    print(person)
    print("=" * 30)
    frozen_person = FrozenPerson("Ali")
    print(frozen_person)
    print("=" * 30)
    #frozen_person.name = "New Name"    # You can not set attribute of a  @dataclass(frozen=True)


if __name__ == "__main__" :
    main()