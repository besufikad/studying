# """
# Python tutorial
#
# """
# # name = "John"
# # age = "35"
# # rint(name + "is " + age + " years old")
# #
# # a = " Yirga Belay"
# # print(a.lower())
# # print(a.replace("Belay", "Hizkias"))
#
# # from math import *
# # my_num = 5
# # print(str(my_num) + " my favorite number")
# # print(pow(my_num, 2))
# # print(max(4, 6))
# # print(min(2, 3))
# # print(round(8.1))
# # print(floor(3.7))
#
# # name = input("What is your name?")
# # print(name + ":" + " How are you?")
#
# # num1 = input("Enter a number: ")
# # num2 = input("Enter another number: ")
# # result = float(num1) + int(num2)
# # print(result)
# #
# # friends = ["Kevin", "Karen", "Jim"]
# # print(friends)
# # print(friends[0], friends[1], friends[2])
# # print(friends[1])
# # print(friends[2])
#
# # coordinates = (4,5)
# # print(coordinates)
# # print(coordinates[1])
#
# # def say_hi(name, age):
# #     print("Hello " + name + ", you are " + age)
# #
# #
# # say_hi("Yirga", str(35))
#
#
# # def cube(num):
# #     return num * num * num
# #
# #
# # result = cube(4)
# # print(result)
#
#
# # is_male = True
# # is_tall = False
# #
# # if is_male and is_tall:
# #     print("You are male and tall")
# # else:
# #     print("You are either not male or not tall, or not both")
#
#
# # def max_num(num1,num2,num3):
# #     if num1 > num2 and num1 > num3:
# #         print("First number is greater")
# #     elif num2 > num1 and num2 > num3:
# #         print("Second number is greater")
# #     elif num3 > num1 and num3 > num1:
# #         print("Third number is greater")
# #     else:
# #         print("They are equal")
# #
#
# # i = 1
# # while i <= 10:  # condition:
# #     print(i)
# #     i = i + 1
# # print("Done")
#
# # for loop
# # for letter in "Giraffe Academy":
# #     print(letter)
# #
# # for index in range(3, 10):
# #     print(index)
#
#
# # print(2 ** 3)
#
#
# # def raise_to_power(base_num, power_num):
# #     result = 1
# #     for index in range(power_num):
# #         result = result * base_num
# #     return  result
# #
# #
# # print(raise_to_power(2, 3))
# # print(pow(2, 3))
#
#
# # number_grid = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9],
# #     [0]
# # ]
# #
# #
# # for row in number_grid:
# #     for col in row:
# #         print(col)
#
#
# # def translate(phrase):
# #     translation = ""
# #     for letter in phrase:
# #         if letter in "AEIOUaeiou":
# #             translation = translation + "g"
# #         else:
# #             translation = translation + letter
# #     return translation
# #
# #
# # print(translate(input("Enter a Phrase")))
#
#
# # try:
# #     number = int(input("Enter a number: "))
# #     print(number)
# # except:
# #     print("Invalid Input")
#
# #
# # class Student:
# #     def __init__(self, name, major, gpa, is_on_probation):
# #         self.name = name
# #         self.major = major
# #         self.gpa = gpa
# #         self.is_on_probation = is_on_probation
# import img as img
# import numpy as np
#
# #
# # print("I love pizza")
#
# # name = "Yirga"
# # print("Hello " + name)
#
# # age = 21
# # print(age)
# # print(type(age))
# # print("Your age is {}" .format(age))
#
# # height = 20.21
# # print(height)
# # print(type(height))
#
# # name = "Yirga Belay"
# # print(name.lower())
# # print(name.upper())
# # print(len(name))
# # print(name.capitalize())
# # print(name.find("B"))
# # print(name.isdigit())
# # print(name.isprintable())
# # print(name.count("Y"))
#
#
# # name = input("What is your name?")
# # age = int(input("How old are you?"))
# # age += 1
# # print("Your name is {} and {} years old".format(name, age))
#
# # import math
# # pi = 3.14
# # x = 1
# # y = 2
# # z = 3
# # print(max(x,y,z))
# # print(min(x,y,z))
# # print(round(pi))
# # print(math.ceil(pi))
# # print(math.floor(pi))
# # print(abs(pi))
# # print(pow(2,3))
#
# # name = "Yirga belay"
# # first_name = name[0:5:1]
# # print(first_name)
#
#
# # temp = int(input("What is the temperature outside?"))
# # if 0 <= temp <= 30:
# #     print("good day")
# # elif temp < 0 or temp > 30:
# #     print("Bad day")
# # else:
# #     print("God Knows")
#
#
# # name = ""
# # while len(name) == 0:
# #     name = input("Name?")
# #     print("hello" + name)
#
#
# # for i in range(10):
# #     print(i+1)
# #
# #
# # for j in range(50,100+1):
# #     print(j)
#
#
# # import time
# # for seconds in range(10, 0, -1):
# #     print(seconds)
# #     time.sleep(1)
# # print("Happy New Year")
#
#
# # import pandas as pd
# # from matplotlib import pyplot as plt
# # x = [1,2,3]
# # y = [1,4,9]
# # plt.plot(x,y)
# # plt.show()
# #
# # food =["pizza", "spaghetti"]
# # food[0] = "Enjera"
# # food.append("Dabo")
# # food.insert(0,"Doro wat")
# # print(food[:])
# # for x in food:
# #     print(x)
#
#
# # drinks = ["coffe","soda", "tea"]
# # dinner = ["pizza","hamburger", "hotdog"]
# # dessert = ["cake", "ice cream"]
# # food = [drinks,dinner,dessert]
# # print(food)
# # print(food[2][0])
#
# # name = "bro Code"
# # # if(name[0].islower()):
# # #     name = name.capitalize()
# # first_name = name[0:3].upper()
# # last_name = name[4:].upper()
# # print(first_name)
# # print(last_name)
# # print(name)
#
# #
# # def hello(name):
# #     print("Hello! " + name )
# #
# #
# # hello("Yirga")
#
# # def multiply(num1,num2):
# #     result = num1 * num2
# #     return result
# #
# #
# # print(multiply(6, 8))
#
#
# # def hello(first, middle, last):
# #     print("Hello " + first + " " + middle + " " + last)
# #
# #
# # hello("Yirga", "Belay", "Muna")
#
#
# # name = "Bro"  # global scope
# #
# #
# # def display_name(name):
# #     name = "Code"  # local scope
# #     print(name)
# #
# #
# # display_name(name)
# # print(name)
#
#
# # def add(*args):
# #     sum = 0
# #     for i in args:
# #         sum += i
# #     return sum
# #
# #
# # print(add(1, 2, 3))
#
# # import random
# #
# #
# # x = random.randint(1,6)
# # y = random.random()
# #
# # myList = ['rock', 'paper','scissors']
# # z = random.choice(myList)
# # print(z)
#
#
# # import os
# # path = "D:\\Python Coding\\test.txt"
# #
# # if os.path.exists(path):
# #     print("Exists")
# # else:
# #     print("Not Exists")
#
# #
# # with open('test.txt') as file:
# #     print(file.read())
# # print(file.close())
# # text1 = "ypppjoihfoirehgo \nthokffr "
# # with open('test1.txt','w') as file:
# #     file.write(text1)
#
# #
# # import shutil
# # shutil.copyfile('test.txt','copy.txt')
#
# # import os
# # source = "test.txt"
# # destination = ""
#
#
# # import os
# # os.remove('test1.txt')
# #
#
#
# # import messages as msg
# #
# # msg.hello()
# # msg.bye()
# # help("modules")
#
# #
# # # POOP
# # from Car import Car
# #
# # car_1 = Car("Chevy", "Corvette", 2021, "Blue")
# #
# # print(car_1.make)
# # print(car_1.model)
# # car_1.drive()
# #
# # import queue
# # print(queue.Full())
# # help(queue)
#
#
# # def loud(text):
# #     return text.upper()
# #
# #
# # def quiet(text):
# #     return text.lower()
# #
# #
# # def hello(func1,func2):
# #     text = func1("Hello")
# #     text1 = func2("Yirga")
# #     print(text)
# #     print(text1)
# #
# #
# # hello(loud, quiet)
#
# # import datetime
# #
# # dir(datetime)
# # import builtins
# #
# # print(dir(builtins))
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import xlrd
#
# # plt.show()
# # a = np.array([1, 2, 3, 4, 5])
# # b = np.array((10, 12, 13, 14, 15, 16))
# # print(a.ndim)
# # print(b.ndim)
# # print(b.shape)
# # x = np.linspace(0, 10, 1000)
# # y = np.sin(x)
# # plt.plot(x, y, label='sinc')
# # plt.xlabel('Values of x')
# # plt.ylabel('Sin values')
# # plt.title("Trial Plot of Sin function")
# # plt.show(block=True)
# # plt.interactive(False)
# # plt.imshow((x, y))
# # plt.show()
# # plt.imshow(a)
# # Global_irr = pd.read_excel(r'D:\Python Coding\Glob.xlsx')
# # print(Global_irr)
#
#
# # loc = r"D:\Python Coding\Glob.xlsx"
# # wb = xlrd.open_workbook(loc)
# # Excel = wb.sheet_by_index(0)
# # print(Excel.cell_value(0, 0))
#
#
# # base = 6
# # height = 3
# # area = base*height/2
# # print("The area is " + str(area))
#
# # def greeting(hours, minutes, seconds):
# #     print("Total seconds are: " + str(hours / 3600 + minutes / 60 + seconds))
# #
# #
# # greeting(1, 2, 3)
#
#
# # def area_triangle(base, height):
# #     return base * height / 2
# #
# #
# # area_a = area_triangle(5, 4)
# # print(area_a)
#
#
# # def convert_seconds(seconds):
# #     hours = seconds // 3600
# #     minutes = (seconds - hours * 3600) // 60
# #     remaining_seconds = seconds - hours * 3600 - minutes * 60
# #     return hours, minutes, remaining_seconds
# #
# # result = convert_seconds(5000)
# # #hours, minutes, seconds = convert_seconds(5000)
# # print(type(result))
# # print(result)
#
# # values = [23,52,59,37,48]
# # sum = 0
# # length = 0
# # for value in values:
# #     sum += value
# #     length += 1
# #     print("Total sum: " + str(sum) + " - Average: " + str(sum/length))
#
# # for left in range(7):
# #     for right in range(left,7):
# #         print("[" + str(left) + "|" + str(right) + "]", end=" ")
# #     print()
# #
# # for x in [25]:
# #     print(x)
#
# # def factorial(n):
# #     if n < 2:
# #         return 1
# #     return n * factorial(n - 1)
#
#
# # name = "Manny"
# # number = len(name)*3
# # print("Hello {}, your lucky number is {}".format(name,number))
#
#
# # fruits = ["Pineapple","Banana", "Apple", "melon"]
# # fruits.append("Kiwi")
# # fruits.insert(0, "Orange")
# # fruits.pop(1)
# # print(fruits)
#
# # animals = ["lion", "Zebra", "Dolphin", "Monkey"]
# # chars = 0
# # for animal in animals:
# #     chars += len(animal)
# #
# #
# # print("Total characters: {}, Average length: {}".format(chars,chars/len(animals)))
#
#
# # winners = ["Ashley", "Dylan", "Reese"]
# # for index, person in enumerate(winners):
# #     print("{} - {}".format(index+1, person))
#
#
# # def full_emails(peaple):
# #     result = []
# #     for email, name in peaple:
# #         result.append("{} <{}>".format(name, email))
# #     return result
# #
# #
# # print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
#
#
# # multiples = []
# # for x in range(1,11):
# #     multiples.append(x*7)
# # print(multiples)
# #
# # print(10%2)
#
#
# # x ={}
# # print(type(x))
# # file_counts = {"jpg":10, "txt": 14, "csv":2, "py":23}
# # #print(file_counts)
# # file_counts["cfg"] = 8
# # print(file_counts)
# # print(del)
# # for extension in file_counts:
# #     print(extension)
# #
# # for ext, amount in file_counts.items():
# #     print("There are {} files with .{} extension".format(amount,ext))
# # print(file_counts.keys())
# # print(file_counts.values())
# # v_in = 5
# # v_out = 30
# # v_r = 12
# # Pr = 500
# # for v in np.random.randint(2, 35, size=24):
# #     # i = len(v)
# #     if v <= v_in or v >= v_out:
# #         print(0)
# #     elif v_in < v or v <= v_r:
# #         print(Pr * (v ** 3 - v_in ** 3) / (v_r ** 3 - v_in ** 3))
# #     elif v_r < v or v <= v_out:
# #         print(Pr)
# #     else:
# #         print(0)
#
for i in range(50):
    print(i)