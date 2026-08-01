"""
6. Class Variables:
Problem: Add a class variable to Car
that keeps track of the number of cars created.

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
    



class ElectricCar(Car):                              #inheritance
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)         # super refer to car initi
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"    

# my_Tesla = ElectricCar("Tesla","Model S","40khw")
# print(my_Tesla.fuel_type())

Car("Tata","Safari")
# print(safari.fuel_type())

Car("test","Test")

print(Car.total_car)