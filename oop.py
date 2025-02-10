# object oriented programming
class Cars:
    # constructor method
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    # a method function
    def describe_car(self):
        print(f'My dream car make is {self.make}',
              f'My dream car model is {self.model}', f'Manufacture is {self.year}')

# create object or instances of class

myobj =Cars("BMW","BMW",2025)
myobj.describe_car()
myobj2 = Cars("Land rover","Land rover",2025)
myobj2.describe_car()
myobj3 = Cars("Lexus","Lexus",2025)
myobj3.describe_car()
myobj4 = Cars("Range Rover","range Rover",2025)
myobj4.describe_car()
myobj5 = Cars("Toyota","Sunset",2025)
myobj5.describe_car()