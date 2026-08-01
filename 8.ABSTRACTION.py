"""
ABSTRACTION:
Abstraction is the process of hiding 
internal implementation details and showing
only essential functionality to the user.

Example:ATM Machine

You can:
Withdraw money
Check balance

You cannot see:
Bank server logic
Validation steps
Network calls
"""
from abc import abstractmethod,ABC

class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        pass

class Car:
    def engine(Vehicle):
        print("How Car Engine Works")

class Bike:
    def engine(Vehicle):
        print("How Bike Engine Works")            

  