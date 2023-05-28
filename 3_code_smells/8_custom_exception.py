"""
Very advanced Employee management system.
"""

"""
Smell 8 (BONUS):
Create custom error exception for your particular case,
in this case we can show what are fixed days in errors.
VacationDaysShortageError()
"""

from dataclasses import dataclass
from typing import List

from enum import Enum, auto
from abc import abstractmethod, ABC

FIXED_VACATION_DAYS_PAYOUT = 5  # The fixed nr of vacation days that can be paid out.


class VacationDaysShortageError(Exception):
    """Custom error that is raised when not enough vacation days are available"""

    def __init__(self, requested_days: int, remaining_days: int, message: str) -> None:
        self.requested_days = requested_days
        self.remaining_days = remaining_days
        self.message = message
        # passing message to Exception parent class for initialization
        super().__init__(message)


class Role(Enum):
    """Employess roles."""

    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()


@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company."""

    name: str
    # now role is isinstance of Role class from Enum
    role: Role
    vacation_days: int = 25

    def take_a_holiday(self) -> None:
        """Let the employee take a single holiday."""
        if self.vacation_days < 1:
            raise VacationDaysShortageError(
                requested_days=1,
                remaining_days=self.vacation_days,
                message="You don't have any holidays left. Now back to work, you!",
            )

        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")

    def payout_holiday(self):
        # pay out 5 holidays
        # check that there are enough vacation days left for a payout
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise VacationDaysShortageError(
                requested_days=FIXED_VACATION_DAYS_PAYOUT,
                remaining_days=self.vacation_days,
                message="You don't have enough holidays left over for a payout.",
            )

        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")

    @abstractmethod
    def pay(self) -> None:
        """Method to call when paying an employee"""


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate_dollar: float = 50
    hours_worked: int = 10

    def pay(self) -> None:
        """Pay an employee."""
        print(f"Paying employee {self.name} a monthly salary of ${self.monthly_salary}.")


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 5000

    def pay(self) -> None:
        """Pay an employee."""
        print(f"Paying employee {self.name} a monthly salary of ${self.monthly_salary}.")


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees(self, role: Role) -> List[Employee]:
        """Find all employees with a particular role."""
        # using list comprehension here
        return [employee for employee in self.employees if employee.role == role]


def main() -> None:
    """Main function."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role=Role.MANAGER))
    company.add_employee(HourlyEmployee(name="Brenda", role=Role.PRESIDENT))
    company.add_employee(HourlyEmployee(name="Tim", role=Role.INTERN))

    print(company.find_employees(role=Role.VICEPRESIDENT))
    print(company.find_employees(role=Role.MANAGER))
    print(company.find_employees(role=Role.INTERN))

    company.employees[0].pay()
    company.employees[0].take_a_holiday()


if __name__ == "__main__":
    main()
