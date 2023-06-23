from dataclasses import dataclass
from abc import ABC, abstractclassmethod

@dataclass
class Employee(ABC):
    """Employee"""

    name: str
    id: int

    @abstractclassmethod
    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    """Employee that's paid based on number of worked hours."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return super().compute_pay() + self.commission * self.contracts_landed
    

@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on fixed monthly salary."""

    monthly_salary: float = 0
    percentage: float = 1.0

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return self.monthly_salary * self.percentage

   
@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    """Employee that's paid based on fixed monthly salary."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return super().compute_pay() + self.commission * self.contracts_landed
    

@dataclass
class Freelancer(Employee):
    """Freelancer that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number:str = ""   

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return self.pay_rate * self.hours_worked
    

@dataclass
class FreelancerWithCommission(Freelancer):
    """Freelancer that's paid based on number of worked hours."""
    
    commission: float = 100
    contracts_landed: float = 0  

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return super().compute_pay() + self.commission * self.contracts_landed  

def main() -> None:

    print("="*50)
    henry = HourlyEmployee(name="Henry", id=123456, pay_rate=50.0, hours_worked=100)
    print(f"{henry.name} worked {henry.hours_worked} hours and earned ${henry.compute_pay()}.")
    print("="*50)
    sarah = SalariedEmployeeWithCommission(name="Sarah", id=547896, monthly_salary=5000, contracts_landed=10)
    print(f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}.")
    print("="*50)


if __name__ == "__main__":
    main()