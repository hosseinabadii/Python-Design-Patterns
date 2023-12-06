"""
@dataclass decorator create automatically __init__() and __repr__() dunder methods.
It is useful for data oriented classses.
"""
import random
import string
from dataclasses import dataclass, field, FrozenInstanceError


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Person:
    """Define instance attributes, not class attributes."""

    name: str
    age: int
    address: str
    phone: int = 000000000

    # Not included in __repr__ and __str__
    active: bool = field(repr=False, default=True)

    # Get a function to generate default value
    email_addresses: list[str] = field(default_factory=list)

    # Not allowed to be used as an argument when initialization
    id: str = field(init=False, default_factory=generate_id)

    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Excecute after the initialization step."""
        self._search_string = f"{self.name} {self.address}"


@dataclass(frozen=True)
class FrozenPerson:
    """You cannot change the value of attributes after initialization."""

    name: str


@dataclass(kw_only=True)
class KeywordOnlyPerson:
    """You can instantiate an object only with keyword arguments."""

    name: str


def main() -> None:
    person = Person("John", 25, "Canada", 111222333)
    print("=" * 30)
    print(person)
    print("=" * 30)
    frozen_person = FrozenPerson("David")
    print(frozen_person)
    print("=" * 30)
    try:
        frozen_person.name = "New Name"
    except FrozenInstanceError as e:
        print(f"Error---{e}")

    print("=" * 30)
    try:
        keyword_only_person = KeywordOnlyPerson("Ammy")
        print(keyword_only_person)
        print("=" * 30)
    except TypeError as e:
        print(f"Error---{e}")


if __name__ == "__main__":
    main()
