"""
1.Class Method and Self:
Problem: Add a method to the Car class that
displays the full name of the car (brand and model).

"""

class Car:
    def __init__(self,brand,model):
        self.brand =  brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"   

    

car1 = Car("Tata","Punch")
print(car1.model)  
print(car1.brand)
print(car1.fullname())      
        
