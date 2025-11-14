# print("hello world")

# x=5
# y=10
# sum = x+y
# print(sum)
# sum = x-y
# print(sum)
# sum = x*y
# print(sum)
# sum = x/y
# print(sum)

# x=5
# y=10
# print = x+y
# print = x*y

# x = 10.00
# y = 20.00
# print(type(x))
# print(type(y))
# print(bool(x))

# my_var = 10
# print(my_var)

# x,t,z = "20", "30", "50"
# x = "20", "30", "50"
# print(x)

# fruits= ["apple", "banana", "cherry"]
# x, y, z = fruits
# x=y=z=fruits
#print(type(x))

# x = "good"
# def my_function():
#print("python "+x)
#my_function()

# def my_func():
#         global x
#         x="good"
# my_func()
# print("python is "+ x)

# x = 5
# print(type(x))

# x ="elish"
# print(type(x))

# x = "5.5"
# print(type(x))

# x = 5.5
# print(type(x))

# LISTS

# my_list = ["apple", "banana", "cherry"]
# print(type(my_list))
# print(my_list)

# my_list = ["apple", "banana", "cherry"]
# print(my_list[-1])

# my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon",]
# print(my_list[2:5])

# my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon",]
# print(my_list[-4:-1])

# my_list = ["apple", "banana", "cherry"]
# my_list[1] = "blackcurrant"
# print(my_list)

# my_list=['APPLE', 'BANANA', 'CHERRY']
# my_list[2:5]= ["Elish love Amaan"]
# print(my_list)
# my_list.append("Amaan love Elish")
# print(my_list)

# my_list = ["apple", "banana", "cherry"]
# my_list.insert(1, "orange")
# print(my_list)

# list1= ["amaan", "mayank"]
# list2= ["dipanshu", "aamir"]
# list1.extend(list2)
# print(list1)

# my_list = ["apple", "banana", "cherry"]
# print(my_list)
# my_list.append("orange")
# print(my_list)
# my_list.insert(2, "papaya")
# print(my_list)
# my_list.remove("orange")
# print(my_list)
# my_list.pop(2)
# print(my_list)

# my_list = ["apple", "banana", "cherry"]
# print(my_list)
# my_list.append("orange")
# print(my_list)
# my_list.insert(2, "papaya")
# print(my_list)
# my_list.remove("orange")
# print(my_list)
# my_list.pop(2)
# print(my_list)

# my_list.clear()
# print(my_list)

# LIST2= []
# LIST2.append("Amaan")
# LIST2.insert(1, "Elish")
# print(LIST2)

# list1=[]
# list1.append(1)
# print(list1)

# list1[0]= "hello"
# print(list1)

#loops

# list1 = [1, 2, 3, 4, 5]
# for x in list1:
#     print(x)

# list1 = [1, 2, 3, 4, 4, 4, 5]
# for x in list1:
#     print(x)
#     if x==7:
#          break

# text = "hello"
# print(text.upper())

# text = "HELLO"
# print(text.lower())

# text = "hello"
# print(text.strip())

# text = "hello"
# print(text.replace("h", "c"))

# text = "hello"
# print(text.split())

# formatting

# name = "Amaan"
# age = 19
# print(f"My name is {name} and I am {age} years old")

#assignments

# x = 10
# x += 5
# print(x)

# x -= 5
# print(x)

# x *= 5
# print(x)

# x /= 5
# print(x)

# x %= 2
# print(x)

# x //= 2
# print(x)        

# x **= 2
# print(x)

#comparisons

# x = 10
# y = 5   

# print(x > y)   # True
# print(x < y)   # False
# print(x == y)  # False
# print(x != y)  # True
# print(x >= y)  # True
# print(x <= y)  # False

# dictionary
# my_dict = {
#     "name": "Amaan",
#     "age": 19,
#     "city": "delhi"
# }

# print(my_dict)
# print(my_dict["name"])
# print(my_dict["age"])
# print(my_dict["city"])

# my_dict["city"] = "Uttar Pradesh"
# print(my_dict)

# print(my_dict.keys())
# print(my_dict.values())

# itrating through a dictionary
# my_dict = {
#     "name": "Amaan",
#     "age": 19,
#     "city": "delhi"
# }
# for key, value in my_dict.items():  
#     print(f"{key}: {value}")

# if-else
# age = 18 

# if age >= 18:
#      print("you are adult")

# else:
#      print("you are not adult")

#if-elf-else
# age = 18 

# if age >= 18:
#      print("you are adult")
# elif age == 18:
#       print("you are teen")
# else:
#      print("you are not adult")

#Nested if
# x = 15 

# if x >= 10:
#     print("x is greater then 10")
      
#     if x >= 20:
#         print("x is also greater then 20")

#     else:
#         print("x is not greater then 20")

#odd and even
# x = 176

# if x /2:
#     print("x is even number")

# else:
#     print("x is odd number")

# person_age = []

# person_age.append(input("what is your age: "))

# if int(person_age [0]) >= 18:
#     print("you are eligible for driving")

# else:
#     print("you are not eligible for driving")


# word = "python"

# for x in word:
#     print(x)

#     for i in range (1, 10, 2):
#         print(i)

# for i in range(1,4):
#     for j in range(1,3):
#         print(f"i = {i}, j = {j}")

# for i in range(1,50):
#     if i==20:
#         break
#     print(i)

# print all even numbers less then 30 using range()

# for i in range(1,30):
#     if i%2==0:
#         print(i)

# use a nested for loop to print a 3*3 multiplication table
# i = 3
# for i in range(30):
#         if i%3==30:
#             print(i)

# function
# def greet():
#     print("hello, Python!")
# greet()

# functions ith perameters
# def greet(name):
#     print(f"hello, {name}!")
# greet("Amaan")
# greet("Elish")

#Functions with return values

# def add(a, b):
#     return a+b
# result=add(5,8)
# print(result)

# def greet(name="student"):
#     print(f"hello, {name}")
# greet()
# greet("alice")

#  function
# def greet():
#     print("hello!")
# greet()

# # 2nd
# def add(a,b):
#     return(a+b)
# result=add(20,10)
# print(result)

# # write a function that demonstrates local and global variables
# def my_function():
#     local_var = "I am local"
#     print(local_var)

# class Car:
#     def __init__(self, brand, colour): #Constructor
#      self.brand = brand #Attribute
#      self.colour = colour #Attribute
    
#     def drive(self):
#      print(f"{self.colour}{self.brand} is driving ")

# #objects
# car1 =Car("konigseg" , "Black")
# car2 =Car("pagani","White")

# car2.drive()

# import array
# import random
# numbers = array.array('i', [1, 2, 3, 4, 5])
# print(numbers)

# from numpy import random

# x = random.randint(100)
# print(x)

# import pandas as pd

# data = [10, 20, 30, 40]
# series = pd.Series(data)
# print(series)

# print(type(series))
# print(series[2])
# print(series.describe())
# print(series.mean())
# print(series.sum())  

# import pandas as pd

# data = {'Name': ['Amaan', 'Elish', 'Ayan', 'Ishan', 'khulood Appi', 'Ilma Appi'],
# 'Age': [19, 17, 13, 13, 19, 20],
# 'City': ['Delhi', 'Delhi', 'UP', 'UP', 'UP', 'UP']}
# df = pd.DataFrame(data)
# print(df)

from turtle import pd
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
s =pd.Series(arr)
print(s)

data = {"math": 90, "science": 85, "english": 78}
s = pd.Series(data)
print(s)