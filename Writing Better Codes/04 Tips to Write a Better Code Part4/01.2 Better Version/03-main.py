from datetime import datetime
from typing import Callable
from functools import partial

GreetingReader = Callable[[], str]
def greet(name: str, greeting_reader: GreetingReader) -> str:
    return f"{greeting_reader()}, {name}."

def greet_list(names: list[str], greeting_reader: Callable[[], str]) -> list[str]:
    return [greet(name, greeting_reader) for name in names]

def read_greeting() -> str:
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour <= 18:
        return "Good afternoon"
    else:
        return "Good evening"
    
def read_name() -> str:
    return input("Enter your name: ")

def main() -> None:
    greet_fn = partial(greet, greeting_reader=read_greeting)
    print(greet_fn(read_name()))
    # print(greet(read_name(), read_greeting))
    print(greet_list(["Ali", "Reza", "Narges"], read_greeting))

if __name__ == "__main__":
    main()