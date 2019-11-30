class my_class:
    var1 = 5
    var2 = 10

    def fun(self):
        print(" Hello from function: ")        # we'll explain self parameter later in task 4
my_object = my_class()
my_object.fun()

my_object.var2 = 15    # change value stored in variable2 in my_object

print(my_object.var1)
print(my_object.var2)

my_object.fun()   # call method foo() of object my_object

print("value of var1 from my_object")

