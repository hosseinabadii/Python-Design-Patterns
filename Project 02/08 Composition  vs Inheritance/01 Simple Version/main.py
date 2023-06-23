from dataclasses import dataclass

@dataclass
class HourlyEmployee:
    """Employee that's paid based on number of worked hours."""

    name: str
    id: int
    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked
            + self.commission * self.contracts_landed
            + self.employer_cost
        )
    
    def __str__(self):
        return f"{self.name} worked for {self.hours_worked} hours and earned ${self.compute_pay()}."
    

@dataclass
class SalariedEmployee:
    """Employee that's paid based on fixed monthly salary."""

    name: str
    id: int
    commission: float = 100
    contracts_landed: float= 0
    monthly_salary: float = 0
    percentage: float = 1.0

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.monthly_salary * self.percentage
            + self.commission * self.contracts_landed
        )
    
    def __str__(self):
        return f"{self.name} landed {self.contracts_landed} contracts and earned ${self.compute_pay()}."
    

@dataclass
class Freelancer:
    """Freelancer that's paid based on number of worked hours."""

    name: str
    id: int
    commission: float = 100
    contracts_landed: float= 0
    pay_rate: float = 0
    hours_worked: int = 0
    vat_number:str = ""   

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked
            + self.commission * self.contracts_landed
        )
    
    def __str__(self):
        return f"{self.name} worked for {self.hours_worked} hours and earned ${self.compute_pay()}."
    

def main() -> None:

    print("="*50)
    henry = HourlyEmployee(name="Henry", id=123456, pay_rate=50.0, hours_worked=100)
    print(henry)
    print("="*50)
    sarah = SalariedEmployee(name="Sarah", id=547896, monthly_salary=5000, contracts_landed=10)
    print(sarah)
    print("="*50)


if __name__ == "__main__":
    main()