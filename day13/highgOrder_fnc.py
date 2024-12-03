# Higher Order Functions

# Function as a Parameter
# def sumNumbers(nums):
#     return sum(nums)

#function as prameter

# def high_order_function(f, lst):
#     summation = f(lst)
#     return summation
# result = high_order_function(sumNumbers, [1,2,3,4,5])
# print(result)


# Function as a Return Value

# def square(x):          
#     return x ** 2

# def cube(x):            
#     return x ** 3

# def absolute(x):        
#     if x >= 0:
#         return x
#     else:
#       return -(x)


# def higher_order_function(type): 
#     if type == 'square':
#         return square
#     elif type == 'cube':
#         return cube
#     elif type == 'absolute':
#         return absolute
    
# result = higher_order_function('square')
# print(result(3))       
# result = higher_order_function('cube')
# print(result(3))     
# result = higher_order_function('absolute')
# print(result(-3))   



# Python Closures

# def addTen():
#     ten = 10
#     def add(num):
#         return num + ten
#     return add

# closure_result = addTen()
# print(closure_result(5))  
# print(closure_result(10))
     
# Python Decorators

# Normal function
# def greeting():
#     return 'Welcome to Python'
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# g = uppercase_decorator(greeting)
# print(g())   



'''This decorator function is a higher order function
that takes a function as a parameter'''
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# @uppercase_decorator
# def greeting():
#     return 'Welcome to Python'
# print(greeting())   



# Applying Multiple Decorators to a Single Function


'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# # Second decorator
# def split_string_decorator(function):
#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string

#     return wrapper

# @split_string_decorator
# @uppercase_decorator   
# def greeting():
#     return 'Welcome to Python'
# print(greeting())  


# Accepting Parameters in Decorator Functions

# def decorator_with_parameters(function):
#     def wrapper_accepting_parameters(para1, para2, para3):
#         function(para1, para2, para3)
#         print("I live in {}".format(para3))
#     return wrapper_accepting_parameters

# @decorator_with_parameters
# def print_full_name(first_name, last_name, country):
#     print("I am {} {}. I love to studying.".format(
#         first_name, last_name, country))

# print_full_name("Ashuu", "Mohaz",'somalia')



# Built-in Higher Order Functions



# numbers = [1, 2, 3, 4, 5] 
# def square(x):
#     return x ** 2
# numbers_squared = map(square, numbers)
# print(list(numbers_squared))   
# numbers_squared = map(lambda x : x ** 2, numbers)
# print(list(numbers_squared))   


# numbers_str = ['1', '2', '3', '4', '5'] 
# numbers_int = map(int, numbers_str)
# print(list(numbers_int))   



# names = ['Ashuu', 'Miki', 'Moha', 'Jacar'] 

# def change_to_upper(name):
#     return name.upper()

# names_upper_cased = map(change_to_upper, names)
# print(list(names_upper_cased))  

# # Let us apply it with a lambda function
# names_upper_cased = map(lambda name: name.upper(), names)
# print(list(names_upper_cased))   



#Python - Filter Function

# Lets filter only even nubers
# numbers = [1, 2, 3, 4, 5] 

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))      



# numbers = [1, 2, 3, 4, 5]  

# def is_odd(num):
#     if num % 2 != 0:
#         return True
#     return False

# odd_numbers = filter(is_odd, numbers)
# print(list(odd_numbers))      



# # Filter long name
# names = ['Ashuu', 'Miki', 'Moh', 'Jacar']  
# def is_name_long(name):
#     if len(name) > 7:
#         return True
#     return False

# long_names = filter(is_name_long, names)
# print(list(long_names))   



#Python - Reduce Function
from functools import reduce
      
numbers_str = ['1', '2', '3', '4', '5']  
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)       