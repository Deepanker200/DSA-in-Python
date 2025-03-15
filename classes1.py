# class Student:
    
#     #Default Contstructor
#     def __init__(self):
#         pass
    
#     # Parameterized constructor
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         # print(self)
#         print("Adding new student in DB") 
    
#     def full_name(self):
#         return f"{self.name}{self.marks}"
     

# s1=Student("Deepanker",99)
# print(s1.name,s1.marks)
# print(s1.full_name())

# class Car:
#     color="blue"
#     brand="Mercedes"

# c1=Car()
# print(c1.brand)


## Problem Statement

class Car:
    total_car=0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1
        
    def get_brand(self):
       return self.__brand+" !"
    
    def full_name(self):
        return f"{self.__brand}{self.__model}"
        
    def fuel_type(self):
        return "Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
       return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size 

    def fuel_type(self):
        return "Electric Charge"

my_tesla=ElectricCar("Tesla","Model S","85kWh")
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())


safari=Car("Tata","Safari")
safari2=Car("Tata2","Safari2")
# print(safari.fuel_type())
# print(Car.total_car)       

# static_car=Car("Tata3","Safari3")
# print(static_car.general_description())
# print(Car.general_description())


# safari.model="City"
print(safari.model)
safari.brand="City"
print(safari.brand)

# my_car=Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

print(isinstance(my_tesla,Car))