#Importing a Module
# import myModule
# print(myModule.generate_fullName('Ashuu', 'Mohaz'))

# from myModule import generate_fullName as fullname, sum_two_nums as total, person as p, gravity as g

# print('Full Name:', fullname('Ashuu', 'Mohaz'))

# print('Sum of two numbers:', total(1, 9))

# mass = 100
# weight = g(mass) 

# print('Weight of an object:', weight)


# p = {
#     'firstname': 'Ashuu',
#     'lastname': 'Mohaz'
# }

# print('Person firstname:', p['firstname'])

#Import Functions from a Module and Renaming
#During importing we can rename the name of the module.


#Import Built-in Modules
# Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re

# OS Module
# import os

# # creating directory
# os.mkdir('mydir')
# #changing the curent directory
# os.chdir('path')
# # getting current working directory
# os.getcwd()
# #removing directory
# os.rmdir()

#Sys Module
# import sys
# print(sys.argv[0], sys.argv[0]) 
# print('welcome {}. enjoy {} challenge!' .format(sys.argv[1])) #IndexError: list index out of range


# # to exit sys
# sys.exit()
# # To know the largest integer variable it takes
# sys.maxsize
# # To know environment path
# sys.path
# # To know the version of python you are using
# sys.version

#Statistics Module

# from statistics import  mean, median, mode, stdev
# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
# print(mean(ages))       
# print(median(ages))     
# print(mode(ages))       
# print(stdev(ages))      


# Math Module

# import math
# print(math.pi)           
# print(math.sqrt(2))     
# print(math.pow(2, 3))   
# print(math.floor(9.81)) 
# print(math.ceil(9.81))   
# print(math.log10(100))   

# from math import pi
# print(pi)


# import math
# from math import pi, sqrt, pow, floor, ceil, log10
# print(pi)                 # 3.141592653589793
# print(sqrt(2))            # 1.4142135623730951
# print(pow(2, 3))          # 8.0
# print(floor(9.81))        # 9
# print(ceil(9.81))         # 10
# print(math.log10(100))    # 2

# from math import pi as  PI
# print(PI) # 3.141592653589793


#String Module

# import string
# print(string.ascii_letters)
# print(string.digits)       
# print(string.punctuation)

# Random Module

# from random import random, randint
# print(random()) 
# print(randint(5, 20))
