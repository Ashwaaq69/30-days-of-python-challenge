#functions
#Declaring and Calling a Function
# syntax
# Declaring a function
# def function_name():
#     codes
#     codes
# # Calling a function
# function_name()

#Function without Parameters
# def Generate_full_name():
#     first_name = 'ashuu'
#     last_name = 'mohaz'
#     space = ' '
#     full_name = first_name + space + last_name
#     print(full_name)
#     Generate_full_name()
    
# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     print(total)
# add_two_numbers() 

#Function Returning a Value - Part 1

# def Generate_full_name():
#     first_name = 'ashuu'
#     last_name = 'mohaz'
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print(Generate_full_name())


# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     return total
# print(add_two_numbers())


#Function with Parameters
# def greeting (name):
#     message = name + ', welcome to python for everyone!'
#     return message
# print(greeting('Ashuu'))

# def add_ten(num):
#     ten = 10
#     return num + ten
# print(add_ten(90))

# def square_number(x):
#     return x * x
# print(square_number(2))

# def area_of_circle (r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(10))

# def sum_of_numbers(n):
#     total = 0
#     for i in range(n+1):
#         total+=i
#     print(total)
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050


# def generate_fullname(first_name, last_name):
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print('full name:', generate_fullname('Ashuu', 'Mohaz'))
    
# def sum_two_numbers (num_one, num_two):
#     sum = num_one + num_two
#     return sum
# print('Sum of two numbers: ', sum_two_numbers(1, 9))

# def calculate_age (current_year, birth_year):
#     age = current_year - birth_year
#     return age;

# print('Age: ', calculate_age(2021, 1819))

# def weight_of_object (mass, gravity):
#     weight = str(mass * gravity)+ ' N' 
#     return weight
# print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))    


#Passing Arguments with Key and Value

# def print_fullname(firstname, lastname):
#     space = ' '
#     full_name = firstname  + space + lastname
#     print(full_name)
# print(print_fullname(firstname = 'Ashuu', lastname = 'Mohaz'))

# def add_two_numbers (num1, num2):
#     total = num1 + num2
#     print(total)
# print(add_two_numbers(num2 = 3, num1 = 2)) 

#Function Returning a Value - Part 2
#returning a str
# def print_name(firstname):
#     return firstname
# print_name('Ashuu') 

# def print_full_name(firstname, lastname):
#     space = ' '
#     full_name = firstname  + space + lastname
#     return full_name
# print_full_name(firstname='Miki', lastname='mohaz')


#returning a num
# def add_two_numbers (num1, num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(2, 3))

# def calculate_age (current_year, birth_year):
#     age = current_year - birth_year
#     return age;
# print('Age: ', calculate_age(2019, 1819))

#returning boolean
# def is_even(n):
#     if n % 2 == 0:
#         print('Even')
#         return True
#     return False
# print(is_even(10))  # Output: Even True
# print(is_even(11))  # Output: False

# returning a list 
# def find_even_nums(n):
#     even_numbers = []
#     for i in range(n+1):
#         if i % 2 == 0:
#             even_numbers.append(i)
#     return even_numbers
# print(find_even_nums(10))

#Function with Default Parameters

# def greetings (name = 'miki'):
#     message = name + ', welcome to Python for Everyone!'
#     return message
# print(greetings())
# print(greetings('Ashuu'))

# def generate_full_name (first_name = 'Ashuu', last_name = 'Mohaz'):
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name

# print(generate_full_name())
# print(generate_full_name('Miki','suufi'))

# def calculate_age (birth_year,current_year = 2021):
#     age = current_year - birth_year
#     return age;
# print('Age: ', calculate_age(1821))

# def weight_of_object (mass, gravity = 9.81):
#     weight = str(mass * gravity)+ ' N'
#     return weight
# print('Weight of an object in Newtons: ', weight_of_object(100)) 
# print('Weight of an object in Newtons: ', weight_of_object(100, 1.62))

#Arbitrary Number of Arguments

# def sum_all_nums(*nums):
#     total = 0
#     for num in nums:
#         total += num     
#     return total
# print(sum_all_nums(2, 3, 5)) 

#Default and Arbitrary Number of Parameters in Functions

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Ashuu','Miki','Moha','suufi'))


#Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) 