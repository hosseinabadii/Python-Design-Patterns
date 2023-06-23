from typing import Optional
from dataclasses import dataclass
from abc import ABC, abstractclassmethod


class Commission(ABC):
    """Represents a generic commission"""

    @abstractclassmethod
    def get_payment(self) -> float:
        """Computes the commission to be paid out."""


@dataclass
class ContractCommission(Commission):
    """Represents a contract commission"""

    commission: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        return self.commission * self.contracts_landed
    

class Contract(ABC):
    """Represents a contract and payment process for a particular employee"""

    @abstractclassmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract"""


@dataclass
class HourlyContract(Contract):
    """Contract type for an employee that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost

    
@dataclass
class SalariedContract(Contract):
    """Contract type for an employee that's paid based on fixed monthly salary."""

    monthly_salary: float = 0
    percentage: float = 1.0

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class FreelancerContract(Contract):
    """Contract type for a freelancer that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number:str = ""   

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked


@dataclass
class Employee:
    """Employee"""

    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission:
            payout += self.commission.get_payment()
        return payout
    

def main() -> None:

    print("="*50)
    henry_contract = HourlyContract(pay_rate=50.0, hours_worked=100)
    henry = Employee(name="Henry", id=123456, contract=henry_contract)
    print(f"{henry.name} worked {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}.")
    print("="*50)
    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(name="Sarah", id=547896, contract=sarah_contract, commission=sarah_commission)
    print(f"{sarah.name} landed {sarah.commission.contracts_landed} contracts and earned ${sarah.compute_pay()}.")
    print("="*50)

if __name__ == "__main__":
    main()
