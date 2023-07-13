from datetime import datetime

class Greeting:
    def __init__(self, greeting_intro: str) -> None:
        self.greeting_intro = greeting_intro

    def greet(self, name: str) -> str:
        return f"{self.greeting_intro}, {name}."

    def greet_list(self, names: list[str]) -> list[str]:
        return [self.greet(name) for name in names]

def main() -> None:
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting_intro = "Good morning"
    elif 12 <= current_hour <= 18:
        greeting_intro = "Good afternoon"
    else:
        greeting_intro = "Good evening"
    name = input("Enter your name: ")
    greeting = Greeting(greeting_intro)
    print(greeting.greet(name))

if __name__ == "__main__":
    main()