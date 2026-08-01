"""
3. Inheritance
Problem: Create an ElectricCar class that inherits from
the Car class and has an additional attribute battery_size.

"""

class Car:
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model

    def fullname(self):
        return f"{self.brand}{self.model}"    #additional function


class ElectricCar(Car):                              #inheritance
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)         # super refer to car initi
        self.battery_size = battery_size


my_Tesla = ElectricCar("Tesla X ","Model S","40khw")
print(my_Tesla.fullname())

# my_car = Car("Tata","Punch")
# print(my_car.brand)
# print(my_car.model)        
        