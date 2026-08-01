"""
5. Polymorphism:
Polymorphism means "many forms" — the same method
name behaves differently in different situations.

One interface, multiple behaviors

#Problem: Demonstrate polymorphism by defining
a method fuel_type in both Car and ElectricCar
classes, but with different behaviors.
"""

class Car:
    def __init__(self,brand,model):
        self.__brand = brand 
        self.model = model

    def get_brand(self):
        return self.__brand + "!"   

    def fullname(self):
        return f"{self.__brand}{self.model}"    #additional function

    def fuel_type(self):
        return "Petrol or Diesel"
    



class ElectricCar(Car):                              #inheritance
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)         # super refer to car initi
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"    

my_Tesla = ElectricCar("Tesla","Model S","40khw")
print(my_Tesla.fuel_type())

safari = Car("Tata","Safari")
print(safari.fuel_type())