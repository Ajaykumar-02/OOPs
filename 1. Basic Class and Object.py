"""
1.Basic Class and Object:
Problem: Create a Car class with attributes
like brand and model.
Then create an instance of this class.

"""

class Car:                               # Car is class
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model



my_car = Car("Toyota","Kia")  #my_car is object
print(my_car.brand)      
print(my_car.model)      

my_new_car = Car("Tata","Punch")  #my_new_car is object
print(my_new_car.model)