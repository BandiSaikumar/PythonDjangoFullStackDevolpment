class square:
    def __init__(self):
        self.sides = 4          # special method __init__

my_object = square()
print(my_object.sides)

class Car:

    def __init__(self):
        self.colour = "red"

  # Note: you should not pass self parameter explicitly, only color parameter

my_object = Car()
print(my_object.colour)