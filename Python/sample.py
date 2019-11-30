# n = (' Hello Python Full Stack '.split())
# print(n)

# x = (" Hello,Python! ".split())
# print(x)

#Numbers

# print(10 + 15 * 10 + 25)
# print((10 + 15) * (10 + 25))

# a = 5
# print(a)
# a = a * 10
# print(a * 5)

# my_income = 100    #when two strings are separted by underscore(_) called snakecasing
# tax_rate = 10.0

# my_taxes = my_income * tax_rate
# print(my_taxes)

#Strings

# "hello" 'hello' "i'm a sai"

# my_string = "Saikumar"
# print(my_string)
# print(my_string[-1])
# print(my_string[0])   #String indexing

# print(my_string[::-1])
# print(my_string[3:])
# print(my_string[:3])
# print(my_string[::2])
# print(my_string[::4])
# print(my_string[2:5])    #String sciling

# x = my_string.upper()
# print(x)
# x = my_string.lower()
# print(x)
# x = my_string.capitalize()
# print(x)         #String methods

# x = " Insert another string:{} ".format("Sai")
# print(x)
# x = " First_String: {} " " Second_String: {} ".format("Cat", "Dog")
# print(x)
# x = " First_String: {y} "" Second_String: {x} ".format(x = "Dog", y = "Cat")
# print(x)         #String formatting

#Lists

# mylist = [1, 2, 3, 4, 5]
# mylist = ['Saikumar', 5, 6, 10, 54.5, 55.0, 56.0, 'a', 'b', 'c',['x', 'y', 'z']]
# mylist = ['s', 'a', 'i', [1, 5, 4]]

# print(mylist[:3])
# print(mylist[3:])
# print(mylist[::-1])
# print(mylist[::2])    #List slicing

# print(mylist[0])
# print(mylist[-1])     #List indexing

# mylist.append("New item")
# print(mylist)
# mylist.pop()             #Delete the element from the list
# print(mylist)
# mylist[0] = "new item"   #Add the new item to list
# print(mylist)

# x = mylist[3][2]       #Nested list
# print(x)
# print(len(mylist))     #Length of list

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# first_column = [row[0] for row in matrix]
# print(first_column)     #List comprehension

# mylist = [15, 54, 60, 2, 4, 5, 10]
# mylist.sort()       #Sorting of list
# print(mylist)
# mylist.reverse()    #Reverse of list
# print(mylist)

# x = ['S', 'a', 'i']
# mylist.extend(x)  #Extend keyword
# print(mylist)
# mylist.append(x)  #Append keyword
# print(mylist)

#Dictionaries

# my_dict = {'key1' : 'value1', 'key2' : 'value2', 'key3' : {'154':['a', 1, 2, 'Saikumar']}}  #List_comprehension
# print(my_dict['key3']['154'][3].upper())    #Nested dictionaries

# my_dict = {'Breakfast': 'Idly', 'lauch': 'Rice', 'dinner': 'tiffin'}
# my_dict['lauch'] = 'chapathi'
# my_dict['Breakfast'] = 'masala dosa'
# print(my_dict['lauch'])
# print(my_dict)

#Tuples

# t = (5, 10, 15, 20)
# print(t[1])
# print(t[3])
# t = [5, 10, 15, 20]
# t[0] = 'New item'
# print(t)


#Boolean

True
False
0
1

#sets

# x = set()
# x.add(5)
# x.add(10)
# x.add(15)
# x.add(0.5)
# print(x)
#
# n = set([5, 5, 5, 10, 10, 10, 15, 15, 15, 0.5, 0.5, 0.5])
# print(n)

#Control flow

#<=, >=, ==, !=    #Comparision operator
#and, or, not      #Logical operator

# if 1 == '1':
#     print("True")
# elif 1 != 1:
#     print("yes!")
# else:
#     print("False")    #If, elif & else Statement

# i = 5
# while i < 10:
#     print(i)
#     i = i + 1

# if 1 != '1':
#     print("True")
# else:
#     print("False")

# if 1 > 5:
#     print("Hello!")
#     if 5 > 2:
#         print("True")
# else:
#     print("False") #If else statement

# seq = [1, 5, 10, 15, 20]
# for item in seq:
#     print(item)

# x = [5, 10, 15, 20, 25]
# out = []
# for i in x:
#     out.append(i**2)
# print(out)

# mylist = [(1, 5), (5, 10), (10, 15)]
# for tup1,tup2 in mylist:
#     print(tup1)
#     print(tup2)   #Tuples in for loop

# d = {"Sai":1,"kumar":2}
# for k in d:
#     print(k)
#     print(d[k])  #Dictionaries in for loop

# i = 5
# while i < 10:
#     print("i is:{}".format(i))
#     i += 1     #list formatting

# for i in list(range(0,21,5)):
#     print(i)   #List in for loop

# x = [5, 10, 15, 20]
# out = [i**2 for i in x]
# print(out)         #List comprehension

#Function

# def addnum(num1, num2):
#     print(num1 + num2)
# addnum(5, 10)

# def add(num1, num2):
#     if type(num1) == type(num2) ==type('10'):
#         return num1 + num2
#     else:
#         print("I want integers!")
# result = add( '10', '15' )
# print(result)

# def fun(Sai = 'Love'):
#     """
#     This is my function
#     Sai
#     LOve
#     """
#     print("This is python function:{}".format(Sai))
# fun()

# def hello():
#     return 'hello'
# result ='Hello'
# print(result)

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def even(num):
#     return num % 2 == 0
# result = filter(even, mylist)
# print(list(result))

# result = filter(lambda num:num % 2 == 0, mylist)
# print(list(result))    #Lambda function

# st = 'hello'
# print(st.upper())
# print(st.lower())
# print(st.capitalize())

# t = ("go to hotel! #sports")
# result = t.split('#')[1]
# print(result)

# print('x'in [1, 2, 3, 'x'])

#Scope of python

# x = 50
# def fun():
#     x = 100
#     return x
# print(x)
# print(fun())
# fun()
# print(x)

# lambda x:x%2 == 0     #Here x is a local variable

# name = " This is global name :"

# def fun():
#     name = " Saikumar "
#     def hello():
#         print(" Hello, ", name)
#     hello()
# fun()
# print(name)

# x = 100
# def func(x):
#     print(" x is :", x)
#     x = 1000
#     print(" Local x is changed: ", x)
# func(x)

# x = 100
# def fun():
#     global x
#     x = 1000
#     return x
# print(" Before function call: ", x)
# fun()
# print(" After function call ", x)

#Object oriented concepts

# mylist = [5, 10, 15, 20]
# mylist.append(25)
# print(mylist)

# mystring =" iam Saikumar"
# count = 0
# for i in mystring:
#     if i == 'a':
#         count += 1
# print(" Count of a in mystring is :", str(count))

# print(type([5, 10, 15, 20]))
# print(type(()))
# print(type([]))
# print(type(50))
# print((type(100.5)))

# class sample():
#     pass
# x = sample()
# print(x)

# class dog():
#     spieces = " Mammals"
      # breed = " Rice"
      # name = " Sammy "
#     def __init__(self, breed, name):   #Attritubes are charactertics of object
#         self.breed = breed
#         self.name = name

# mydog = dog(" Rice "," Sammy ")
# print(mydog.breed)
# print(mydog.name)
# print(mydog.spieces)

# class circle():
#     pi = 3.15
#     def __init__(self, radius = 1):
#         self.radius = radius

#     def area(self):
#         return self.radius * self.radius * circle.pi   #Objects are function or operation that performs the body of class

#     def set_radius(self, new_rad):
#         self.radius = new_rad
# c = circle(5)
# c.set_radius(100)
# print(c.area())

# class Animal():
#     def __init__(self):
#         print(" Animal created :")

#     def type(self):
#         print(" Animal ")

#     def eat(self):
#         print(" Eatting ")      #Base or old class

# class dog(Animal):
#     def __init__(self):
#         print(" dog created: ")
#     def bark(self):
#         print(" Wool ")
#     def eat(self):
#         print(" Dog Eatting ")      #Derived or new class
# d = dog()
# d.type()
# d.eat()
# d.bark()    #Inheristance

# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return ("title:{}, author:{}, pages:{} ".format(self.title,self.author,self.pages))

#     def __len__(self):
#         return self.pages
#     def __del__(self):
#         print(" Book have been destroyed! ")                  #Special methods rfers to string,length & delete representation

# b = Book("Python", "Guido van roosum", 1000)
# print(len(b))
# print(b)
# del b

# mylist =[1, 5, 10, 15]
# print(mylist)

# try:        #Block of code involves error reflected by try block
#     f = open(' input.txt ',' W ')
#     f.write(" Test written as simple: ")
# except IOError:               #Block of code used to catch error in input as well as output
#     print(" ERROR:File not found to read data ")
# else:
#     print(" Sucess! ")
#     f.close()
#     print(" Hello,World! ")
# finally:                   #This block always works even if error occurs
#     print(" I always be myself ")

# def func_in_module():
#     print(" Iam inside the module file ")
# import mymodule
# mymodule.func_in_module()

# from mymodule import func_in_module()
# func_in_module()

# import mymodule as mm
# mm.func_in_module()
# from mymodele import *
# func_in_module()                      #Modules and packages

# def func():
#     print(" Function ")
#     print(" Top level function ")
# if __name__ == "__main__":
#     print(" Run directly")
# else:
#     print(" Imported ")

# import functools
# print(" Top level function ")
# func()
# if __name__ =="__main__":
#     print(" Run directly ")
# else:
#     print(" Imported ")           #Name and main are biuld in variable

# s = "global variable"

# def fun():
#     s = 100
#     print(s)

# fun()
# print(s)

# def fun():
#     local = 10
#     print(locals())
#     print(globals()['s'])
# fun()

# def hello(name = " Sai! "):
#     return "Hello, ",name
# print(hello())

# new =hello()
# print(new)

# def hello(name = " Sai "):
#     print(" Function run ")
# def greet():
#     return " String inside the greet "
# def welcome():
#     return " String inside the welcome "
#     print(greet())
#     print(welcome())
#     print(" End of hello()")
#     if name == " Sai ":
#         return greet()
#     else:
#         return welcome()
# x = hello()
# print(x())
# # welcome()

# def hello():
#     return " Hi Sai! "
# def other(func):
#     print(" Hello ")
#     print(func)
# other(hello())

# def new_decorator(self):
#
#     def wrap_func():
#         print(" Code is to be executed ")
#         # func()
#         print(" Function call ")
#     return wrap_func()      #Decorator is powerful tool in python where function modifies the functionalities of other function

# @new_decorator
# def func_need_decorator():
#     print("Function need a decorator ")
#     func_need_decorator = new_decorator(func_need_decorator)
#     func_need_decorator()

#Regular Expression

# import re
# pattern = ['term1', 'term2']
# text = " This is string having term1 than other "
# for pattern in pattern:
#     print(" Iam searching for: "+pattern)
#     if re.search(pattern, text):
#         print(" Match ")
#     else:
#         print(" Not Match ")

# import re
# split_term = '@'
# email = 'user@gmail.net'
# print(re.split(split_term,email))

# import re
# def multi_re_find(pattern, phrase):
#     for pattern in pattern:
#         print(" Searching for pattern:{} ".format(pattern))
#         print(re.findall(pattern, phrase))
#         print(" \n ")

#     test_phrase = " sa , sasa, saasaa, saaasaaa, saaaasaaaa, 1234"

#     test_pattern = [' sa+ ']
#     test_pattern = [' sa* ']
#     test_pattern = [' sa?']
#     test_pattern = [' {1, 3} ']
#     test_pattern = [' {3} ']
#     test_pattern = [r' \d+ ']
#     test_pattern = [r' \D+']
#     test_pattern = [r' \s+ ']
#     test_pattern = [r' \S+ ']
#     test_pattern = [r' \w+ ']
#     test_pattern = [r' \W+ ']
# multi_re_search(test_pattern, test_phrase)
# multi_re_find('pattern','phrase')

