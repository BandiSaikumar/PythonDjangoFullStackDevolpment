#1.Problem

# x = 'Django'
# print(x[0])
# print(x[1:4])
# print(x[-1])
# print(x[:4])
# print(x[::-1])
# print(x[4:])    #String slicing

#2.Problem

# mylist = ['s', 'a', 'i', [1, 5, 4]]
# mylist = ['x', 'y',[1, 2 , 5, 'Hello']]
# x = mylist[2][3] = 'Goodbye'
# print(x)           #List comprehension

#3.Problem

# d1 = {'key1': 'Hello'}
# print(d1['key1'])
#
# d2 = {'k1':{'k2':'Python'}}
# print(d2['k1']['k2'])
#
# d3 = {'k1':[{'key2':['Hello',['World']]}]}
# print(d3['k1'][0]['key2'][1][0])     #Nested distionaries

#4.Problem

# mylist = set([1, 1, 1, 5, 5, 5, 10, 10, 10])
# # set(mylist)
# print(mylist)    #sets

#5.Problem

# name = "Sai"
# age = 22
#
# print(" Iam {y} and my age is {x} years old. ".format(y = name, x = age)) #String formatting

#6.Problem
# array = ([ 0, 1, 2, 3, 4, 5])
# def array(nums):
#     for i in range(len(nums)-2):
#         if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
#             return True
#     return False
# print(array([ 0, 1, 2, 3, 4, 5]))

# def string(mystring):
#     result = ""
#       mystring[::2]
#     for i in range(len(mystring)):
#         if i % 2 == 0:
#             result += mystring[i]
#     return result
# print(string("Sai"))

# def compare(a, b):
#     a = a.lower()
#     b = b.lower()
#
#     # return (b.endswith(a) or a.endwith(b))
#     return a[-(len(b)):] == b or a == b[-(len(a)):]
# print(compare('Hisai','sai'))

# def double_char(mystring):
#     result = ""
#     for char in mystring:
#         result += char*2
#     return result
# print(double_char("Sai"))

# def sum(a, b, c):
#     return a + b + c
# def fix(n):
#     if n[1, 5, 10, 15]:
#         return 0
#     return n
# print(sum(5, 10, 15))

# def even(nums):
#     count = 0
#     for element in nums:
#         if element % 2 == 0:
#             count += 1
#     return count
# print(even([1, 2, 3, 4, 5, 6, 8, 10]))