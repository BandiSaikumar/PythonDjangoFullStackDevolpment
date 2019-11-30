class Complex:
    def create(self, real_part, imag_part):
        self.real_part = real_part
        self.imag_part = imag_part

if __name__ == "__main__":
    my_object = Complex()
# print(my_object.create)

class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current

if __name__ == "__main__":
    my_object = Calculator()
# print(my_object.add)