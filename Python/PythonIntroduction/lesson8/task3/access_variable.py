class car:
    colour = " "

    def description(self):
        description_string = (" This is my new %s car. "%(self.colour))
        return description_string               # we'll explain self parameter later in task 4

car1 = car()
car2 = car()

car1.colour = " red "
car2.colour = " blue "

print(car1.description())
print(car2.description())