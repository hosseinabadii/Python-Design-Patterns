"""
Very advanced Employee management system.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import List
import os
os.system("clear")

FIXED_VACATION_DAYS_PAYOUT = 5  # The fixed nr of vacation days that can be paid out.

class Role(Enum):

    PRESIDENT = auto()
    MANAGER = auto()
    INTERN = auto()
    LEAD = auto()
    WORKER = auto()


class NotEnoughVacations(Exception):

    def __init__(self, requested_days: int, remaining_days: int, message: str) -> None:
        message += f"\nrequested days={requested_days} and remaining_days={remaining_days}"
        super().__init__(message)


@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company."""

    name: str
    role: str
    vacation_days: int = 25

    @abstractmethod
    def pay(self) -> None:
        """Calculate the pay for employee"""

    def take_a_holiday(self) -> None:
        """Let the employee take a single holiday"""
        if self.vacation_days < 1:
            raise NotEnoughVacations(
                requested_days=1,
                remaining_days=self.vacation_days,
                message="You don't have any holidays left. Now back to work, you!",
            )
        self.vacation_days -= 1
        print(f"Have fun on your holiday. Holidays left: {self.vacation_days}")
    
    def payout_a_holiday(self) -> None:
        """Let the employee  pay out 5 holidays."""
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise NotEnoughVacations(
                requested_days=FIXED_VACATION_DAYS_PAYOUT,
                remaining_days=self.vacation_days,
                message="You don't have enough holidays left over for a payout.",
                )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate: float = 50
    hours_worked: int = 10

    def pay(self):
        print(
            f"Paying employee {self.name} a hourly rate of" +
            f" ${self.hourly_rate} for {self.hours_worked} hours."
        )


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 5000

    def pay(self) -> None:
        """Pay an employee."""
        print(
            f"Paying employee {self.name} a monthly salary of ${self.monthly_salary}."
        )


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employee(self, role: Role):
        """find employee based on role"""
        return [employee for employee in self.employees if employee.role == role]


def main() -> None:
    """Main function."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role=Role.MANAGER))
    company.add_employee(HourlyEmployee(name="Brenda", role=Role.PRESIDENT))
    company.add_employee(HourlyEmployee(name="Tim", role=Role.INTERN, vacation_days=8))

    print(company.find_employee(Role.PRESIDENT))
    print(company.find_employee(Role.MANAGER))
    print(company.find_employee(Role.INTERN))

    company.employees[0].pay()
    company.employees[1].pay()

    company.employees[2].payout_a_holiday()
    company.employees[2].take_a_holiday()


if __name__ == "__main__":
    main()
