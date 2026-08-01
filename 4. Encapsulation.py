"""
4.Encapsulation:
Encapsulation is the process
of binding data and methods together and restricting
direct access to data.

#Example:
Capsule medicine — everything packed safely inside
(data + methods)

#Problem: Modify the Car class to encapsulate
the brand attribute, making it private, and
provide a getter method for it.

"""

class Car:
    def __init__(self,brand,model):
        self.__brand = brand 
        self.model = model

    def get_brand(self):
        return self.__brand + "!"   

    def fullname(self):
        return f"{self.__brand}{self.model}"    #additional function



class ElectricCar(Car):                              #inheritance
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)         # super refer to car initi
        self.battery_size = battery_size


my_Tesla = ElectricCar("Tesla X ","Model S","40khw")
# print(my_Tesla.__brand) #hide = __ 
print(my_Tesla.get_brand())