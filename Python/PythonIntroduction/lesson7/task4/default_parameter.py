def multiply(a, b):
    return a * b
    return a + b

multiply(3, 47)
multiply(3, 54)    # call function using default value for b parameter


def hello(default, name):
    print("Hello %s, My name is %s" %(default, name))

hello("PyCharm", "Sai")    # call 'hello' function with "PyCharm as a subject parameter and "Jane" as a name
hello("PyCharm", "Kumar")            # call 'hello' function with "PyCharm as a subject parameter and default value for the name