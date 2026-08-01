"""
7. Static Method:
Problem: Add a static method to the
Car class that returns a general description
of a car.
"""

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand 
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"   

    def fullname(self):
        return f"{self.__brand}{self.model}"    #additional function

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def car_description():
        return "Cars are means for Transport"


class ElectricCar(Car):                              #inheritance
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)         # super refer to car initi
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge" 

my_car= Car("TATA","Punch")

print(Car.car_description())


        