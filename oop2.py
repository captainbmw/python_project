class Fruits:
    def __init__(self, name, colour, price):
        self.name = name
        self.colour = colour
        self.price = price


    def describe_fruit(self):
         print(f"This  {self.name} fruit is {self.colour} at  Ksh{self.price} land on it!")
# instances of a class

my_fruit = Fruits("Apple", "blue", 100)
my_fruit.describe_fruit()
my_fruit = Fruits("Pineapple", "yellow", 200)
my_fruit.describe_fruit()
my_fruit = Fruits("Pear", "red", 300)
my_fruit.describe_fruit()
my_fruit = Fruits("Bananas", "green", 400)
my_fruit.describe_fruit()
my_fruit = Fruits("Mango", "red", 500)
my_fruit.describe_fruit()