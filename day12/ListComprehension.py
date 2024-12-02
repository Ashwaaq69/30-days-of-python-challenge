#List Comprehension
#List Comprehension is a compact way to create lists in Python.
# syntax
# [i for i in iterable if expression]

#one way

# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = [i * 2 for i in numbers]
# print(doubled_numbers)

# language = 'react'
# lst = list(language)
# # print(type(lst))
# # print(lst)


#another way

# lst = [i for i in language]
# print(type(lst))
# print(lst)

#For instance if you want to generate a list of numbers
# Generating numbers

# numbers = [i for i in range(11)]
# print(numbers)

 # It is possible to do mathematical operations during iteration
 
# squares = [i * i for i in range(11)]
# print(squares)

# It is also possible to make a list of tuples


# numbers = [(i, i*i) for i in range(11)]
# print(numbers)


#List comprehension can be combined with if expression

# Generating even numbers

# even_numbers = [i for i in range(21) if i % 2 == 0]
# print(even_numbers)

# Generating odd numbers

# odd_numbers = [i for i in range(21) if i % 2 != 0]
# print(odd_numbers)


# Filter numbers: let's filter out positive even numbers from the list below

# numbers = [-8, -7, -6, -3, 0, 1,2,3,4,5,6,7,8,10]
# possitive_even_nus = [i for i in range(21) if i % 2 == 0 and i > 0]
# print(possitive_even_nus)


# Flattening a three dimensional array

# list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
# flattened_list = [number for row in list_of_lists for number in row]
# print(flattened_list)


#Lambda Function

#Lambda function is a small anonymous function without a name.
#Creating a Lambda Function

# syntax
# x = lambda param1, param2, param3: param1 + param2 + param2
# print(x(arg1, arg2, arg3))
## Named function
# def add_two_nums(a,b):
#     return a + b
# print(add_two_nums(4,5))


# Lets change the above function to a lambda function
# add_two_nums = lambda a, b: a + b
# print(add_two_nums(2,3))    

# Self invoking lambda function

# (lambda a,b: a+b)(5,5)
# print((lambda a,b: a+b)(5,5))


# square = lambda x : x ** 2
# print(square(3))    # 9
# cube = lambda x : x ** 3
# print(cube(3))    

# # Multiple variables
# multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
# print(multiple_variable(5, 5, 3)) # 22


#Lambda Function Inside Another Function

# def power(x):
#     return lambda n : x ** n


# cube = power(2)(3)   
# print(cube)        
# two_power_of_five = power(2)(5) 
# print(two_power_of_five)  